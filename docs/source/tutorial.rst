Tutorial
========

  “There is no royal road to geometry.” — Euclid

This module makes triangle processing fun!
The beginner will enjoy how the :class:`geometrylib.utils` module
lets you get started quickly.

>>> from geometrylib import utils
>>> utils.is_isosceles(5, 5, 7)
True

But fancier programmers can use the Triangle
class to create an actual triangle object
upon which they can then perform lots of operations.
For example, consider this Python program:

.. testcode::

  from geometrylib.shape import Triangle
  t = Triangle(5, 5, 5)
  print ('Equilateral?', t.is_equilateral())
  print ('Isosceles?', t.is_isosceles())

Since methods :func:`~geometrylib.shape.Triangle.is_equilateral()`
return Boolean values, this program will produce the following output:

.. testoutput::

  Equilateral? True
  Isosceles? True

Read the `guide <guide.html>`_ to learn more!

.. warning::

  This module only handles three-sided polygons;
  five-sided figures are right out.
