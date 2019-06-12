# -*- coding: utf-8 -*-

from __future__ import print_function, division

import sys
from os.path import basename, isfile


from matplotlib import use
use("TkAgg")
import matplotlib as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

try:  # Python 3
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter.filedialog import askopenfilenames, asksaveasfilename
    from tkinter.colorchooser import askcolor
    from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk as Navigation
except ImportError:  # Python 2
    import Tkinter as tk
    import ttk
    from tkFileDialog import askopenfilenames, asksaveasfilename
    from tkColorChooser import askcolor
    from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg as Navigation


_pad = 5  # Default inter-widget padding
_icon_base64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAD1BMVEU9S8398wXFw8Xt6+39//2jZEuFAAAAU0lEQVQI103O0Q2AIAwEUD66gIkTqAOA1wEo3P4zKaUY+/VyueSajrh0sSvBNkDqgG17AOY4CwqA+026qWpzVK1RFvGEzLMM5Fkmhe2Hb2JhvfEAWLIaQGXGTJoAAAAASUVORK5CYII="

_root = None


def array_from_file(filename):
    """ Get a 2D numpy array of float from a file. """
    data = []
    try:
        with open(filename) as file:
            for line in file:
                line = line.replace(",", " ")
                row = []
                for num in line.split():
                    try:
                        row.append(float(num))
                    except ValueError:
                        break
                if len(row) > 1:
                    data.append(row)
        return np.array(data)
    except Exception:
        return np.array([])


class _ToolTip(object):
    """ A tooltip that appears when the mouse enters the associated widget. """
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

        widget.bind('<Enter>', self.showtip)
        widget.bind('<Leave>', self.hidetip)

    def showtip(self, *_):
        """ Show the tooltip (called on enter event) """
        if self.tipwindow or not self.text:
            return
        x, y, _, cy = self.widget.bbox("insert")
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
        """ Hide the tooltip (called on leave event) """
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


