# -*- coding: utf-8 -*-

from __future__ import print_function, division

import sys
from os.path import basename, isfile
from dateutil import parser as dateparser
from dateutil.parser._parser import ParserError as DateParserError
from traceback import format_exc

from PySide2.QtCore import *
from PySide2.QtWidgets import *

import numpy as np

from matplotlib import rcParams, dates
from matplotlib.figure import Figure
from matplotlib.colors import to_hex
#from matplotlib.lines import Line2D
#from matplotlib import ticker, dates
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar

from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_options_plot import Ui_PlotOptions
from ui.ui_options_line import Ui_LineOptions
from ui.ui_dialog_view_file import Ui_ViewFileDialog


__all__ = 'array_from_file', 'add_file', 'add_array', 'start'

_icon_base64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAD1BMVEU9S8398wXFw8Xt6+39//2jZEuFAAAAU0lEQVQI103O0Q2AIAwEUD66gIkTqAOA1wEo3P4zKaUY+/VyueSajrh0sSvBNkDqgG17AOY4CwqA+026qWpzVK1RFvGEzLMM5Fkmhe2Hb2JhvfEAWLIaQGXGTJoAAAAASUVORK5CYII="


def array_from_file(filename, dateparserinfo=None):
    """Get a 2D numpy array of float (or date represented as float in the matplotlib standard) from a file."""
    data = []
    with open(filename) as file:
        if filename.endswith(".csv"):
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
                                row.append(dates.date2num(dateparser.parse(val, dateparserinfo)))
                            except DateParserError:
                                break
                    if len(row) > 1:
                        data.append(row)
                return np.array(data)

        for line in file:
            line = line.replace(",", " ")
            row = []
            for val in line.split():
                try:
                    row.append(float(val))
                except ValueError:
                    try:
                        row.append(dates.date2num(dateparser.parse(val, dateparserinfo)))
                    except DateParserError:
                        break
            if len(row) > 1:
                data.append(row)
    return np.array(data)


fig = Figure()
ax = fig.add_subplot()


_files_to_load = []
_data_to_load = {}

suppress_errors = False
"""bool: Whether to hide errors and other output from add_file and add_array"""


def add_file(filename):
    """
    Add a file to be loaded.

    Parameters
    ----------
    filename : str
        The file to be loaded (should be 2d).

    Returns
    -------
    success : bool
        True if successful, false otherwise.

    Notes
    -----
        `filename` should have at least 2 rows and 2 columns.
    """
    if isfile(filename):
        _files_to_load.append(filename)
        return True
    if not suppress_errors:
        print(f"[PloPy]: '{filename}' is not a file.")
    return False


