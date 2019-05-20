# -*- coding: utf-8 -*-

from __future__ import print_function, division

from sys import exit, argv, executable
from os.path import basename, isfile


try:
    from matplotlib import use
except ImportError:  # install matplotlib if missing
    print("Error: matplotlib is not installed. Installing...", end="\r")
    from subprocess import call
    call([executable, "-m", "pip", "install", "matplotlib"])
    print("Installed matplotlib.                            ", end="\r")
    from matplotlib import use

use("TkAgg")
import matplotlib as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

try:
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter.filedialog import askopenfilenames, asksaveasfilename
    from tkinter.colorchooser import askcolor
    from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk as Navigation
except ImportError:
    import Tkinter as tk
    import ttk
    from tkFileDialog import askopenfilenames, asksaveasfilename
    from tkColorChooser import askcolor
    from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg as Navigation


# This program is dedicated to my parents, Lothar and Dorothee,
# for supporting me in my Python endeavors
# \UF381


_pad = 5  # Default inter-widget padding
_icon_base64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAD1BMVEU9S8398wXFw8Xt6+39//2jZEuFAAAAU0lEQVQI103O0Q2AIAwEUD66gIkTqAOA1wEo3P4zKaUY+/VyueSajrh0sSvBNkDqgG17AOY4CwqA+026qWpzVK1RFvGEzLMM5Fkmhe2Hb2JhvfEAWLIaQGXGTJoAAAAASUVORK5CYII="

def loadFile(filename):
    data = []
    try:
        with open(filename) as fileRead:
            for line in fileRead:
                line = line.replace(",", " ")
                row = []
                for num in line.split():
                    if len(num) < 1:
                        break
                    try:
                        row.append(float(num))
                    except ValueError:
                        break
                if len(row) > 1:
                    data.append(row)
        return np.array(data)
    except Exception:
        return np.array([])


