Scripting
=========

>>> from plopy import add_file, add_array, start
>>> add_array([(0, 0), (1, 1), (2, 0)], "zigzag")
>>> add_file("test-data.txt")
>>> add_array([(0, 0), (1, 1), (2, 0), (3, -1), (4, 0)], "zigzag")
[PloPy]: Array zigzag updated (it was already loaded).
>>> start()


.. automodule:: __init__
   :members: add_array, add_file, start
