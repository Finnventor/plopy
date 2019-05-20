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


pad = 5
IMAGE_DATA = "R0lGODlhEAAQAPcAAD1Lzf3zBcXDxe3r7f3//Q"+"A"*1003+"CH5BAAAAAAALAAAAAAQABAABwhpAAUIHEiwoEACCAkMGJBwYcKDDRMqlAgxgMUAER8KQBjAIcaJGhd2FLmw5MKKEztOZEgAJUOMAFgCaLmRwMWPBGbOpMkRJMIBO2mSNLkw5smaGFkiDMrTps+cFGv+lKi06dSMCA1qJRgQADs="


def loadFile(filename):
    data = []
    try:
        with open(filename) as fileRead:
            for line in fileRead:
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
        """ Display the first 20 and last 5 rows of a file. """
        tk.Toplevel.__init__(self, root, *args, **kwargs)
        self.resizable(False, False)
        self.filename = filename
        self.root = root
        self.title("Plo.Py")
        self.tk.call('wm', 'iconphoto', root._w,
                     tk.PhotoImage(data=IMAGE_DATA))

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
        self.toggle.grid(row=0, column=0, padx=(pad, 0), pady=pad)

        ttk.Button(f, text="Close", command=self.destroy
                   ).grid(row=0, column=1, padx=pad, pady=pad)

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
                  ).grid(row=0, column=0, columnspan=2, sticky="EW", padx=pad)

        ttk.Button(self, text="View", command=self.showfile
                   ).grid(row=0, column=2, padx=(1, pad), pady=pad)

        L = ttk.Label(self, text="Columns", style="W.TLabel")

        colf = ttk.LabelFrame(self, labelwidget=L, style="W.TFrame",
                              relief="groove")
        colf.grid(row=1, columnspan=3, sticky="EW", padx=pad, ipady=(3))

        colnum = len(self.root.data[self.filename][0])
        columns = ["Column "+str(c) for c in range(1, 1+colnum)]

        ttk.Label(colf, text=str(self.root.data[self.filename].shape),
                  style="W.TLabel"
                  ).grid(row=0, column=0, padx=pad)

        ttk.Label(colf, text="X:", style="W.TLabel"
                  ).grid(row=0, column=2, padx=(pad, 0))
        self.xcolumn = tk.StringVar()
        ttk.OptionMenu(colf, self.xcolumn, columns[0], *columns,
                       style="W.TMenubutton").grid(row=0, column=3)

        ttk.Label(colf, text="Y:", style="W.TLabel"
                  ).grid(row=0, column=4, padx=(2*pad, 0))
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
        self.colorbutton.grid(row=2, column=2, padx=(1, pad), pady=pad)

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


class Window(tk.Tk):
    def __init__(self, files, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Plo.Py")

        self.tk.call('wm', 'iconphoto', self._w,
                     tk.PhotoImage(data=IMAGE_DATA))

        self.style = ttk.Style(self)
        self.style.configure("W.TLabel", background='#ffffff')
        self.style.configure("W.TFrame", background='#ffffff')
        self.style.configure("W.TCheckbutton", background='#ffffff')
        self.style.configure("W.TMenubutton", background='#ffffff')

        # default colors for plots
        self.defcolors = plt.rcParams['axes.prop_cycle'].by_key()['color']
        self.defcolorindex = 0

        self.data = {"": np.array([[0, 0], [1, 1]])}

        self.canvas = MplCanvas(self)
        self.canvas.grid(row=1, column=0, sticky="nsew", padx=5)

        self.grid_columnconfigure(0, weight=1, minsize=300)
        self.grid_rowconfigure(1, weight=1, minsize=300)

        self.titlevar = tk.StringVar()
        e = ttk.Entry(self, textvariable=self.titlevar, width=40,
                      justify="center")
        e.grid(row=0, column=0, padx=50, pady=(5, 0))
        ToolTip(e, "Plot Title")
        self.titlevar.trace("w", self.settitle)

        flabel = ttk.Frame(self)
        flabel.grid(row=2, column=0, sticky="ew")
        flabel.grid_columnconfigure(1, weight=1)

        self.ylabel = tk.StringVar()
        e = ttk.Entry(flabel, textvariable=self.ylabel, width=20)
        e.grid(row=0, column=0, padx=(5, 0))
        ToolTip(e, "Y Axis Label")
        self.ylabel.trace("w", self.setylabel)
        self.xlabel = tk.StringVar()
        e = ttk.Entry(flabel, textvariable=self.xlabel, width=20)
        e.grid(row=0, column=1, pady=pad)
        ToolTip(e, "X Axis Label")
        self.xlabel.trace("w", self.setxlabel)

        ttk.Frame(flabel, height=15, width=120
                  ).grid(row=0, column=2, fill=None)

        ttk.Button(self, text="Add File", command=self.selectfile
                   ).grid(row=0, column=1)

        b = ttk.Button(self, text="Save", command=self.savefile)
        b.grid(row=2, column=1)
        ToolTip(b, "Save Plot as Image")

        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=1, sticky="n")

        # add a fake disabled tab to ensure proper sizing
        self.fakeframeoptions = FrameOptions(self, self.notebook, "", "",
                                             "#000000")
        self.fakeframeoptions.line = ""  # prevent fake frame from showing
        self.fakeframeoptions.marker = ""
        self.notebook.add(self.fakeframeoptions,
                          text="", sticky="nesw")
        self.notebook.tab(0, state="disabled")

        self.bind("<Control-s>", self.savefile)

        self.addfiles(files)

    def selectfile(self):
        filenames = askopenfilenames(title="Plo.Py - Add Files",
                                     filetypes=[('Text files', '.txt'),
                                                ('Text files', '.dat'),
                                                ('Text files', '.csv'),
                                                ('All Files', '*')])
        self.addfiles(filenames)

    def addfiles(self, filenames):
        for filename in filenames:
            if filename not in self.data.keys():
                filecontent = loadFile(filename)
                if len(filecontent.shape) != 2:
                    print("Could not parse", basename(filename))
                    self.bell()
                    continue
                self.data[filename] = filecontent
                FrameOptions(self, self.notebook, basename(filename), filename,
                             self.defcolors[self.defcolorindex],
                             style="W.TFrame")
                self.defcolorindex += 1
                if self.defcolorindex >= len(self.defcolors):
                    self.defcolorindex = 0

        if filenames:
            # remove the fake frame if it and others exist
            if self.fakeframeoptions and len(self.data) > 1:
                self.fakeframeoptions.destroy()
                self.fakeframeoptions = None
                del self.data[""]
            if not self.titlevar.get():
                self.titlevar.set(basename(filenames[0]))
            self.update()

    def update(self):
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


if __name__ == "__main__":
    files = []
    for filename in argv[1:]:
        if isfile(filename):
            files.append(filename)
        else:
            print("'"+filename+"' is not a file.")

    try:
        from ctypes import windll
        windll.shell32.SetCurrentProcessExplicitAppUserModelID("plopy")
    except Exception:
        pass

    root = Window(files)

    # set sizes
    root.update()
    root.minsize(root.winfo_width()-100, root.winfo_height()-10)
    exit(root.mainloop())
