# -*- coding: utf-8 -*-

import sys
import os.path
from datetime import datetime
from dateutil import parser as dateparser
from dateutil.parser import ParserError as DateParserError
from traceback import format_exc, print_exc
from io import BytesIO
import warnings

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import QStandardItemModel, QStandardItem, QImage, QIcon, QAction, QDesktopServices

import numpy as np

from matplotlib import rcParams, ticker, dates as mpldates
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from matplotlib.colors import to_hex
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar

from .ui.ui_mainwindow import Ui_MainWindow
from .ui.ui_options_figure import Ui_FigureOptions
from .ui.ui_options_axes import Ui_AxesOptions
from .ui.ui_options_axes_add import Ui_AddAxesOptions
from .ui.ui_options_axes_lim import Ui_AxesLimOptions
from .ui.ui_options_plot import Ui_PlotOptions
from .ui.ui_options_line import Ui_LineOptions
from .ui.ui_dialog_load_advanced import Ui_AdvancedLoadDialog
from .ui.ui_dialog_view_array import Ui_ViewArrayDialog
from .ui.ui_dialog_view_file import Ui_ViewFileDialog
from .ui.ui_options_parser import Ui_ParserOptionsDialog


rcParams['savefig.directory'] = ""


__all__ = 'array_from_file', 'add_file', 'add_array', 'start', 'fig', 'ax'


dateparser_kw = {}

def array_from_file(filename, date_format=None, dateparser_kw=dateparser_kw):
    """
    Get a 2D numpy array of float (or date represented as float in
    the matplotlib standard) from a file.

    Parameters
    ----------
    filename : str
        The path to the file to be loaded.
    date_format : str or None
        If None, `dateutil.parser.parse` is used, which automatically
        guesses the format (but uses `dateparser_kw` to figure out
        ambiguous dates).
        Otherwise, the str is used in `datetime.datetime.strptime`
        for faster loading.
    dateparser_kw : dict
        Keyword options for `dateutil.parser.parse`.

    Notes
    -----
    If the filename ends with `.csv` and the first two lines contain a `,`
    lines will be split on commas only, otherwise on any combination
    of commas or whitespace.

    If a value cannot be directly converted to a float, it will be
    parsed as a date using `dateutil.parser.parse`, and if that fails
    the whole line is assumed to be a header and discarded.

    If `date_format` is specified, `datetime.datetime.strptime` is used
    instead to parse dates, which can run significantly faster
    (31 vs 142 seconds on a 86 MB file).
    """
    data = []
    with open(filename) as file:
        if date_format:
            if filename.endswith(".csv"):
                line = file.readline() + file.readline()
                file.seek(0)
                if "," in line:
                    for line in file:
                        row = []
                        for val in line.split(","):
                            try:
                                row.append(float(val))
                            except ValueError:
                                try:
                                    row.append(mpldates.date2num(datetime.strptime(val, date_format)))
                                except ValueError:
                                    break
                        if len(row) > 1:
                            data.append(row)
                    return np.array(data)

            for line in file:
                row = []
                for val in line.replace(",", " ").split():
                    try:
                        row.append(float(val))
                    except ValueError:
                        try:
                            row.append(mpldates.date2num(datetime.strptime(val, date_format)))
                        except ValueError:
                            break
                if len(row) > 1:
                    data.append(row)

        elif filename.endswith(".csv"):
            line = file.readline()
            file.seek(0)
            if "," in line:
                for line in file:
                    row = []
                    for val in line.split(","):
                        try:
                            row.append(float(val))
                        except ValueError:
                            try:
                                row.append(mpldates.date2num(dateparser.parse(val, **dateparser_kw)))
                            except DateParserError:
                                break
                    if len(row) > 1:
                        data.append(row)
                return np.array(data)

        else:
            for line in file:
                row = []
                for val in line.replace(",", " ").split():
                    try:
                        row.append(float(val))
                    except ValueError:
                        try:
                            row.append(mpldates.date2num(dateparser.parse(val, **dateparser_kw)))
                        except DateParserError:
                            break
                if len(row) > 1:
                    data.append(row)
    return np.array(data)


