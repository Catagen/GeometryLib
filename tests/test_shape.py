import unittest
from geometrylib.shape import Triangle

class TriangleTests(unittest.TestCase):


	def test_raise_valueerror(self):
		self.assertRaises(ValueError, Triangle, 2, 3, 10)
		self.assertRaises(ValueError, Triangle, 2, 3, -4)

	def test_rotations(self):
		t1 = Triangle(3, 4, 5)
		self.assertEqual(t1._rotations(), ((3, 4, 5), (4, 5, 3), (5, 3, 4)))

	def test_equal(self):
		t1 = Triangle(2, 3, 4)
		t2 = Triangle(2, 3, 4)
		t3 = Triangle(3, 4, 2)

		self.assertEqual(t1, t2)
		self.assertEqual(t1, t3)
		self.assertEqual(t2, t3)

	def test_equal(self):
		t1 = Triangle(2, 3, 4)
		t2 = Triangle(2, 3, 4)
		t3 = Triangle(3, 4, 2)
		t4 = Triangle(3, 2, 4)

		self.assertEqual(t1, t1)
		self.assertEqual(t1, t3)
		self.assertEqual(t2, t3)
		self.assertNotEqual(t1, t4)

	def test_is_similar(self):
		t = Triangle(4, 6, 7)
		self.assertTrue(t.is_similar(Triangle(8, 12, 14)))
		self.assertTrue(t.is_similar(Triangle(12, 14, 8)))
		self.assertFalse(t.is_similar(Triangle(8, 14, 12)))
		self.assertFalse(t.is_similar(Triangle(8, 12, 12)))

	def test_equilateral(self):
		t1 = Triangle(4, 6, 7)
		t2 = Triangle(6, 6, 6)
		self.assertFalse(t1.is_equilateral())
		self.assertTrue(t2.is_equilateral())

	def test_is_isosceles(self):
		t1 = Triangle(4, 6, 7) #false
		t2 = Triangle(6, 6, 5) #true
		t3 = Triangle(7, 4, 7) #true
		t4 = Triangle(4, 6, 6) #true

		self.assertFalse(t1.is_isosceles())
		self.assertTrue(t2.is_isosceles())
		self.assertTrue(t3.is_isosceles())
		self.assertTrue(t4.is_isosceles())

	def test_perimeter(self):
		t1 = Triangle(2, 3, 4)
		t2 = Triangle(3, 2, 4)
		t3 = Triangle(5, 5, 5)

		self.assertEqual(t1.perimeter(), t2.perimeter())
		self.assertNotEqual(t3.perimeter(), t2.perimeter())
		self.assertEqual(t1.perimeter(), 9)

	def test_area(self):
		t1 = Triangle(2, 3, 4)
		t2 = Triangle(2, 4, 3)
		t3 = Triangle(8, 9, 10)
		t4 = Triangle(3, 4, 5)

		self.assertEqual(t1.area(), t2.area())
		self.assertNotEqual(t3.area(), t1.area())
		self.assertEqual(t4.area(), 6)

	def test_scale(self):
		t1 = Triangle(2, 3, 4).scale(2)
		t2 = Triangle(4, 6, 8)
		t3 = Triangle(5, 6, 8)

		self.assertEqual(t1, t2)
		self.assertNotEqual(t1, t3)