class ToolTip(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

        widget.bind('<Enter>', self.showtip)
        widget.bind('<Leave>', self.hidetip)

    def showtip(self, *_):
        """Display text in tooltip window"""
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = self.widget.winfo_rootx()
        y = cy + self.widget.winfo_rooty() + 5
        if cy == 0:
            y += 18
            x += 1

        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        try:  # For Mac OS
            tw.tk.call("::tk::unsupported::MacWindowStyle",
                       "style", tw._w,
                       "help", "noActivates")
        except tk.TclError:
            pass
        label = tk.Label(tw, text=self.text,
                         background="#ffffff", relief="solid", borderwidth=1)
        label.pack(ipadx=1)

    def hidetip(self, *_):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


class CustomNotebook(ttk.Notebook):
    """A ttk Notebook with close buttons on each tab"""
    __initialized = False

    def __init__(self, *args, **kwargs):
        if not self.__initialized:
            self.__initialize_custom_style()
            self.__inititialized = True

        kwargs["style"] = "CustomNotebook"
        ttk.Notebook.__init__(self, *args, **kwargs)

        self._active = None
        self._emptyframe = None
        self._isempty = True

        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

        self._emptyframe = FrameOptions(self._root(), self, "", "", "#000000")
        self._emptyframe.line = ""
        self._emptyframe.marker = ""
        self.tab(0, state="disabled")
        print(self._emptyframe)

    def add(self, widget, **kwargs):
        ttk.Notebook.add(self, widget, **kwargs)
        if self._isempty and self._emptyframe:
            self.forget(0)
            self._isempty = False

    def forget(self, index):
        if self.winfo_children()[index] is not self._emptyframe:
            ttk.Notebook.forget(self, index)
            self.winfo_children()[index].destroy()
            self._root().update()

    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index

    def on_close_release(self, event):
        """Called when the button is released over the close button"""
        if not self.instate(['pressed']):
            return

        element = self.identify(event.x, event.y)
        index = self.index("@%d,%d" % (event.x, event.y))

        if "close" in element and self._active == index:
            self.forget(index)
            self.event_generate("<<NotebookTabClosed>>")

        self.state(["!pressed"])
        self._active = None

    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            tk.PhotoImage("img_close", data='''
                iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAAAVklEQVR4AWMYWcC
                VCDWOhBS4AfF/IG7Ho6YdqsaJkGH9MMPwGNIPEyDDMExDSDWsHogb4IaQCaaBDK
                DIEISrEAZRakgDYa9RHtiURz9dE6QrUdlo5AAAvx8nV9K3YjUAAAAASUVORK5CY
                II='''),
            tk.PhotoImage("img_closeactive", data='''
                iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAQAAAD8x0bcAAAA1UlEQVR4AZXSM0I
                GYBjA8d8et7BlHCDrCukUGUt2bbm27HOFK2TXZ//f6X0smZOvQ79+HfLFpdC1z7
                B3o1AkKtx5sqsUlNr15E6FMIrcu1crnNpfWVFIcO5di2KTAkwq1uzdOUCeD0cY8
                WkDbPg0jEMf8oAunxoElPPWfFoDDT51A2M+5QL2fQrEI9enMWDcp2zARoRRtk/j
                QE9EukWLAmb1PvVGFj4aU/hRqHBOfWiKGMGMYo0+nEYO80G1cKpFDhPlcddSHrv
                gm2QLjjyVAQORp5ImX1McV/+ToXN/AAAAAElFTkSuQmCC'''),
            tk.PhotoImage("img_closepressed", data='''
                iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAQAAAD8x0bcAAAAvUlEQVR4AZXSAeY
                CURDH8Q+wsFdo/9BN/kDFUhLSLeoM6Qh1hFA6QR2hbpJIlG0jg+VF+g7M/N68N2
                Pm+ZWWmYOzs4OZloTc1lPdsKetXIPMSS21kwzBKsTUVoK26i2sjcKrjOzCawPzu
                FWi9HBXoh/qHDh6h3HY8x/J0RdwU4dVhmCsEporcEmSho2ky6dyXd1P5RYRdpqN
                G4S6AP7i8Z1JOgKFYPl9mGSO39dCbpMseCOXUJjGV9mbKvzGC4+4qP/m7PJBAAA
                AAElFTkSuQmCC''')
        )

        style.element_create("close", "image", "img_close",
                             ("active", "pressed", "!disabled", "img_closepressed"),
                             ("active", "!disabled", "img_closeactive"), border=8, sticky='')
        style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
        style.layout("CustomNotebook.Tab", [
            ("CustomNotebook.tab", {
                "sticky": "nswe",
                "children": [
                    ("CustomNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                                    ]
                            })
                        ]
                    })
                ]
            })
        ])


class MplCanvas(ttk.Frame):
    def __init__(self, master, width=5, height=4, dpi=100):
        ttk.Frame.__init__(self, master)

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(fig, master=self)

        self.canvas.get_tk_widget().pack(padx=5, fill="both", expand=1)

        self.figure = self.canvas.figure
        self.draw = self.canvas.draw
        self.draw()

        Navigation(self.canvas, self)

    def update_figure(self, data):
        self.axes.cla()
        for k, v in data.items():
            self.axes.plot(v[:, 0], v[:, 1])
        self.draw()