class ParserOptionsDialog(QDialog):
    date_formats_kw = [{"dayfirst": False, "yearfirst": True},   # YMD
                       {"dayfirst": True, "yearfirst": False},   # DMY
                       {"dayfirst": False, "yearfirst": False},  # MDY
                       {"dayfirst": True, "yearfirst": True}]    # YDM
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_ParserOptionsDialog()
        self.ui.setupUi(self)

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)  # hide ? button

        try:
            self.ui.date_format.setCurrentIndex(self.date_formats_kw.index(dateparser_kw))
        except ValueError:
            pass

        self.accepted.connect(self.apply_config)

    def apply_config(self):
        dateparser_kw.update(self.date_formats_kw[self.ui.date_format.currentIndex()])


fig = Figure()
"""
Instance of `matplotlib.figure.Figure`. Can be used to pre-configure the plot,
just like when using ``fig, ax = plt.subplots()``
"""
ax = fig.add_subplot()
"""
A subplot of `fig`. Can be used to pre-configure the plot,
just like when using ``fig, ax = plt.subplots()``, or removed and replaced
by a grid of axes using `fig.add_subplot()`
"""

_files_to_load = []
_data_to_load = []

suppress_errors = False
"""bool: Whether to hide errors and other output from `add_file` and `add_array.`"""


def add_file(filename):
    """
    Add a file to be loaded.

    Parameters
    ----------
    filename : str
        The file to be loaded.

    Returns
    -------
    success : bool
        True if successful, false otherwise.

    Notes
    -----
        `filename` should have at least 2 rows and 2 columns of data.
    """
    if not suppress_errors and not os.path.isfile(filename):
        print(f"[PloPy]: '{filename}' is not a file.")
        return False
    _files_to_load.append(filename)
    return True


def add_array(array, name=None, raise_=False):
    """
    Add an array to be loaded.

    Parameters
    ----------
    array : np.array or iterable of iterable of float
        The data to be loaded.
    name : str or None
        The name to be used for the tab.
    raise : bool
        Whether to raise the exception if one is caused
        by converting the input to a numpy array.

    Returns
    -------
    success : bool
        True if successful, false otherwise.

    Notes
    -----
        `array` should have at least 2 rows and 2 columns.
    """
    try:
        array = np.array(array)
    except Exception:
        print(f"[PloPy]: Could not convert {name} into numpy array")
        if raise_:
            raise
        return False
    if len(array.shape) == 2:
        _data_to_load.append((array, name))
        return True
    if not suppress_errors:
        print("[PloPy]: Array must be 2D (of columns and rows).")
    return False


def update():
    """
    Redraw the canvas.
    Weakest level of updating.
    """
    fig.canvas.draw()

def relabel(axes, draw=True):
    """
    Update the legend and redraw the canvas.
    Second-weakest level of updating.

    Necessary after changing a line's label, markers, or linestyle.
    """
    handles, labels = axes.get_legend_handles_labels()
    if labels:
        axes.legend(handles, labels, loc=axes.plopy_legend_loc)
    else:
        l = axes.get_legend()
        if l: l.remove()
    if draw:
        update()

def relim(axes, draw=True):
    """
    Recalculate axes limits, update the legend, and redraw the canvas.
    Strongest level of updating.
    """
    axes.relim()
    axes.autoscale()
    relabel(axes, draw)


def axes_to_str(axes):
    """Return the location of the axes as the string "Axes (`nrows`, `ncols`, `index`)" """
    return f"Axes {str(axes.get_gridspec())[8:-1]}, {axes.get_subplotspec().num1+1})"


class FigureCanvasCustom(FigureCanvas):
    def get_window_title(self):
        title = None
        if self.figure._suptitle:
            title = self.figure._suptitle.get_text()
        if not title:
            for axes in self.figure.axes:
                title = axes.get_title()
                if title:
                    break
        if not title:
            return super().get_window_title()
        return title


class ViewArrayDialog(QDialog):
    def __init__(self, parent, data, name, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, windowTitle=f"Plo.Py - View {name}")
        self.ui = Ui_ViewArrayDialog()
        self.ui.setupUi(self)
        self.data = data

        self.ui.data_load_all.pressed.connect(self.populate_table)
        self.populate_table(max=20)

    def populate_table(self, max=None):
        xlen, ylen = self.data.shape
        if max:
            if xlen > max: xlen = max
            if ylen > max: ylen = max

        self.ui.data_table.setRowCount(xlen)
        self.ui.data_table.setColumnCount(ylen)

        for x in range(xlen):
            for y in range(ylen):
                self.ui.data_table.setItem(x, y, QTableWidgetItem(str(self.data[x, y])))


