# -*- coding: utf-8 -*-

from __future__ import print_function, division

import sys
from os.path import basename, isfile


from matplotlib import use
use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from matplotlib import ticker, dates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

try:  # Python 3
    import tkinter as tk
    from tkinter import ttk
    from tkinter.messagebox import askquestion
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
    """Get a 2D numpy array of float from a file."""
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
    """A tooltip that appears when the mouse enters the associated widget."""

    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

        widget.bind('<Enter>', self.showtip)
        widget.bind('<Leave>', self.hidetip)

    def showtip(self, *_):
        """Show the tooltip (called on enter event)."""
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
        """Hide the tooltip (called on leave event)."""
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

    def __init__(self, root, *args, **kwargs):
        self.root = root
        if not self.__initialized:
            self.__initialize_custom_style()
            self.__inititialized = True

        kwargs["style"] = "CustomNotebook"
        ttk.Notebook.__init__(self, *args, **kwargs)

        self._active = None
        self._emptyframe = None
        self.isempty = True

        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

        self._emptyframe = _LineOptions(self._root(), self, Line2D([], []),
                                        notitle=True)
        self.tab(0, state="disabled")

    def add(self, widget, **kwargs):
        """Add a widget to the notebook."""
        ttk.Notebook.add(self, widget, **kwargs)
        if self.isempty and len(self.tabs()) > 1:
            self.hide(0)
            self.isempty = False

    def forget(self, index):
        """Remove a widget from the notebook."""
        if self.nametowidget(self.tabs()[index]) is not self._emptyframe:
            self.nametowidget(self.tabs()[index]).destroy()
            self._root().update()
        if not self.select():
            self.isempty = True
            self.add(self._emptyframe)
            self.tab(0, state="disabled")

    def on_close_press(self, event):
        """Called when the button is pressed over the close button."""
        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index

    def on_close_release(self, event):
        """Called when the button is released over the close button."""
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
        style = self.root.style
        self.images = (
            tk.PhotoImage("img_close", master=self.root, data='''
                iVBORw0KGgoAAAANSUhEUgAAABIAAAASBAMAAACk4JNkAAAAGFBMVEUAAAAAAAA
                AAAAAAAAAAAAAAAAAAAAAAABWNxwqAAAAB3RSTlMAj4FweoeWafOgkAAAAC1JRE
                FUCNdjIAs4MLBAGMyFDOIGEKa4ailUlq1cAMpihLPElQoxdDgwMJFlOwCPLARt2
                xEilQAAAABJRU5ErkJggg=='''),
            tk.PhotoImage("img_closeactive", master=self.root, data='''
                iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAQAAAD8x0bcAAAA1UlEQVR4AZXSM0I
                GYBjA8d8et7BlHCDrCukUGUt2bbm27HOFK2TXZ//f6X0smZOvQ79+HfLFpdC1z7
                B3o1AkKtx5sqsUlNr15E6FMIrcu1crnNpfWVFIcO5di2KTAkwq1uzdOUCeD0cY8
                WkDbPg0jEMf8oAunxoElPPWfFoDDT51A2M+5QL2fQrEI9enMWDcp2zARoRRtk/j
                QE9EukWLAmb1PvVGFj4aU/hRqHBOfWiKGMGMYo0+nEYO80G1cKpFDhPlcddSHrv
                gm2QLjjyVAQORp5ImX1McV/+ToXN/AAAAAElFTkSuQmCC'''),
            tk.PhotoImage("img_closepressed", master=self.root, data='''
                iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAQAAAD8x0bcAAAAvUlEQVR4AZXSAeY
                CURDH8Q+wsFdo/9BN/kDFUhLSLeoM6Qh1hFA6QR2hbpJIlG0jg+VF+g7M/N68N2
                Pm+ZWWmYOzs4OZloTc1lPdsKetXIPMSS21kwzBKsTUVoK26i2sjcKrjOzCawPzu
                FWi9HBXoh/qHDh6h3HY8x/J0RdwU4dVhmCsEporcEmSho2ky6dyXd1P5RYRdpqN
                G4S6AP7i8Z1JOgKFYPl9mGSO39dCbpMseCOXUJjGV9mbKvzGC4+4qP/m7PJBAAA
                AAElFTkSuQmCC'''),
            tk.PhotoImage("img_blank", master=self.root, data='')
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

    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        self.canvas = FigureCanvasTkAgg(fig, master=self)

        self.canvas.get_tk_widget().pack(padx=5, fill="both", expand=1)

        self.draw = self.canvas.draw
        self.draw()

        Navigation(self.canvas, self)


class _ArrayView(tk.Toplevel):
    """Display the first 25 and last 5 rows of an array in a Toplevel."""
    def __init__(self, root, data, *args, **kwargs):
        tk.Toplevel.__init__(self, root, *args, **kwargs)
        self.resizable(False, False)
        self.root = root
        self.title("Plo.Py")
        self.tk.call('wm', 'iconphoto', root._w,
                     tk.PhotoImage(master=self, data=_icon_base64))

        self.string = tk.StringVar()
        if len(data) > 40:
            self.string.set(str(data[:24])[:-1]
                            + "\n ...\n"
                            " "+str(data[-5:])[1:])
        else:
            self.string.set(str(data))

        ttk.Label(self, textvariable=self.string
                  ).pack(padx=10, pady=(10, 0))

        self.f = ttk.Frame(self)
        self.f.pack()

        ttk.Button(self.f, text="Close", command=self.destroy
                   ).grid(row=0, column=1, padx=_pad, pady=_pad)


class _FileView(_ArrayView):
    """
    Display the first 20 and last 5 rows of a file,
    or their parsed version, in a Toplevel.
    """

    def __init__(self, root, data, filename, *args, **kwargs):
        _ArrayView.__init__(self, root, data, *args, **kwargs)

        self.toggle = ttk.Button(self.f, text="View Parsed",
                                 command=self.viewparsed)
        self.toggle.grid(row=0, column=0, padx=(_pad, 0), pady=_pad)

        self.data = self.string.get()

        with open(filename) as file:
            lines = file.readlines()

        if len(lines) > 40:
            self.original = ("".join(lines[:21])
                             + "...\n"
                             + "".join(lines[-5:]).rstrip())
        else:
            self.original = "".join(lines).rstrip()

        self.vieworiginal()

    def viewparsed(self):
        """Switch to showing the parsed version of the file (an array)."""
        self.string.set(self.data)
        self.toggle.config(text="View Original", command=self.vieworiginal)

    def vieworiginal(self):
        """Switch to showing the original raw version of the file."""
        self.toggle.config(text="View Parsed", command=self.viewparsed)
        self.string.set(self.original)


class AxesOptions(tk.Toplevel):
    """Options for configuring axes."""
    scales = {"Linear": "linear", "Logarithmic": "log"}
    locators = {"None": ticker.NullLocator, "Auto": ticker.AutoLocator,
                "Logarithmic": ticker.LogLocator, "Date": dates.AutoDateLocator}

    formatters = {"None": ticker.NullFormatter, "Auto": ticker.ScalarFormatter,
                  "Logarithmic": ticker.LogFormatter,
                  "Date": dates.AutoDateFormatter}

    mlocators = {"None": ticker.NullLocator, "Auto": ticker.AutoMinorLocator}
    def __init__(self, root, ax, *args, **kwargs):
        tk.Toplevel.__init__(self, root, *args, **kwargs)
        self.title("Plo.Py - Configure Axes")
        self.tk.call('wm', 'iconphoto', self._w,
                     tk.PhotoImage(master=self, data=_icon_base64))
        self.root = root
        self.ax = ax
        self.xscale = tk.StringVar(value=next((k for k, v in self.scales.items() if v == ax.xaxis.get_scale()), ""))
        self.yscale = tk.StringVar(value=next((k for k, v in self.scales.items() if v == ax.yaxis.get_scale()), ""))
        self.xlocator = tk.StringVar(value=next((k for k, v in self.locators.items() if v == type(ax.xaxis.get_major_locator())), ""))
        self.ylocator = tk.StringVar(value=next((k for k, v in self.locators.items() if v == type(ax.yaxis.get_major_locator())), ""))
        self.xformatter = tk.StringVar(value=next((k for k, v in self.formatters.items() if v == type(ax.xaxis.get_major_formatter())), ""))
        self.yformatter = tk.StringVar(value=next((k for k, v in self.formatters.items() if v == type(ax.yaxis.get_major_formatter())), ""))
        self.xmlocator = tk.StringVar(value=next((k for k, v in self.mlocators.items() if v == type(ax.xaxis.get_minor_locator())), ""))
        self.ymlocator = tk.StringVar(value=next((k for k, v in self.mlocators.items() if v == type(ax.yaxis.get_minor_locator())), ""))

        w = 15  # OptionMenu width

        # Scales
        f = ttk.LabelFrame(self, text="Scale")
        ttk.Label(f, text="X:").grid(row=0, column=0, sticky="nw", padx=(5, 1), pady=(2, 4))
        o = ttk.OptionMenu(f, self.xscale, self.xscale.get(),
                           *self.scales.keys())
        o.config(width=w)
        o.grid(row=0, column=1, sticky="new", padx=(0, 5), pady=(0, 5))
        ttk.Label(f, text="Y:").grid(row=0, column=2, sticky="nw", padx=(5, 1), pady=(2, 4))
        o = ttk.OptionMenu(f, self.yscale, self.yscale.get(),
                           *self.scales.keys())
        o.config(width=w)
        o.grid(row=0, column=3, sticky="new", padx=(0, 5), pady=(0, 5))
        f.columnconfigure(1, weight=1)
        f.columnconfigure(3, weight=1)
        f.rowconfigure(0, weight=1)
        f.grid(row=0, column=0, sticky="new", padx=7, pady=7)

        # Locators
        f = ttk.LabelFrame(self, text="Tick Locations")
        ttk.Label(f, text="X:").grid(row=0, column=0, sticky="nw", padx=(5, 1), pady=(2, 4))
        o = ttk.OptionMenu(f, self.xlocator, self.xlocator.get(),
                           *self.locators.keys())
        o.config(width=w)
        o.grid(row=0, column=1, sticky="new", padx=(0, 5), pady=(0, 5))
        ttk.Label(f, text="Y:").grid(row=0, column=2, sticky="nw", padx=(5, 1), pady=(2, 4))
        o = ttk.OptionMenu(f, self.ylocator, self.ylocator.get(),
                           *self.locators.keys())
        o.config(width=w)
        o.grid(row=0, column=3, sticky="new", padx=(0, 5), pady=(0, 5))
        f.columnconfigure(1, weight=1)
        f.columnconfigure(3, weight=1)
        f.rowconfigure(0, weight=1)
        f.grid(row=1, column=0, sticky="new", padx=7, pady=7)

        # Formatters
        f = ttk.LabelFrame(self, text="Tick Formats")
        ttk.Label(f, text="X:").grid(row=0, column=0, sticky="nw", padx=(5, 1), pady=(2, 4))
        o = ttk.OptionMenu(f, self.xformatter, self.xformatter.get(),
                           *self.formatters.keys())
        o.config(width=w)
        o.grid(row=0, column=1, sticky="new", padx=(0, 5), pady=(0, 5))
        ttk.Label(f, text="Y:").grid(row=0, column=2, sticky="nw", padx=(5, 1), pady=(2, 4))
        o = ttk.OptionMenu(f, self.yformatter, self.yformatter.get(),
                           *self.formatters.keys())
        o.config(width=w)
        o.grid(row=0, column=3, sticky="new", padx=(0, 5), pady=(0, 5))
        f.columnconfigure(1, weight=1)
        f.columnconfigure(3, weight=1)
        f.rowconfigure(0, weight=1)
        f.grid(row=2, column=0, sticky="new", padx=7, pady=7)

        # MinorLocators
        f = ttk.LabelFrame(self, text="Minor Tick Locations")
        ttk.Label(f, text="X:").grid(row=0, column=0, sticky="nw", padx=(5, 1), pady=(2, 4))
        o = ttk.OptionMenu(f, self.xmlocator, self.xmlocator.get(),
                           *self.mlocators.keys())
        o.config(width=w)
        o.grid(row=0, column=1, sticky="new", padx=(0, 5), pady=(0, 5))
        ttk.Label(f, text="Y:").grid(row=0, column=2, sticky="nw", padx=(5, 1), pady=(2, 4))
        o = ttk.OptionMenu(f, self.ymlocator, self.ymlocator.get(),
                           *self.mlocators.keys())
        o.config(width=w)
        o.grid(row=0, column=3, sticky="new", padx=(0, 5), pady=(0, 5))
        f.columnconfigure(1, weight=1)
        f.columnconfigure(3, weight=1)
        f.rowconfigure(0, weight=1)
        f.grid(row=3, column=0, sticky="new", padx=7, pady=7)

        # Apply, Ok, Cancel
        f2 = ttk.Frame(self)
        ttk.Button(f2, text="Apply", command=self.apply).grid(row=0, column=0, sticky="ne")
        ttk.Button(f2, text="Ok", command=self.ok).grid(row=0, column=1, sticky="ne")
        ttk.Button(f2, text="Cancel", command=self.destroy).grid(row=0, column=2, sticky="ne")
        f2.grid(row=4, column=0, sticky="se", padx=4, pady=4)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        for w in f2.winfo_children():
            w.grid_configure(padx=3, pady=3)

        self.focus_force()

    def apply(self):
        """Apply the edits, returning True if successful."""
        try:
            if self.xscale.get():
                self.ax.set_xscale(self.scales[self.xscale.get()])
            if self.yscale.get():
                self.ax.set_yscale(self.scales[self.yscale.get()])

            if self.xlocator.get():
                xl = self.locators[self.xlocator.get()]()
                self.ax.xaxis.set_major_locator(xl)
            if self.ylocator.get():
                yl = self.locators[self.ylocator.get()]()
                self.ax.yaxis.set_major_locator(yl)

            if issubclass(self.locators[self.xlocator.get()], dates.DateLocator):
                self.ax.xaxis.set_major_formatter(self.formatters[self.xformatter.get()](xl))
            elif self.xformatter.get():
                self.ax.xaxis.set_major_formatter(self.formatters[self.xformatter.get()]())
            if issubclass(self.locators[self.ylocator.get()], dates.DateLocator):
                self.ax.yaxis.set_major_formatter(self.formatters[self.yformatter.get()](yl))
            elif self.yformatter.get():
                self.ax.yaxis.set_major_formatter(self.formatters[self.yformatter.get()]())

            if self.xmlocator.get():
                self.ax.xaxis.set_minor_locator(self.mlocators[self.xmlocator.get()]())
            if self.ymlocator.get():
                self.ax.yaxis.set_minor_locator(self.mlocators[self.ymlocator.get()]())

            self.root.draw()
        except Exception:
            self.root.bell()
            raise
        return True

    def ok(self):
        if self.apply():
            self.destroy()


class _LineOptions(ttk.Frame):
    """A frame with options for a plotted line."""

    linetypes = {"-": "Line                         -",
                 "--": "Dashed line           --",
                 "-.": "Dot-Dash line        -.",
                 ":": "Dotted line              :",
                 "None": "No Line                    "}

    markertypes = {"o": "Circle marker          o",
                   "^": "Triangle marker      ^",
                   "s": "Square marker         s",
                   "p": "Pentagon marker    p",
                   "h": "Hexagon marker     h",
                   "*": "Star marker              *",
                   "+": "Plus marker             +",
                   ".": "Point marker             .",
                   ",": "Pixel marker              ,",
                   "None": "No marker                  "}

    def __init__(self, root, notebook, line, notitle=False, *args, **kwargs):
        ttk.Frame.__init__(self, notebook, *args, **kwargs, style="W.TFrame")
        self.root = root
        self.line = line

        self.label = tk.StringVar(value=self.line.get_label())
        ttk.Entry(self, width=47, textvariable=self.label
                  ).grid(row=0, column=0, columnspan=2, sticky="EW", padx=_pad)

        b = ttk.Button(self, text="View", command=self.show)
        b.grid(row=0, column=2, padx=(1, _pad), pady=_pad)

        self.lineformat = tk.StringVar(
            value=self.linetypes.get(self.line.get_ls(), "None"))
        ttk.OptionMenu(self, self.lineformat, self.lineformat.get(),
                       *self.linetypes.values(),
                       style="W.TMenubutton"
                       ).grid(row=2, column=0, sticky="w")

        self.markerformat = tk.StringVar(
            value=self.markertypes.get(self.line.get_marker(), "None"))
        ttk.OptionMenu(self, self.markerformat, self.markerformat.get(),
                       *self.markertypes.values(),
                       style="W.TMenubutton"
                       ).grid(row=2, column=1, sticky="w")

        self.root.style.configure(self.line.get_c()+".TButton",
                                  background=self.line.get_c())
        self.colorbutton = ttk.Button(self, style=self.line.get_c()+".TButton",
                                      text="Color", command=self.selectcolor)
        self.colorbutton.grid(row=2, column=2, padx=(1, _pad), pady=_pad)

        self.label.trace("w", self.updatelabel)
        self.markerformat.trace("w", self.updatemarker)
        self.lineformat.trace("w", self.updateline)

        notebook.add(self, text="" if notitle else self.line.get_label() or "Untitled",
                     sticky="nesw")

    def show(self):
        """Open an _ArrayView window showing the data."""
        _ArrayView(self.root, np.column_stack(self.line.get_data()))

    def selectcolor(self):
        """Open a colorchooser dialog (for the color of the line)."""
        color = askcolor(self.line.get_c(), title="Select Color - Plo.Py")[1]
        if color is not None:
            self.root.style.configure(color+".TButton",
                                      background=color)
            self.colorbutton.config(style=color+".TButton")
            # add color to root
            self.line.set_c(color)
            self.update()

    def update(self, *_):
        """Update the graph."""
        self.root.draw()

    def updatelabel(self, *_):
        """Called when the label entry is edited."""
        self.line.set_label(self.label.get())
        self.update()

    def updatemarker(self, *_):
        """Called when the selected marker is changed."""
        self.line.set_marker(self.markerformat.get()[-2].strip() +
                             self.markerformat.get()[-1])
        self.update()

    def updateline(self, *_):
        """Called when the selected linestyle is changed."""
        self.line.set_ls(self.lineformat.get()[-2].strip() +
                         self.lineformat.get()[-1])
        self.update()

    def destroy(self):
        ttk.Frame.destroy(self)
        if self.line in ax.lines:
            ax.lines.remove(self.line)
        self.update()


class _LineColumnOptions(_LineOptions):
    """A frame with options for a plotted line with column selection."""
    def __init__(self, root, notebook, line, data):
        self.data = data
        _LineOptions.__init__(self, root, notebook, line)

        colf = ttk.LabelFrame(self, style="W.TFrame", relief="groove",
                              labelwidget=ttk.Label(self, text="Columns",
                                                    style="W.TLabel"))
        colf.grid(row=1, columnspan=3, sticky="EW", padx=_pad, ipady=(3))

        columns = [str(i) for i in range(1, 1 + self.data.shape[1])]

        ttk.Label(colf, style="W.TLabel", text="Size: {}".format(self.data.shape)
                  ).grid(row=0, column=0, padx=_pad)

        ttk.Label(colf, text="X: Column", style="W.TLabel"
                  ).grid(row=0, column=2, padx=(_pad, 0))
        self.xcolumn = tk.StringVar()
        ttk.OptionMenu(colf, self.xcolumn, "1", *columns,
                       style="W.TMenubutton"
                       ).grid(row=0, column=3)

        ttk.Label(colf, text="Y: Column", style="W.TLabel"
                  ).grid(row=0, column=4, padx=(2*_pad, 0))
        self.ycolumn = tk.StringVar()
        ttk.OptionMenu(colf, self.ycolumn, "2", *columns,
                       style="W.TMenubutton").grid(row=0, column=5)

        self.xcolumn.trace("w", self.updatexcolumn)
        self.ycolumn.trace("w", self.updateycolumn)

        colf.grid_columnconfigure(1, weight=1)
        colf.grid_columnconfigure(6, weight=2)

    def updatexcolumn(self, *_):
        self.line.set_xdata(self.data[:, int(self.xcolumn.get())-1])
        self.root.update()

    def updateycolumn(self, *_):
        self.line.set_ydata(self.data[:, int(self.ycolumn.get())-1])
        self.root.update()

    def show(self):
        """Open an _ArrayView window showing the data."""
        _ArrayView(self.root, self.data)


class _LineFileOptions(_LineColumnOptions):
    """
    A frame with options for a plotted line with column selection
    and file viewing.
    """

    def __init__(self, root, notebook, line, data, filename, *args, **kwargs):
        _LineColumnOptions.__init__(self, root, notebook, line, data,
                                    *args, **kwargs)
        self.filename = filename

    def show(self):
        """Open an _FileView window showing the parsed and unparsed data."""
        _FileView(self.root, self.data, self.filename)


class Window(tk.Tk):
    """The main plopy window. Use start() to open."""

    def __init__(self, *args, **kwargs):
        self.isedited = False
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Plo.Py")

        self.tk.call('wm', 'iconphoto', self._w,
                     tk.PhotoImage(master=self, data=_icon_base64))

        self.style = ttk.Style()
        self.style.configure("W.TLabel", background='#ffffff')
        self.style.configure("W.TFrame", background='#ffffff')
        self.style.configure("W.TCheckbutton", background='#ffffff')
        self.style.configure("W.TMenubutton", background='#ffffff')

        menu = tk.Menu(self)
        # File
        m = tk.Menu(menu, tearoff=0)
        m.add_command(label="Load Data", command=self.selectfile)
        m.add_command(label="Reload Data", command=self.reloadfiles)
        m.add_command(label="Save Image", command=self.savefile)
        menu.add_cascade(label="File", menu=m)

        # Format
        self.showgrid = tk.BooleanVar()
        self.aspectratio = tk.StringVar(value=ax.get_aspect())
        self.dorescale = tk.BooleanVar()
        m = tk.Menu(menu, tearoff=0)
        m.add_command(label="Configure Axes", command=lambda: AxesOptions(self, ax))
        m.add_checkbutton(label="Grid",
                          command=self.setgrid, variable=self.showgrid)
        m.add_checkbutton(label="Equal Aspect Ratio",
                          onvalue="equal", offvalue="auto",
                          command=self.setaspect, variable=self.aspectratio)
        m.add_separator()
        m.add_checkbutton(label="Auto-Rescale Axes",
                          command=self.draw, variable=self.dorescale)
        menu.add_cascade(label="Format", menu=m)

        self.config(menu=menu)

        self.canvas = _MplCanvas(self)
        self.canvas.grid(row=1, column=0, sticky="nsew", padx=5, rowspan=2)

        self.grid_columnconfigure(0, weight=1, minsize=300)
        self.grid_rowconfigure(2, weight=1, minsize=300)

        self.titlevar = tk.StringVar()
        if fig._suptitle:
            self.titlevar.set(fig._suptitle.get_text())
        e = ttk.Entry(self, textvariable=self.titlevar, width=40,
                      justify="center")
        e.grid(row=0, column=0, padx=50, pady=(5, 0))
        _ToolTip(e, "Plot Title")
        self.titlevar.trace("w", self.settitle)

        flabel = ttk.Frame(self)
        flabel.grid(row=3, column=0, sticky="ew")
        flabel.grid_columnconfigure(1, weight=1)

        self.ylabel = tk.StringVar(value=ax.get_ylabel())
        e = ttk.Entry(flabel, textvariable=self.ylabel, width=20)
        e.grid(row=0, column=0, padx=(5, 0))
        _ToolTip(e, "Y Axis Label")
        self.ylabel.trace("w", self.setylabel)
        self.xlabel = tk.StringVar(value=ax.get_xlabel())
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

        self.after_idle(self.load)

        self.dorescale.set(True)

    def load(self):
        """Load pre-selected files and data."""
        self.focus_force()
        for line in ax.lines:
            _LineOptions(self, self.notebook, line)

        self.addfiles(_files_to_load)
        for n, a in _data_to_load.items():
            self.adddata(a, n)

    def adddata(self, array, name):
        """Add an array to be plotted."""
        _LineColumnOptions(self, self.notebook,
                           ax.plot(array[:, 0], array[:, 1], label=name)[0],
                           array)
        self.update()

    def selectfile(self, *_):
        """Open a file selection dialog, then send the output to .addfiles()"""
        filenames = askopenfilenames(title="Plo.Py - Add Files",
                                     filetypes=[('Data files', '.txt'),
                                                ('Data files', '.dat'),
                                                ('Data files', '.csv'),
                                                ('All Files', '*')])
        self.addfiles(filenames)

    def addfiles(self, filenames):
        """Add a file to be parsed and plotted."""
        for filename in filenames:
            filecontent = array_from_file(filename)
            if len(filecontent.shape) != 2:
                print("Could not parse", basename(filename))
                self.bell()
                continue

            _LineFileOptions(
                self, self.notebook,
                ax.plot(filecontent[:, 0], filecontent[:, 1],
                        label=basename(filename))[0],
                filecontent, filename)

        if filenames:
            if not self.titlevar.get():
                self.titlevar.set(basename(filenames[0]))
            self.update()

    def update(self):
        """Update the _MplCanvas."""
        if self.dorescale.get():
            ax.relim()
            ax.autoscale()

        self.draw()

    def draw(self):
        """Redraw the _MplCanvas."""
        handles, labels = ax.get_legend_handles_labels()
        if labels:
            ax.legend(handles, labels)

        self.canvas.draw()
        self.isedited = True

    def settitle(self, *_):
        """Update the graph's title."""
        fig.suptitle(self.titlevar.get())
        self.draw()

    def setxlabel(self, *_):
        """Update the graph's x-axis label."""
        ax.set_xlabel(self.xlabel.get())
        self.draw()

    def setylabel(self, *_):
        """Update the graph's y-axis label."""
        ax.set_ylabel(self.ylabel.get())
        self.draw()

    def setaspect(self):
        """Update the graph's aspect ratio."""
        ax.set_aspect(self.aspectratio.get())
        self.draw()

    def setgrid(self):
        """Update the graph's grid."""
        ax.grid(self.showgrid.get())
        self.draw()

    def reloadfiles(self, *_):
        """Re-parse all loaded files, then update the graph."""
        for pane in self.notebook.winfo_children():
            if isinstance(pane, _LineFileOptions):
                pane.data = array_from_file(pane.filename)
                pane.updatexcolumn()
                pane.updateycolumn()

    def savefile(self, *_):
        """
        Save the plot as an image or other format.

        Returns whethere the plot was saved.
        """
        plttitle = fig._suptitle
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
            fig.savefig(filename)
            self.isedited = False
            return True
        return False

    def destroy(self):
        """Close the window. If plot was edited, show save/close dialog."""
        if self.isedited and not self.notebook.isempty:
            response = askquestion(title="Plo.Py",
                                   message="Save plot before closing?",
                                   type="yesnocancel")

            if response == "yes":
                if not self.savefile():
                    return
            elif response == "cancel":
                return

        tk.Tk.destroy(self)


fig = Figure()
ax = fig.add_subplot(111)


_files_to_load = []
_data_to_load = {}
suppress_errors = False


def add_file(filename):
    """
    Add a file to be loaded (with at least 2 columns).

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
    Add an array to be loaded (with at least 2 columns).

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
        if name in _data_to_load and not suppress_errors:
            print("[PloPy]: Array {} updated (it was already loaded)."
                  .format(name))
        _data_to_load[name] = array
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

    # differentiate this from python.exe by giving it a unique id
    # (gets icon to show up in taskbar on windows)
    try:
        from ctypes import windll
        from random import random
        windll.shell32.SetCurrentProcessExplicitAppUserModelID("plopy.{}".format(random()))
    except Exception:
        pass

    _root = Window()
    # set sizes
    _root.update()
    _root.minsize(_root.winfo_width()-100, _root.winfo_height()-10)
    exit(_root.mainloop())


if __name__ == "__main__":
    start()
