Scripting
=========

>>> from plopy import add_file, add_array, start
>>> add_array([(0, 0), (1, 1), (2, 0)], "zigzag")
True
>>> add_file("test-data.txt")
True
>>> add_array([(0, 0), (1, 1), (2, 0), (3, -1), (4, 0)], "zigzag")
[PloPy]: Array zigzag updated (it was already loaded).
True
>>> add_file("nonexistent.csv")
[PloPy]: 'nonexistent.csv' is not a file.
False
>>> start()

.. image:: images/scripting.png
   :width: 600

.. automodule:: __init__
   :members: add_array, add_file, suppress_errors, start