class ViewFileDialog(ViewArrayDialog):
    def __init__(self, parent, data, filename, *args, **kwargs):
        self.__has_loaded_raw = False
        QDialog.__init__(self, parent, *args, **kwargs, windowTitle=f"Plo.Py - View {os.path.basename(filename)}")
        self.ui = Ui_ViewFileDialog()
        self.ui.setupUi(self)
        self.data = data
        self.filename = filename

        self.ui.data_load_all.pressed.connect(self.populate_table)
        self.ui.raw_load_all.pressed.connect(self.populate_raw)

        self.populate_table(max=20)
        self.ui.tabWidget.currentChanged.connect(self.tab_change)

    def tab_change(self, index):
        if self.__has_loaded_raw is False and index == 1:
            try:
                self.populate_raw(max=20)
            except Exception:
                self.ui.raw_text.setPlainText(format_exc())

    def populate_raw(self, max=None):
        with open(self.filename) as f:
            lines = []
            for i, line in enumerate(f):
                lines.append(line)
                if max and i > max:
                    break
        self.ui.raw_text.setPlainText("".join(lines))
        self.__has_loaded_raw = True


class AdvancedLoadDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_AdvancedLoadDialog()
        self.ui.setupUi(self)

    def setup_current_time(self):
        table = self.ui.date_format_table
        current_time = datetime.now()
        for row in range(table.rowCount()):
            table.setItem(row, 1, QTableWidgetItem(current_time.strftime(table.verticalHeaderItem(row).text())))

    def choose_data_files(self):
        filenames, extension = QFileDialog.getOpenFileNames(self,
            "Plo.Py - Open Data File", None, "Text Files (*.txt *.csv *.dat);;All Files (*)")

    def exec_(self):
        self.setup_current_time()
        return super().exec_()


