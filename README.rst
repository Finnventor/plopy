plopy
=====
A program for making data plotting with matplotlib easily customizable in a GUI.

Features
--------

- Intelligent data file parsing

   - Automatically skips over headers (or any line that cannot be converted to ``float`` or ``datetime``)
   - Supports many date formats in input automatically using ``dateutil.parser``
   - Works with comma-separated and/or whitespace-separated input files

- Graph configuration: line style, color, points, legend

- Dialogs to create multiple axes and assign lines to them

- Supports all output formats supported by ``matplotlib``
  (``.png``, ``.jpg``, ``.pdf`` ... )

Installation
------------
After installing `Python 3
<https://python.org/downloads/>`_, run the command ``pip install plopy``

You can also `try it online
<https://repl.it/@Finnventor/import-plopy-demo?lite=true>`_ on repl.it,
but that loads slowly and is not recommended for normal use.

Usage
-----
To open the GUI, run the command ``python -m plopy``, or also
preselect files by appending their paths to the command
(``python -m plopy data.csv log.txt`` ... ).

``plopy`` can also be controlled from a script.
Use ``plopy.add_file`` and ``plopy.add_array``,
then call ``plopy.start()``

If you're already accustomed to matplotlib, or want to convert pre-existing
programs, you can import ``plopy.fig`` and ``plopy.ax`` to plot on, and call
``plopy.start()`` when done. This method also works in combination with the
previous one.

See `the docs <https://plopy.readthedocs.io/en/latest/scripting.html>`_ for more examples.