class FileView(tk.Toplevel):
    def __init__(self, root, filename, *args, **kwargs):
        """ Display the first 20 and last 5 rows of a file in a Toplevel. """
        tk.Toplevel.__init__(self, root, *args, **kwargs)
        self.resizable(False, False)
        self.filename = filename
        self.root = root
        self.title("Plo.Py")
        self.tk.call('wm', 'iconphoto', root._w,
                     tk.PhotoImage(data=_icon_base64))

        with open(filename) as file:
            lines = file.readlines()

        if len(lines) > 40:
            self.original = ("".join(lines[:21])
                             + "...\n"
                             + "".join(lines[-5:]).rstrip())
        else:
            self.original = "".join(lines).rstrip()

        self.string = tk.StringVar()
        self.string.set(self.original)

        ttk.Label(self, textvariable=self.string
                  ).pack(padx=10, pady=(10, 0))

        f = ttk.Frame(self)
        f.pack()

        self.toggle = ttk.Button(f, text="View Parsed",
                                 command=self.viewparsed)
        self.toggle.grid(row=0, column=0, padx=(_pad, 0), pady=_pad)

        ttk.Button(f, text="Close", command=self.destroy
                   ).grid(row=0, column=1, padx=_pad, pady=_pad)

    def viewparsed(self):
        data = self.root.data[self.filename]
        if len(data) > 40:
            self.string.set(str(data[:21])[:-1]
                            + "\n ...\n"
                            " "+str(data[-5:])[1:])
        else:
            self.string.set(str(data))

        self.toggle.config(text="View Original", command=self.vieworiginal)

    def vieworiginal(self):
        self.toggle.config(text="View Parsed", command=self.viewparsed)
        self.string.set(self.original)


class FrameOptions(ttk.Frame):
    def __init__(self, root, notebook, title, filename, defaultcolor,
                 *args, **kwargs):
        ttk.Frame.__init__(self, notebook, *args, **kwargs)
        self.root = root
        self.filename = filename
        self.defaultcolor = self.color = defaultcolor
        self.xcol = 0
        self.ycol = 1
        self.line = "-"
        self.marker = "o"

        self.label = tk.StringVar(value=title)
        ttk.Entry(self, width=47, textvariable=self.label
                  ).grid(row=0, column=0, columnspan=2, sticky="EW", padx=_pad)

        b = ttk.Button(self, text="View", command=self.showfile)
        b.grid(row=0, column=2, padx=(1, _pad), pady=_pad)
        if not filename:
            b.config(state="disabled")

        L = ttk.Label(self, text="Columns", style="W.TLabel")

        colf = ttk.LabelFrame(self, labelwidget=L, style="W.TFrame",
                              relief="groove")
        colf.grid(row=1, columnspan=3, sticky="EW", padx=_pad, ipady=(3))

        colnum = len(self.root.data[self.filename][0])
        columns = ["Column "+str(c) for c in range(1, 1+colnum)]

        ttk.Label(colf, style="W.TLabel",
                  text="Size: {}".format(self.root.data[self.filename].shape)
                  ).grid(row=0, column=0, padx=_pad)

        ttk.Label(colf, text="X:", style="W.TLabel"
                  ).grid(row=0, column=2, padx=(_pad, 0))
        self.xcolumn = tk.StringVar()
        ttk.OptionMenu(colf, self.xcolumn, columns[0], *columns,
                       style="W.TMenubutton"
                       ).grid(row=0, column=3)

        ttk.Label(colf, text="Y:", style="W.TLabel"
                  ).grid(row=0, column=4, padx=(2*_pad, 0))
        self.ycolumn = tk.StringVar()
        ttk.OptionMenu(colf, self.ycolumn,
                       columns[1] if colnum > 1 else columns[0], *columns,
                       style="W.TMenubutton").grid(row=0, column=5)

        colf.grid_columnconfigure(1, weight=1)
        colf.grid_columnconfigure(6, weight=2)

        self.lineformat = tk.StringVar(value="Line                         -")
        ttk.OptionMenu(self, self.lineformat, "Line                         -",
                       "Line                         -",
                       "Dashed line           --",
                       "Dot-Dash line        -.",
                       "Dotted line              :",
                       "No Line                    ",
                       style="W.TMenubutton"
                       ).grid(row=2, column=0, sticky="w")

        self.markerformat = tk.StringVar(value="Circle marker         o")
        ttk.OptionMenu(self, self.markerformat, "Circle marker         o",
                       "Circle marker          o",
                       "Triangle marker      ^",
                       "Square marker         s",
                       "Pentagon marker    p",
                       "Hexagon marker     h",
                       "Star marker              *",
                       "Plus marker             +",
                       "Point marker             .",
                       "Pixel marker              ,",
                       "No marker                  ",
                       style="W.TMenubutton"
                       ).grid(row=2, column=1, sticky="w")

        self.root.style.configure(self.defaultcolor+".TButton",
                                  background=self.defaultcolor)
        self.colorbutton = ttk.Button(self, style=self.defaultcolor+".TButton",
                                      text="Color", command=self.selectcolor)
        self.colorbutton.grid(row=2, column=2, padx=(1, _pad), pady=_pad)

        self.label.trace("w", self.update)
        self.markerformat.trace("w", self.updatemarker)
        self.lineformat.trace("w", self.updateline)
        self.xcolumn.trace("w", self.updatexcol)
        self.ycolumn.trace("w", self.updateycol)

        notebook.add(self, text=title, sticky="nesw")

    def showfile(self):
        FileView(self.root, self.filename)

    def selectcolor(self):
        color = askcolor(self.color, title="Select Color -")[1]
        if color is not None:
            self.root.style.configure(color+".TButton",
                                      background=color)
            self.colorbutton.config(style=color+".TButton")
            # add color to root
            self.color = color
            self.update()

    def update(self, *_):
        self.root.update()

    def updatexcol(self, *_):
        self.xcol = int(self.xcolumn.get().split()[-1]) - 1
        self.update()

    def updateycol(self, *_):
        self.ycol = int(self.ycolumn.get().split()[-1]) - 1
        self.update()

    def updatemarker(self, *_):
        f = self.markerformat.get()
        self.marker = "" if "No" in f else f.split()[-1]
        self.update()

    def updateline(self, *_):
        f = self.lineformat.get()
        self.line = "" if "No" in f else f.split()[-1]
        self.update()

    def destroy(self):
        ttk.Frame.destroy(self)
        self.update()


