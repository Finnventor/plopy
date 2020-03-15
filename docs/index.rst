plopy
=====
A program for making data plotting with matplotlib easily customizable in a GUI.

Features
--------

- Intelligent data file parsing
- Support for dates in input using ``dateutil.parser``
- Graph configuration: line style, color, points
- Custom axes scale and tick locations
- Supports all output formats supported by ``matplotlib``
  (``.png``, ``.jpg``, ``.pdf`` ... )

Installation
------------
After installing `Python 3
<https://python.org/downloads/>`_, run the command ``pip install plopy``

Another option is downloading the `standalone version
<https://raw.githubusercontent.com/Finnventor/plopy/master/__init__.py>`_,
but this is not recommended.

You can also `try it online
<https://repl.it/@Finnventor/import-plopy-demo?lite=true>`_ on repl.it
(this may load slowly, though).

Usage
-----
To open the GUI, run the command ``python -m plopy``. If desired,
preselect files by appending their paths to the command
(``python -m plopy data.csv log.txt`` ... ).

plopy can also be controlled from a script.
Use ``plopy.add_file(filename)`` and ``plopy.add_array(array, name)``,
then call ``plopy.start()``

If you're already accustomed to matplotlib, or want to convert pre-existing
programs, you can use ``plopy.fig`` and ``plopy.ax`` to plot on, and call
``plopy.start()`` when done. This method also works in combination with the
previous one.

.. toctree::
   :hidden:
   index
   :maxdepth: 2
   :glob:

   *