class _CustomNotebook(ttk.Notebook):
    """
    A ttk Notebook with close buttons on each tab, customized for showing
    FrameOptions. It automatically creates a hidden tab if no others exist
    to ensure the notebook keeps its size.
    Based on an example by @BrianOakley (boakley.github.io)
    """
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

        self._emptyframe = _FrameOptions(self._root(), self, "", "", "#000000")
        self._emptyframe.line = ""
        self._emptyframe.marker = ""
        self.tab(0, state="disabled")

    def add(self, widget, **kwargs):
        """Add a widget to the notebook."""
        ttk.Notebook.add(self, widget, **kwargs)
        if self._isempty and len(self.tabs()) > 1:
            self.hide(0)
            self._isempty = False

    def forget(self, index):
        """Remove a widget from the notebook."""
        if self.winfo_children()[index] is not self._emptyframe:
            ttk.Notebook.forget(self, index)
            self.winfo_children()[index].destroy()
            self._root().update()
        if not self.select():
            self._isempty = True
            self.add(self._emptyframe)
            self.tab(0, state="disabled")

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
        try:
            index = self.index("@%d,%d" % (event.x, event.y))
        except tk.TclError:
            return

        if "close" in element and self._active == index:
            self.forget(index)
            self.event_generate("<<NotebookTabClosed>>")

        self.state(["!pressed"])
        self._active = None

    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            tk.PhotoImage("img_close", data='''
                iVBORw0KGgoAAAANSUhEUgAAABIAAAASBAMAAACk4JNkAAAAGFBMVEUAAAAAAAA
                AAAAAAAAAAAAAAAAAAAAAAABWNxwqAAAAB3RSTlMAj4FweoeWafOgkAAAAC1JRE
                FUCNdjIAs4MLBAGMyFDOIGEKa4ailUlq1cAMpihLPElQoxdDgwMJFlOwCPLARt2
                xEilQAAAABJRU5ErkJggg=='''),
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
                AAElFTkSuQmCC'''),
            tk.PhotoImage("img_blank", data='')
        )

        style.element_create("close", "image", "img_close",
                             ("disabled", "img_blank"),
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


class _MplCanvas(ttk.Frame):
    """
    A matplotlib canvas for tkinter.
    Can be updated, but remember to call .draw()
    """
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


class _FileView(tk.Toplevel):
    """
    Display the first 20 and last 5 rows of a file,
    or their parsed version, in a Toplevel.
    """
    def __init__(self, root, filename, *args, **kwargs):
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
        """ Switch to showing the parsed version of the file (an array). """
        data = self.root.data[self.filename]
        if len(data) > 40:
            self.string.set(str(data[:21])[:-1]
                            + "\n ...\n"
                            " "+str(data[-5:])[1:])
        else:
            self.string.set(str(data))

        self.toggle.config(text="View Original", command=self.vieworiginal)

    def vieworiginal(self):
        """ Switch to showing the original raw version of the file. """
        self.toggle.config(text="View Parsed", command=self.viewparsed)
        self.string.set(self.original)


class _FrameOptions(ttk.Frame):
    """ A pane consisting of options for a specific line on the plot. """
    def __init__(self, root, notebook, title, filename, defaultcolor,
                 *args, **kwargs):
        ttk.Frame.__init__(self, notebook, *args, **kwargs)
        self.root = root
        self.title = title
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

        colf = ttk.LabelFrame(self, style="W.TFrame", relief="groove",
                              labelwidget=ttk.Label(self, text="Columns",
                                                    style="W.TLabel"))
        colf.grid(row=1, columnspan=3, sticky="EW", padx=_pad, ipady=(3))

        s = self.root.data[self.filename or self.title].shape

        columns = ["Column "+str(c) for c in range(1, 1 + s[1])]

        ttk.Label(colf, style="W.TLabel", text="Size: {}".format(s)
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
                       columns[1] if s[1] > 1 else columns[0], *columns,
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
        """
        Open a window showing both the raw and parsed version of the associated
        file. Should be disabled for datasets.
        """
        _FileView(self.root, self.filename)

    def selectcolor(self):
        """ Open a colorchooser dialog (for the color of the line) """
        color = askcolor(self.color, title="Select Color -")[1]
        if color is not None:
            self.root.style.configure(color+".TButton",
                                      background=color)
            self.colorbutton.config(style=color+".TButton")
            # add color to root
            self.color = color
            self.update()

    def update(self, *_):
        """ Update the graph. """
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
    """ The main plopy window. Use start() to open. """
    def __init__(self, files=None, data=None, *args, **kwargs):
        files = files or []
        data = data or {}
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
        m.add_command(label="Load Data", command=self.selectfile)
        m.add_command(label="Reload Data", command=self.reloadfiles)
        m.add_command(label="Save Image", command=self.savefile)
        menu.add_cascade(label="File", menu=m)

        # Format
        self.minorticks = tk.BooleanVar()
        self.showgrid = tk.BooleanVar()
        self.aspectratio = tk.StringVar(value="auto")
        self.xscale = tk.StringVar(value="linear")
        self.yscale = tk.StringVar(value="linear")
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
        m.add_checkbutton(label="Logarithmic X-Axis",
                          onvalue="log", offvalue="linear",
                          command=self.setxscale, variable=self.xscale)
        m.add_checkbutton(label="Logarithmic Y-Axis",
                          onvalue="log", offvalue="linear",
                          command=self.setyscale, variable=self.yscale)
        m.add_separator()
        m.add_checkbutton(label="Lock Axes Limits",
                          command=self.update, variable=self.lockaxeslimits)
        m.add_checkbutton(label="Auto-Update Graph",
                          command=self.update, variable=self.doautoupdate)
        menu.add_cascade(label="Format", menu=m)

        self.config(menu=menu)

        self.canvas = _MplCanvas(self)
        self.canvas.grid(row=1, column=0, sticky="nsew", padx=5, rowspan=2)

        self.grid_columnconfigure(0, weight=1, minsize=300)
        self.grid_rowconfigure(2, weight=1, minsize=300)

        self.titlevar = tk.StringVar()
        e = ttk.Entry(self, textvariable=self.titlevar, width=40,
                      justify="center")
        e.grid(row=0, column=0, padx=50, pady=(5, 0))
        _ToolTip(e, "Plot Title")
        self.titlevar.trace("w", self.settitle)

        flabel = ttk.Frame(self)
        flabel.grid(row=3, column=0, sticky="ew")
        flabel.grid_columnconfigure(1, weight=1)

        self.ylabel = tk.StringVar()
        e = ttk.Entry(flabel, textvariable=self.ylabel, width=20)
        e.grid(row=0, column=0, padx=(5, 0))
        _ToolTip(e, "Y Axis Label")
        self.ylabel.trace("w", self.setylabel)
        self.xlabel = tk.StringVar()
        e = ttk.Entry(flabel, textvariable=self.xlabel, width=20)
        e.grid(row=0, column=1, pady=_pad)
        _ToolTip(e, "X Axis Label")
        self.xlabel.trace("w", self.setxlabel)

        ttk.Frame(flabel, height=15, width=120
                  ).grid(row=0, column=2, fill=None)

        ttk.Button(self, text="Add File", command=self.selectfile
                   ).grid(row=0, column=1)

        b = ttk.Button(self, text="Save", command=self.savefile)
        b.grid(row=3, column=1)
        _ToolTip(b, "Save Plot as Image")

        self.notebook = _CustomNotebook(self)
        self.notebook.grid(row=1, column=1, sticky="n")

        self.bind("<Control-s>", self.savefile)
        self.bind("<Control-r>", self.reloadfiles)
        self.bind("<Control-o>", self.selectfile)

        self.after(1, lambda: self.load(files, data))

    def load(self, files, data):
        """ Load pre-selected files and data. """
        self.addfiles(files)
        for name, array in data.items():
            self.adddata(name, array)

    def adddata(self, name, array):
        """ Add an array to be plotted. """
        self.data[name] = array
        _FrameOptions(self, self.notebook, name, None, self.getdefcolor(),
                      style="W.TFrame")
        self.update()

    def selectfile(self, *_):
        """
        Open a file selection dialog, then send the output to .addfiles()
        """
        filenames = askopenfilenames(title="Plo.Py - Add Files",
                                     filetypes=[('Data files', '.txt'),
                                                ('Data files', '.dat'),
                                                ('Data files', '.csv'),
                                                ('All Files', '*')])
        self.addfiles(filenames)

    def addfiles(self, filenames):
        """ Add a file to be parsed and plotted. """
        for filename in filenames:
            filecontent = array_from_file(filename)
            if len(filecontent.shape) != 2:
                print("Could not parse", basename(filename))
                self.bell()
                continue
            self.data[filename] = filecontent
            _FrameOptions(self, self.notebook, basename(filename), filename,
                          self.getdefcolor(), style="W.TFrame")

        if filenames:
            if not self.titlevar.get():
                self.titlevar.set(basename(filenames[0]))
            self.update()

    def update(self, force=False):
        """ Update the _MplCanvas. """
        if force or self.doautoupdate.get():
            xlim = self.canvas.axes.set_xlim()
            ylim = self.canvas.axes.set_ylim()
            self.canvas.axes.cla()
            for frame in self.notebook.winfo_children():
                if not frame.title:
                    continue
                data = self.data[frame.filename or frame.title]
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
            self.canvas.axes.set_xscale(self.xscale.get())
            self.canvas.axes.set_yscale(self.yscale.get())

            self.canvas.draw()

    def settitle(self, *_):
        """ Update the graph's title. """
        self.canvas.figure.suptitle(self.titlevar.get())
        self.canvas.draw()

    def setxlabel(self, *_):
        """ Update the graph's x-axis label. """
        self.canvas.axes.set_xlabel(self.xlabel.get())
        self.canvas.draw()

    def setylabel(self, *_):
        """ Update the graph's y-axis label. """
        self.canvas.axes.set_ylabel(self.ylabel.get())
        self.canvas.draw()

    def setxscale(self, *_):
        """ Update the graph's x-axis scale. """
        self.canvas.axes.set_xscale(self.xscale.get())
        self.canvas.draw()

    def setyscale(self, *_):
        """ Update the graph's y-axis scale. """
        self.canvas.axes.set_yscale(self.yscale.get())
        self.canvas.draw()

    def reloadfiles(self, *_):
        """ Re-parse all loaded files, then update the graph. """
        for filename in self.data.keys():
            if filename and isfile(filename):
                self.data[filename] = array_from_file(filename)
        self.update()

    def savefile(self, *_):
        """ Save the plot as an image or other format. """
        plttitle = self.canvas.figure._suptitle
        filetypes = [(v, "."+k) for k, v in
                     self.canvas.canvas.get_supported_filetypes().items()]
        if plttitle and plttitle.get_text():
            plttitle = plttitle.get_text()
            if not plttitle.lower().endswith(".png"):
                plttitle += ".png"
        else:
            plttitle = ""
        filename = asksaveasfilename(title="Plo.Py - Save Plot",
                                     initialfile=plttitle,
                                     filetypes=[("All Files", "*")]+filetypes)
        if filename:
            self.canvas.figure.savefig(filename)

    def getdefcolor(self):
        """ Get a color from the default matplotlib cycler. """
        self.defcolorindex += 1
        return self.defcolors[self.defcolorindex % len(self.defcolors)]

    def destroy(self):
        self.doautoupdate.set(False)
        tk.Tk.destroy(self)


_files_to_load = []
_data_to_load = {}
suppress_errors = False


def add_file(filename):
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
    add_array() : Add a 2D array to be loaded
    suppress_errors: bool; whether to print errors from this function.
    """
    if isfile(filename):
        _files_to_load.append(filename)
        return True
    if not suppress_errors:
        print("[PloPy]: '{}' is not a file.".format(filename))
    return False


def add_array(array, name):
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
    add_file() : Add a file to be loaded.
    suppress_errors : bool; whether to print errors from this function.
    """
    try:
        array = np.array(array)
    except Exception:
        print("[PloPy]: Could not convert {} into numpy array".format(name))
        return False
    if len(array.shape) == 2:
        _data_to_load[name] = array
        if name in _data_to_load and not suppress_errors:
            print("[PloPy]: Array {} updated (it was already loaded)."
                  .format(name))
        return True
    if not suppress_errors:
        print("[PloPy]: Array must be 2D (of columns and rows).")
    return False


def start():
    """
    Open the GUI. Note that this function should always be called last;
    the program exits after this.
    """
    global _root

    for file in sys.argv[1:]:
        add_file(file)

    try:
        from ctypes import windll
        windll.shell32.SetCurrentProcessExplicitAppUserModelID("plopy")
    except Exception:
        pass

    _root = Window(_files_to_load, _data_to_load)
    # set sizes
    _root.update()
    _root.minsize(_root.winfo_width()-100, _root.winfo_height()-10)
    exit(_root.mainloop())


if __name__ == "__main__":
    start()