def add_array(array, name):
    """
    Add an array to be loaded.

    Parameters
    ----------
    array : np.array or list-like of list-like of float
        The data to be loaded (should be 2d).
    name : str
        The name to be used for the tab. Must be unique,
        or it will overwrite another array.

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
        return False
    if len(array.shape) == 2:
        if name in _data_to_load and not suppress_errors:
            print(f"[PloPy]: Array {name} updated (it was already loaded).")
        _data_to_load[name] = array
        return True
    if not suppress_errors:
        print("[PloPy]: Array must be 2D (of columns and rows).")
    return False


class ViewFileDialog(QDialog):
    def __init__(self, data, filename, *args, **kwargs):
        self.__has_loaded_raw = False
        super().__init__(*args, **kwargs)
        self.setWindowTitle(f"Plo.Py - View {basename(filename)}")
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

    def populate_raw(self, max=None):
        with open(self.filename) as f:
            lines = []
            for i, line in enumerate(f):
                lines.append(line)
                if max and i > max:
                    break
        self.ui.raw_text.setPlainText("".join(lines))
        self.__has_loaded_raw = True


class LineOptions(QDialog):
    linestyles = "-", "--", ":", "-.", ""
    markerformats = "o", "^", "s", "p", "h", "*", "+", ".", ",", ""

    def __init__(self, master, line, x, y, *args, **kwargs):
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

        self.ui.line_width.setWhatsThis(f"The width of the line.\nDefault: {rcParams['lines.linewidth']}")
        self.ui.marker_size.setWhatsThis(f"The area of each marker.\nDefault: {rcParams['lines.markersize']}")

    def update_xcol(self, index):
        self.line.set_xdata(self.master.data[:, index])
        self.master.relim()

    def update_ycol(self, index):
        self.line.set_ydata(self.master.data[:, index])
        self.master.relim()

    def update_label(self, text):
        self.line.set_label(text)
        self.master.relabel()

    def update_line_format(self, index):
        self.line.set_linestyle(self.linestyles[index])
        self.master.update()

    def update_marker_format(self, index):
        self.line.set_marker(self.markerformats[index])
        self.master.update()

    def update_line_width(self, n):
        self.line.set_linewidth(n)
        self.master.update()

    def update_marker_size(self, n):
        self.line.set_markersize(n)
        self.master.update()

    def update_color(self, dialog=True):
        if dialog:
            color = QColorDialog.getColor()
            if not color.isValid():
                return
            color = color.name()  # to hex
            self.line.set_c(color)
            self.master.update()
        else:
            color = to_hex(self.line.get_c())
        self.ui.color_frame.setStyleSheet(f"#color_frame {{background-color: {color}}}")


class PlotOptions(QDialog):
    def __init__(self, filename, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filename = filename
        self.setWindowTitle(f"Plo.Py - {basename(self.filename)}")
        self.ui = Ui_PlotOptions()
        self.ui.setupUi(self)

        self.data = array_from_file(self.filename)
        if len(self.data.shape) < 2:
            print(self.data)
        self.current_line_number = 1

        self.ui.line_button.pressed.connect(self.add_line)
        self.add_line()

        self.ui.tab_widget.tabCloseRequested.connect(self.remove_tab)

        self.ui.detail_button.pressed.connect(self.detail_dialog)

    def remove_tab(self, index):
        widget = self.ui.tab_widget.widget(index)
        if widget is not None:
            ax.lines.remove(widget.line)
            self.relim()
            widget.deleteLater()
        self.ui.tab_widget.removeTab(index)

    def add_line(self):
        y_col = self.current_line_number if self.current_line_number < self.data.shape[1] else 1
        line = ax.plot(self.data[:, 0], self.data[:, y_col], label=basename(self.filename))[0]

        w = LineOptions(self, line, 0, y_col)
        self.ui.tab_widget.addTab(w, f"Line {self.current_line_number}")
        self.current_line_number += 1

        self.relabel()

    def update(self):
        """
        Redraw the canvas.
        Weakest level of updating.
        """
        fig.canvas.draw()

    def relabel(self):
        """
        Update the legend and redraw the canvas.
        Second-weakest level of updating.
        """
        handles, labels = ax.get_legend_handles_labels()
        if labels:
            ax.legend(handles, labels)
        else:
            l = ax.get_legend()
            if l: l.remove()
        self.update()

    def relim(self):
        """
        Recalculate axes limits, update the legend, and redraw the canvas.
        Strongest level of updating.
        """
        ax.relim()
        ax.autoscale()
        self.relabel()

    def detail_dialog(self):
        ViewFileDialog(self.data, self.filename).exec_()


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dialogs = {}

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        canvas = FigureCanvas(fig)
        self.ui.verticalLayout.addWidget(canvas)
        self.addToolBar(Qt.BottomToolBarArea,
                        NavigationToolbar(canvas, self))

        self.ui.actionOpen_Data_File.triggered.connect(self.choose_data_files)
        self.ui.actionPlot_Options_Open_Data_File.triggered.connect(self.choose_data_files)

        for i, c in enumerate(rcParams['axes.prop_cycle'].by_key()['color']):
            QColorDialog.setCustomColor(i, c)

        self.show()
        qapp.processEvents()
        self.add_data_files(_files_to_load)

    def choose_data_files(self):
        filenames, extension = QFileDialog.getOpenFileNames(self,
            "Plo.Py - Open Data File", None, "Text Files (*.txt *.csv *.dat);;All Files (*)")
        self.add_data_files(filenames)

    def add_data_files(self, filenames):
        if filenames:
            pbar = QProgressBar(maximum=len(filenames)+1, alignment=Qt.AlignCenter)
            self.ui.statusbar.addPermanentWidget(pbar)

            for i, filename in enumerate(filenames, start=1):
                pbar.setFormat(f"Loading Files ({i}/{len(filenames)}): {basename(filename)}")
                pbar.setValue(i)
                qapp.processEvents()

                action = QAction(basename(filename), self)

                self.dialogs[filename] = PlotOptions(filename)
                action.triggered.connect(lambda: self.plot_options(filename))

                self.ui.menuPlot_Options.addAction(action)

            if hasattr(self.ui, 'actionPlot_Options_Open_Data_File'):
                self.ui.actionPlot_Options_Open_Data_File.deleteLater()
                del self.ui.actionPlot_Options_Open_Data_File

            for filename in filenames:
                self.dialogs[filename].show()

            pbar.deleteLater()

    def plot_options(self, filename):
        d = self.dialogs[filename]
        d.show()
        d.raise_()
        d.activateWindow()


def start():
    """
    Open the GUI.
    Note that this function should be called after preselecting data.
    """
    global qapp
    qapp = QApplication.instance()
    if not qapp:
        qapp = QApplication(sys.argv)

    app = MainWindow()
    return qapp.exec_()


if __name__ == "__main__":
    exit(start())
