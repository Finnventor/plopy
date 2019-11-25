plopy
=====
A program for making high-quality data plotting with matplotlib easily
customizable with a GUI.

Installation
------------
After installing `Python 3
<https://python.org/downloads/>`_, run ``pip install plopy``

You can also download the `standalone version
<https://raw.githubusercontent.com/Finnventor/plopy/master/__init__.py>`_,
but this is not recommended.

Usage
-----
To open the GUI, run the command ``python -m plopy``. If desired,
preselect files by appending their paths to the command
(``python -m plopy data.csv log.txt``... ).

plopy can also be controlled from a script.
Use ``plopy.add_file(filename)`` and ``plopy.add_array(array, name)``,
then call ``plopy.start()``

If you're already accustomed to matplotlib, or want to convert pre-existing
programs, you can use ``plopy.fig`` and ``plopy.ax`` to plot on, and call
``plopy.start()`` when done. This method also works in combination with the
previous one.