class Window(tk.Tk):
    def __init__(self, files=[], data={}, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Plo.Py")

        self.tk.call('wm', 'iconphoto', self._w,
                     tk.PhotoImage(data=_icon_base64))

        self.style = ttk.Style(self)
        self.style.configure("W.TLabel", background='#ffffff')
        self.style.configure("W.TFrame", background='#ffffff')
        self.style.configure("W.TCheckbutton", background='#ffffff')
        self.style.configure("W.TMenubutton", background='#ffffff')

        # default colors for plots
        self.defcolors = plt.rcParams['axes.prop_cycle'].by_key()['color']
        self.defcolorindex = -1

        self.data = {"": np.array([[0, 0], [1, 1]])}

        menu = tk.Menu(self)
        # File
        m = tk.Menu(menu, tearoff=0)
        m.add_command(label="Open", command=self.selectfile, underline=0)
        m.add_command(label="Reload", command=self.reloadfiles, underline=0)
        m.add_command(label="Save", command=self.savefile, underline=0)
        menu.add_cascade(label="File", menu=m)

        # Format
        self.minorticks = tk.BooleanVar()
        self.showgrid = tk.BooleanVar()
        self.aspectratio = tk.StringVar(value="auto")
        self.lockaxeslimits = tk.BooleanVar()
        self.doautoupdate = tk.BooleanVar()
        self.doautoupdate.set(True)
        m = tk.Menu(menu, tearoff=0)
        m.add_checkbutton(label="Minorticks",
                          command=self.update, variable=self.minorticks)
        m.add_checkbutton(label="Grid",
                          command=self.update, variable=self.showgrid)
        m.add_checkbutton(label="Equal Aspect Ratio",
                          onvalue="equal", offvalue="auto",
                          command=self.update, variable=self.aspectratio)
        m.add_separator()
        m.add_checkbutton(label="Lock Axes Limits",
                          command=self.update, variable=self.lockaxeslimits)
        m.add_checkbutton(label="Auto-Update Graph",
                          command=self.update, variable=self.doautoupdate)
        menu.add_cascade(label="Format", menu=m)

        self.config(menu=menu)

        self.canvas = MplCanvas(self)
        self.canvas.grid(row=1, column=0, sticky="nsew", padx=5, rowspan=2)

        self.grid_columnconfigure(0, weight=1, minsize=300)
        self.grid_rowconfigure(2, weight=1, minsize=300)

        self.titlevar = tk.StringVar()
        e = ttk.Entry(self, textvariable=self.titlevar, width=40,
                      justify="center")
        e.grid(row=0, column=0, padx=50, pady=(5, 0))
        ToolTip(e, "Plot Title")
        self.titlevar.trace("w", self.settitle)

        flabel = ttk.Frame(self)
        flabel.grid(row=3, column=0, sticky="ew")
        flabel.grid_columnconfigure(1, weight=1)

        self.ylabel = tk.StringVar()
        e = ttk.Entry(flabel, textvariable=self.ylabel, width=20)
        e.grid(row=0, column=0, padx=(5, 0))
        ToolTip(e, "Y Axis Label")
        self.ylabel.trace("w", self.setylabel)
        self.xlabel = tk.StringVar()
        e = ttk.Entry(flabel, textvariable=self.xlabel, width=20)
        e.grid(row=0, column=1, pady=_pad)
        ToolTip(e, "X Axis Label")
        self.xlabel.trace("w", self.setxlabel)

        ttk.Frame(flabel, height=15, width=120
                  ).grid(row=0, column=2, fill=None)

        ttk.Button(self, text="Add File", command=self.selectfile
                   ).grid(row=0, column=1)

        b = ttk.Button(self, text="Save", command=self.savefile)
        b.grid(row=3, column=1)
        ToolTip(b, "Save Plot as Image")

        self.notebook = CustomNotebook(self)
        self.notebook.grid(row=1, column=1, sticky="n")

        # add a fake disabled tab to ensure proper sizing
#        self.fakeframeoptions = FrameOptions(self, self.notebook, "", "",
#                                             "#000000")
#        self.fakeframeoptions.line = ""  # prevent fake frame from showing
#        self.fakeframeoptions.marker = ""
#        self.notebook.add(self.fakeframeoptions,
#                          text="", sticky="nesw")
#        self.notebook.tab(0, state="disabled")

        self.bind("<Control-s>", self.savefile)
        self.bind("<Control-o>", self.selectfile)

        self.addfiles(files)
        for name, array in data.items():
            self.adddata(name, array)

    def adddata(self, name, array):
        self.data[name] = array
        FrameOptions(self, self.notebook, name, None, self.getdefcolor(),
                     style="W.TFrame")

    def selectfile(self, *_):
        filenames = askopenfilenames(title="Plo.Py - Add Files",
                                     filetypes=[('Data files', '.txt'),
                                                ('Data files', '.dat'),
                                                ('Data files', '.csv'),
                                                ('All Files', '*')])
        self.addfiles(filenames)

    def addfiles(self, filenames):
        for filename in filenames:
            filecontent = loadFile(filename)
            if len(filecontent.shape) != 2:
                print("Could not parse", basename(filename))
                self.bell()
                continue
            self.data[filename] = filecontent
            FrameOptions(self, self.notebook, basename(filename), filename,
                         self.getdefcolor(), style="W.TFrame")

        if filenames:
            if not self.titlevar.get():
                self.titlevar.set(basename(filenames[0]))
            self.update()

    def update(self):
        if self.doautoupdate.get():
            xlim = self.canvas.axes.set_xlim()
            ylim = self.canvas.axes.set_ylim()
            self.canvas.axes.cla()
            for frame in self.notebook.winfo_children():
                data = self.data[frame.filename]
                self.canvas.axes.plot(data[:, frame.xcol],
                                      data[:, frame.ycol],
                                      marker=frame.marker,
                                      linestyle=frame.line,
                                      color=frame.color,
                                      label=frame.label.get())
            self.canvas.axes.set_xlabel(self.xlabel.get())
            self.canvas.axes.set_ylabel(self.ylabel.get())
            handles, labels = self.canvas.axes.get_legend_handles_labels()
            if labels:
                self.canvas.axes.legend(handles, labels)
            if self.minorticks.get():
                self.canvas.axes.minorticks_on()
            if self.lockaxeslimits.get():
                self.canvas.axes.set_xlim(xlim)
                self.canvas.axes.set_ylim(ylim)
            self.canvas.axes.grid(self.showgrid.get())
            self.canvas.axes.set_aspect(self.aspectratio.get())

            self.canvas.draw()

    def settitle(self, *_):
        self.canvas.figure.suptitle(self.titlevar.get())
        self.canvas.draw()

    def setxlabel(self, *_):
        self.canvas.axes.set_xlabel(self.xlabel.get())
        self.canvas.draw()

    def setylabel(self, *_):
        self.canvas.axes.set_ylabel(self.ylabel.get())
        self.canvas.draw()

    def reloadfiles(self, *_):
        for filename in self.data.keys():
            print(filename)
            if filename and isfile(filename):
                self.data[filename] = loadFile(filename)
        self.update()

    def savefile(self, *_):
        plttitle = self.canvas.figure._suptitle
        if plttitle and plttitle.get_text():
            plttitle = plttitle.get_text()
            if not plttitle.endswith(".png"):
                plttitle += ".png"
        else:
            plttitle = ""
        filename = asksaveasfilename(title="Plo.Py - Save Plot",
                                     initialfile=plttitle,
                                     filetypes=[('Portable Network Graphics',
                                                 '.png'),
                                                ('All Files', '*')])
        if filename:
            self.canvas.figure.savefig(filename)

    def getdefcolor(self):
        self.defcolorindex += 1
        return self.defcolors[self.defcolorindex % len(self.defcolors)]


_files_to_load = []
_data_to_load = {}
suppress_errors = False


def addFile(filename):
    """
    Add a file to be loaded. with at least 2 columns.
    A column can be chosen to be plotted against another column.

    Parameters
    ----------
    filename : The file to be loaded

    Returns
    -------
    success : bool
        True if successful, false otherwise. Errors may be printed.

    See Also
    --------
    addArray()
    """
    if isfile(filename):
        _files_to_load.append(filename)
        return True
    if not suppress_errors:
        print("[PloPy]: '{}' is not a file.".format(filename))
    return False


def addArray(array, name):
    """
    Add an array to be loaded with at least 2 columns.
    A column can be chosen to be plotted against another column.

    Parameters
    ----------
    array : np.array or list-like of float
        The data to be loaded.
    name : str
        The name to be used for the tab. Must be unique,
        or it will overwrite another array.

    Returns
    -------
    success : bool
        True if successful, false otherwise. Errors may be printed.

    See Also
    --------
    addFile()
    """
    try:
        array = np.array(array)
    except Exception:
        print("[PloPy]: Could not convert {} into numpy array".format(name))
        return False
    if array.shape == 2:
        _data_to_load[name] = array
        if not suppress_errors and name in _data_to_load:
            print("[PloPy]: Array {} updated because it was already loaded")
        return True
    if not suppress_errors:
        print("[PloPy]: Array must be 2D (of columns and rows).")
    return False


def start():
    global root
    map(addFile, argv[1:])

    try:
        from ctypes import windll
        windll.shell32.SetCurrentProcessExplicitAppUserModelID("plopy")
    except Exception:
        pass

    root = Window(_files_to_load, _data_to_load)
    # set sizes
    root.update()
    root.minsize(root.winfo_width()-100, root.winfo_height()-10)
    exit(root.mainloop())


if __name__ == "__main__":
    start()