class LineOptions(QWidget):
    linestyles = "-", "--", ":", "-.", ""
    markerformats = "o", "^", "s", "p", "h", "*", "+", ".", ",", ""

    def __init__(self, master, line, x, y, axes_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master = master
        self.line = line

        self.ui = Ui_LineOptions()
        self.ui.setupUi(self)

        col_names = [f"Column {i}" for i in range(1, self.master.data.shape[1]+1)]
        self.ui.x_column.addItems(col_names)
        self.ui.x_column.setCurrentIndex(x)
        self.ui.y_column.addItems(col_names)
        self.ui.y_column.setCurrentIndex(y)

        self.ui.x_column.currentIndexChanged.connect(self.update_xcol)
        self.ui.y_column.currentIndexChanged.connect(self.update_ycol)
        self.ui.legend_label.setText(line.get_label())
        self.ui.legend_label.textChanged.connect(self.update_label)
        self.ui.line_format.currentIndexChanged.connect(self.update_line_format)
        self.ui.marker_format.currentIndexChanged.connect(self.update_marker_format)
        self.ui.line_width.setValue(line.get_linewidth())
        self.ui.line_width.valueChanged.connect(self.update_line_width)
        self.ui.marker_size.setValue(line.get_markersize())
        self.ui.marker_size.valueChanged.connect(self.update_marker_size)
        self.update_color(dialog=False)
        self.ui.set_color.pressed.connect(self.update_color)

        self.ui.axes_select.setModel(axes_list)
        self.ui.axes_select.currentTextChanged.connect(self.update_axes)

        self.ui.line_width.setWhatsThis(f"The width of the line.\nDefault: {rcParams['lines.linewidth']}")
        self.ui.marker_size.setWhatsThis(f"The area of each marker.\nDefault: {rcParams['lines.markersize']}")

    def update_xcol(self, index):
        self.line.set_xdata(self.master.data[:, index])
        relim(self.line.axes)

    def update_ycol(self, index):
        self.line.set_ydata(self.master.data[:, index])
        relim(self.line.axes)

    def update_label(self, text):
        self.line.set_label(text)
        relabel(self.line.axes)

    def update_line_format(self, index):
        self.line.set_linestyle(self.linestyles[index])
        relabel(self.line.axes)

    def update_marker_format(self, index):
        self.line.set_marker(self.markerformats[index])
        relabel(self.line.axes)

    def update_line_width(self, n):
        self.line.set_linewidth(n)
        relabel(self.line.axes)

    def update_marker_size(self, n):
        self.line.set_markersize(n)
        relabel(self.line.axes)

    def update_color(self, dialog=True):
        color = to_hex(self.line.get_c())
        if dialog:
            new_qcolor = QColorDialog.getColor(color, self)
            if not new_qcolor.isValid():
                return
            color = new_qcolor.name()  # to hex
            self.line.set_c(color)
            relabel(self.line.axes)
        self.ui.color_frame.setStyleSheet(f"#color_frame {{background-color: {color}}}")

    def update_axes(self, text):
        new_axes = next((axes for axes in fig.axes if axes.plopy_name == text), None)
        if not new_axes:
            print(self.line, "could not be moved to a new axes.")
            return
        old_axes = self.line.axes
        self.line.remove()
        self.line.axes = new_axes
        self.line.set_transform(new_axes.transData)
        new_axes.add_line(self.line)
        relim(old_axes, draw=False)
        relim(new_axes)


class ArrayPlotDialog(QDockWidget):
    _title_count = 0
    @classmethod
    def generate_title(cls):
        cls._title_count += 1
        return f"Array {cls._title_count}"

    def __init__(self, parent, data, axes_list, windowTitle=None, *args, add_initial_line=True, **kwargs):
        if len(data.shape) != 2:
            raise ValueError(f"data.shape should have length 2, instead was {data.shape}")
        self.parent = parent
        self.data = data
        self.axes_list = axes_list  # synced to update the line's axes chooser
        if not windowTitle:
            windowTitle = self.generate_title()
        super().__init__(parent, *args, **kwargs, windowTitle=windowTitle)
        self.ui = Ui_PlotOptions()
        self.ui.setupUi(self)

        self.current_line_number = 1

        self.ui.line_button.pressed.connect(self.add_new_line)
        self.ui.tab_widget.tabCloseRequested.connect(self.remove_tab)
        self.ui.detail_button.pressed.connect(self.detail_dialog)

        self.topLevelChanged.connect(self.resize_when_floating)

        if add_initial_line: self.add_new_line()

    def remove_tab(self, index):
        widget = self.ui.tab_widget.widget(index)
        if widget is not None:
            axes = widget.line.axes
            axes.lines.remove(widget.line)
            relim(axes)
            widget.deleteLater()
        self.ui.tab_widget.removeTab(index)

    def add_new_line(self):
        y_col = self.current_line_number if self.current_line_number < self.data.shape[1] else 1
        line, = fig.axes[0].plot(self.data[:, 0], self.data[:, y_col],
                                 label=f"{self.windowTitle()} Line {self.current_line_number}")
        self.add_line(line)

        relabel(line.axes)

    def add_line(self, line):
        y_col = self.current_line_number if self.current_line_number < self.data.shape[1] else 1
        w = LineOptions(self, line, 0, y_col, self.axes_list)
        self.ui.tab_widget.setCurrentIndex(self.ui.tab_widget.addTab(w, f"Line {self.current_line_number}"))
        self.current_line_number += 1

    def detail_dialog(self):
        ViewArrayDialog(self.parent, self.data, self.windowTitle()).exec_()

    def show(self):
        super().show()
        self.raise_()
        self.activateWindow()

    def resize_when_floating(self, is_toplevel):
        """Resize to minimum (called when docked/undocked)"""
        if is_toplevel:  # only when undocked
            self.resize(0, 0)


class FilePlotDialog(ArrayPlotDialog):
    def __init__(self, parent, filename, axes_list, date_format=None, *args, **kwargs):
        super().__init__(parent, array_from_file(filename, date_format), axes_list, *args, **kwargs, windowTitle=os.path.basename(filename))
        self.filename = filename

    def detail_dialog(self):
        ViewFileDialog(self.parent, self.data, self.filename).exec_()


class AddAxesDialog(QDialog):
    def __init__(self, fd, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fd = fd
        self.ui = Ui_AddAxesOptions()
        self.ui.setupUi(self)

        self.ui.nrows.valueChanged.connect(self.update_max_index)
        self.ui.ncols.valueChanged.connect(self.update_max_index)
        self.ui.index.valueChanged.connect(self.update_radiobutton_state)

    def update_max_index(self):
        self.ui.index.setMaximum(self.ui.nrows.value() * self.ui.ncols.value())
        self.update_radiobutton_state()

    def update_radiobutton_state(self):
        location = self.ui.nrows.value(), self.ui.ncols.value(), self.ui.index.value()
        exists = f"Axes {location}" in (axes.plopy_name for axes in fig.axes)
        self.ui.radio_new.setEnabled(not exists)
        self.ui.radio_twinx.setEnabled(exists)
        self.ui.radio_twiny.setEnabled(exists)

    def show(self):
        self.update_max_index()
        super().show()
        self.raise_()
        self.activateWindow()


class AxesLimDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_AxesLimOptions()
        self.ui.setupUi(self)

        self.current_ax = None
        self.previous_values = None  # ((x1, x2), (y1, y2))

        self.ui.xmin.setRange(float('-inf'), float('inf'))
        self.ui.xmax.setRange(float('-inf'), float('inf'))
        self.ui.ymin.setRange(float('-inf'), float('inf'))
        self.ui.ymax.setRange(float('-inf'), float('inf'))

        self.accepted.connect(self.set_axes_lim)

        self.ui.load_current.pressed.connect(self.update_from_axes)
        self.ui.load_previous.pressed.connect(self.update_from_previous)

    def set_axes_lim(self):
        self.previous_values = x, y = (self.ui.xmin.value(), self.ui.xmax.value()), (self.ui.ymin.value(), self.ui.ymax.value())
        self.current_ax.set_xlim(x)
        self.current_ax.set_ylim(y)
        update()
        self.ui.load_previous.setEnabled(True)

    def update_from_axes(self):
        s, e = self.current_ax.get_xlim()
        self.ui.xmin.setValue(s)
        self.ui.xmax.setValue(e)

        s, e = self.current_ax.get_ylim()
        self.ui.ymin.setValue(s)
        self.ui.ymax.setValue(e)

    def update_from_previous(self):
        if self.previous_values:
            (x1, x2), (y1, y2) = self.previous_values
            self.ui.xmin.setValue(x1)
            self.ui.xmax.setValue(x2)

            self.ui.ymin.setValue(y1)
            self.ui.ymax.setValue(y2)

    def show(self, ax):
        self.current_ax = ax
        self.ui.axes_box.setText(ax.plopy_name)
        self.update_from_axes()

        super().show()
        self.raise_()
        self.activateWindow()


class AxesOptions(QWidget):
    legend_locations = ("best", "upper right", "upper left", "lower right", "lower left",
                        "upper center", "lower center", "center right", "center left", "center")
    def __init__(self, axes, limit_dialog, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.axes = axes
        self.ui = Ui_AxesOptions()
        self.ui.setupUi(self)

        self.ui.title.textEdited.connect(self.set_title)
        self.ui.x_label.textEdited.connect(self.set_xlabel)
        self.ui.y_label.textEdited.connect(self.set_ylabel)
        self.ui.x_tick_type.currentTextChanged.connect(self.set_xticks)
        self.ui.y_tick_type.currentTextChanged.connect(self.set_yticks)

        self.ui.frame.stateChanged.connect(self.set_frame)
        self.ui.grid.stateChanged.connect(self.set_grid)
        self.ui.equal_aspect.stateChanged.connect(self.set_aspect)
        self.ui.configure_limits.pressed.connect(lambda: limit_dialog.show(axes))
        self.ui.tick_direction.currentIndexChanged.connect(self.set_tick_direction)

        axes.plopy_legend_loc = None  # keeps track of legend loc for relabel(axes)
        self.ui.legend_loc.currentIndexChanged.connect(self.set_legend_loc)

        #self.ui.legend_loc.insertSeparator(1)
        #self.ui.legend_loc.insertSeparator(5)
        #self.ui.legend_loc.insertSeparator(9)

    def setup(self, _=None):
        if "Twin" in self.axes.plopy_name:
            if "TwinX" in self.axes.plopy_name:
                self.ui.x_gbox.setEnabled(False)
                self.ui.y_label.setText(self.axes.get_ylabel())
            else:
                self.ui.y_gbox.setEnabled(False)
                self.ui.x_label.setText(self.axes.get_xlabel())
        else:
            self.ui.title.setText(self.axes.get_title())

    def set_title(self, text):
        self.axes.set_title(text)
        update()

    def set_xlabel(self, text):
        self.axes.set_xlabel(text)
        update()

    def set_ylabel(self, text):
        self.axes.set_ylabel(text)
        update()

    @staticmethod
    def set_axis_ticks(axis, selection):
        if selection.startswith("Normal"):
            axis.set_major_locator(ticker.AutoLocator())
            axis.set_major_formatter(ticker.ScalarFormatter())
        elif selection.startswith("Date"):
            l = mpldates.AutoDateLocator()
            axis.set_major_locator(l)
            axis.set_major_formatter(mpldates.AutoDateFormatter(l))
        elif selection == "Blank":
            axis.set_major_locator(ticker.NullLocator())

        if selection.endswith("minor ticks"):
            axis.set_minor_locator(ticker.AutoMinorLocator())
        else:
            axis.set_minor_locator(ticker.NullLocator())

    def set_xticks(self, selection):
        try:
            if selection.endswith("Logarithmic"):
                self.set_axis_ticks(self.axes.xaxis, "Normal")
                self.axes.set_xscale('log' if selection == "Logarithmic" else 'symlog')
            else:
                self.axes.set_xscale('linear')
                self.set_axis_ticks(self.axes.xaxis, selection)

            update()
        except Exception as e:
            print("Error when configuring x ticks:", e)
            if selection != "Blank":
                self.ui.x_tick_type.setCurrentText("Blank")  # note: this will re-run this function

    def set_yticks(self, selection):
        try:
            if selection.endswith("Logarithmic"):
                self.set_axis_ticks(self.axes.yaxis, "Normal")
                self.axes.set_yscale('log' if selection == "Logarithmic" else 'symlog')
            else:
                self.axes.set_yscale('linear')
                self.set_axis_ticks(self.axes.yaxis, selection)

            update()
        except Exception as e:
            print("Error when configuring y ticks:", e)
            if selection != "Blank":
                self.ui.y_tick_type.setCurrentText("Blank")  # note: this will re-run this function

    def set_tick_direction(self, index):
        self.axes.tick_params(which='both', direction=('out', 'in', 'inout')[index])
        update()

    def set_legend_loc(self, index):
        self.axes.plopy_legend_loc = self.legend_locations[index]
        relabel(self.axes)

    def set_frame(self, b):
        self.axes.set_frame_on(b)
        update()

    def set_grid(self, b):
        self.axes.grid(b)
        update()

    def set_aspect(self, b):
        self.axes.set_aspect('equal' if b else 'auto')
        update()


class FigureDialog(QDockWidget):
    def __init__(self, mainwindow, axes_list, figure=fig, *args, **kwargs):
        super().__init__(mainwindow, *args, **kwargs)
        self.figure = figure
        self.axes_list = axes_list
        self.ui = Ui_FigureOptions()
        self.ui.setupUi(self)

        if figure._suptitle:
            self.ui.title.setText(figure._suptitle.get_text())
        self.ui.tight_layout.setCheckState(Qt.Checked if figure.get_tight_layout() else Qt.Unchecked)

        self.ui.title.textChanged.connect(self.set_title)
        self.ui.tight_layout.stateChanged.connect(self.set_layout)

        self.axes_lim_dialog = AxesLimDialog(mainwindow)

        for axes in figure.axes:
            self.add_axes(axes)

        self.add_axes_dialog = AddAxesDialog(self)
        self.ui.axes_button.pressed.connect(self.add_axes_dialog.show)
        self.add_axes_dialog.accepted.connect(self.create_axes)

        self.ui.tab_widget.tabCloseRequested.connect(self.remove_tab)

        self.topLevelChanged.connect(self.resize_when_floating)

    def set_title(self, text):
        self.figure.suptitle(text)
        update()

    def set_layout(self, b):
        self.figure.set_tight_layout(True if b else None)
        update()

    def remove_tab(self, index):
        widget = self.ui.tab_widget.widget(index)
        if widget is not None:
            n_lines = len(widget.axes.lines)
            name = widget.axes.plopy_name
            if n_lines and QMessageBox.Ok != QMessageBox.warning(self, "Plo.Py - Remove Axes?",
                               f"Are you sure you want to delete {name}?\nIt still has {n_lines} line{'s' if n_lines != 1 else ''} attached.",
                               QMessageBox.Ok | QMessageBox.Cancel):
                return
            self.axes_list.removeRow(self.axes_list.findItems(name)[0].row())  # remove axes name from dropdown
            widget.axes.remove()
            widget.deleteLater()
        self.ui.tab_widget.removeTab(index)
        update()

    def add_axes(self, axes):
        name = axes_to_str(axes)
        if self.axes_list.findItems(name):  # axes already exists at that location, may be a twin
            for other_ax in axes.get_shared_x_axes().get_siblings(axes):
                if other_ax is axes:
                    continue
                if other_ax.bbox.bounds == axes.bbox.bounds:
                    name += " TwinX"
                    break
            else:
                for other_ax in axes.get_shared_y_axes().get_siblings(axes):
                    if other_ax is axes:
                        continue
                    if other_ax.bbox.bounds == axes.bbox.bounds:
                        name += " TwinY"
                        break
            while self.axes_list.findItems(name):
                name += " copy"
        axes.plopy_name = name

        self.axes_list.appendRow(QStandardItem(name))  # append axes name (updates all ComboBoxes)

        tab = AxesOptions(axes, self.axes_lim_dialog)
        self.ui.tab_widget.setCurrentIndex(self.ui.tab_widget.addTab(tab, name))
        return tab

    def create_axes(self):
        d_ui = self.add_axes_dialog.ui
        location = d_ui.nrows.value(), d_ui.ncols.value(), d_ui.index.value()
        for axes in fig.axes:
            if axes.plopy_name == f"Axes {location}":
                if d_ui.radio_twinx.isChecked():
                    new_ax = axes.twinx()
                    break
                elif d_ui.radio_twiny.isChecked():
                    new_ax = axes.twiny()
                    break
                else:
                    print(f"Axes already exists at {location}, using that instead")
                    qapp.beep()
                    return
        else:
            new_ax = self.figure.add_subplot(*location)
        self.add_axes(new_ax).setup()
        update()

    def show(self):
        for i in range(self.ui.tab_widget.count()):
            self.ui.tab_widget.widget(i).setup()
        super().show()
        self.raise_()
        self.activateWindow()

    def resize_when_floating(self, is_toplevel):
        """Resize to minimum (called when docked/undocked)"""
        if is_toplevel:  # only when undocked
            self.resize(0, 0)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        _showwarning_old = warnings.showwarning
        def show_warning_new(message, category, filename, lineno, file=None, line=None):
            try:
                self.ui.statusbar.showMessage(f"Warning: {message}", 20000)
            except Exception:
                print_exc()
            _showwarning_old(message, category, filename, lineno, file, line)
        warnings.showwarning = show_warning_new

        self.icon = QIcon()
        icon_path = os.path.join(os.path.dirname(__file__), "ui", "icon_")
        self.icon.addFile(icon_path+"16x16.png", QSize(16, 16))
        self.icon.addFile(icon_path+"24x24.png", QSize(24, 24))
        self.setWindowIcon(self.icon)

        self.dialogs = {}
        self.axes_list = QStandardItemModel(self)

        canvas = FigureCanvasCustom(fig)
        self.ui.verticalLayout.addWidget(canvas)
        nav = NavigationToolbar(canvas, self)
        self.addToolBar(Qt.BottomToolBarArea, nav)

        self.ui.action_load_data_file.triggered.connect(self.choose_data_files)
        self.ui.action_load_data_file_set_format.triggered.connect(self.configure_parser)
        self.ui.action_plot_options_load_data_file.triggered.connect(self.choose_data_files)
        self.ui.action_load_data_file_advanced.triggered.connect(self.choose_data_files_adv)
        self.ui.action_save_plot.triggered.connect(nav.save_figure)
        self.ui.action_copy_plot.triggered.connect(self.copy_plot)

        canvas.setContextMenuPolicy(Qt.ActionsContextMenu)
        #canvas.setContextMenuPolicy(Qt.NoContextMenu)
        canvas.addAction(self.ui.action_save_plot)
        canvas.addAction(self.ui.action_copy_plot)

        for i, c in enumerate(rcParams['axes.prop_cycle'].by_key()['color']):
            QColorDialog.setCustomColor(i, c)

        self.ui.action_whatsthis.triggered.connect(lambda: QTimer.singleShot(200, QWhatsThis.enterWhatsThisMode))
        self.ui.action_whatsthis.setVisible(False)
        self.ui.action_website.triggered.connect(lambda: QDesktopServices.openUrl(self.ui.action_website.toolTip()))
        self.ui.action_docs.triggered.connect(lambda: QDesktopServices.openUrl(self.ui.action_docs.toolTip()))

        self.show()
        self.raise_()
        self.activateWindow()

        qapp.processEvents()

        self.adv_load_dialog = AdvancedLoadDialog(self)
        self.figoptions = FigureDialog(self, self.axes_list)
        self.ui.action_figure_options.triggered.connect(self.figoptions.show)
        nav.edit_parameters = self.figoptions.show

        def rightclick_decorator(func):
            def new_func(*args, **kw):
                func(*args, **kw)
                if nav.mode:
                    canvas.setContextMenuPolicy(Qt.NoContextMenu)
                else:
                    canvas.setContextMenuPolicy(Qt.ActionsContextMenu)
            return new_func
        nav.zoom = rightclick_decorator(nav.zoom)
        nav.pan = rightclick_decorator(nav.pan)
        #print(dir(nav))

        self.add_existing_lines()
        self.add_arrays(_data_to_load)
        self.add_data_files(_files_to_load, always_alert=True)

    def choose_data_files(self, date_format=None):
        filenames, extension = QFileDialog.getOpenFileNames(self,
            "Plo.Py - Open Data File", None, "Text Files (*.txt *.csv *.dat);;All Files (*)")
        self.add_data_files(filenames, date_format)

    def choose_data_files_adv(self):
        result = self.adv_load_dialog.exec_()
        if result == QDialog.Accepted:
            self.choose_data_files(str(self.adv_load_dialog.ui.date_format.currentText()) or None)

    def add_data_files(self, filenames, date_format=None, always_alert=False):
        if filenames:
            pbar = QProgressBar(maximum=len(filenames)+1, alignment=Qt.AlignCenter)
            self.ui.statusbar.addPermanentWidget(pbar)

            show_functions = []
            error_messages = []

            for i, filename in enumerate(filenames, start=1):
                pbar.setFormat(f"Loading Files ({i}/{len(filenames)}): {os.path.basename(filename)}")
                pbar.setValue(i)
                qapp.processEvents()

                try:
                    dialog = FilePlotDialog(self, filename, self.axes_list, date_format)
                except Exception:
                    # errors will be shown after all files have been attempted
                    error_messages.append(f"Error when loading file '{filename}'\n\n{format_exc()}")
                else:
                    self.add_plot_dialog(dialog)
                    show_functions.append(dialog.show)

            for f in show_functions:
                f()

            self.ui.statusbar.removeWidget(pbar)
            pbar.deleteLater()
            qapp.alert(self)
            qapp.processEvents()

            for msg in error_messages:
                QMessageBox.warning(self, "Plo.Py", msg)

        elif always_alert:
            qapp.alert(self)

    def add_arrays(self, arrays):
        show_functions = []
        for array, name in arrays:
            dialog = ArrayPlotDialog(self, array, self.axes_list, windowTitle=name)
            self.add_plot_dialog(dialog)
            show_functions.append(dialog.show)

        for f in show_functions:
            f()

    def add_existing_lines(self):
        for axes in fig.axes:
            for line in axes.lines:
                dialog = ArrayPlotDialog(self, line.get_xydata(), self.axes_list, add_initial_line=False, windowTitle=line.get_label())
                dialog.add_line(line)
                self.add_plot_dialog(dialog)

    def add_plot_dialog(self, dialog):
        action = QAction(dialog.windowTitle(), self)
        action.triggered.connect(dialog.show)
        self.ui.menu_plot_options.addAction(action)

        if hasattr(self.ui, 'action_plot_options_load_data_file'):
            self.ui.action_plot_options_load_data_file.deleteLater()
            del self.ui.action_plot_options_load_data_file

    def copy_plot(self):
        buffer = BytesIO()
        fig.savefig(buffer)
        qapp.clipboard().setImage(QImage.fromData(buffer.getvalue()))

    def configure_parser(self):
        d = ParserOptionsDialog(self)
        d.exec_()
        d.deleteLater()


def start():
    """
    Open the GUI.
    Note that this function should be called after preselecting data.
    """
    global qapp
    qapp = QApplication.instance()
    if not qapp:
        qapp = QApplication(sys.argv)

    # differentiate this from python.exe by giving it a unique id
    # (gets icon to show up in taskbar on windows)
    # https://stackoverflow.com/questions/1551605/#1552105
    try:
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('plopy.app.id')
    except Exception:
        pass

    app = MainWindow()
    return qapp.exec_()


if __name__ == "__main__":
    exit(start())
