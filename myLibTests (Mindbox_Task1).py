import unittest
import math
from abc import ABC, abstractmethod
from area_calculation_module.myLib import Shape, Circle, Triangle, calculate_area

class Area_calculation_tests(unittest.TestCase):

  def test_invalid_circle_init(self):
    self.assertRaises(ValueError, Circle, -10)
    self.assertRaises(ValueError, Circle, 0)

  def test_invalid_triangle_init(self):
    self.assertRaises(ValueError, Triangle, 10, 5, 25)
    self.assertRaises(ValueError, Triangle, 3, -2, 2)
    self.assertRaises(ValueError, Triangle, -3, 2, -2)
    self.assertRaises(ValueError, Triangle, 0, 0, 0)



  def test_invalid_shape(self):
    with self.assertRaises(ValueError):
      calculate_area()
    with self.assertRaises(ValueError):
      calculate_area(1, 2)
    with self.assertRaises(ValueError):
      calculate_area(1, 2, 3, 4)

  def test_is_right_triangle(self):
    self.assertTrue(Triangle(5, 12, 13).is_right_triangle())
    self.assertTrue(Triangle(math.sqrt(25), 12, 13).is_right_triangle())
    self.assertFalse(Triangle(6, 8, 7).is_right_triangle())

  def test_circle(self):
    self.assertEqual(calculate_area(1), math.pi)
    self.assertAlmostEqual(calculate_area(2.5), 19.634954084936208, places=6)
    self.assertEqual(Circle(math.pi).area(), math.pi ** 3)
    self.assertEqual(Circle(10).area(), math.pi * 100)
    self.assertEqual(Circle(1).area(), math.pi)

  def test_triangle(self):
    self.assertEqual(Triangle(13, math.sqrt(25), 12).area(), 30)
    self.assertEqual(Triangle(6, 8, 10).area(), 24)
    self.assertAlmostEqual(calculate_area(3, 4, 5), 6, places=6)
    self.assertEqual(calculate_area(5, 12, 13), 30)
    self.assertAlmostEqual(Triangle(3, 4, 5).area(), 6, places=6)

  def test_child_class_with_abstract_method(self):
    class Child(Shape):
      @abstractmethod
      def hehe(self):
        pass

    with self.assertRaises(TypeError):
      child = Child()

    class Child2(Shape):
      def area(self):
        return "S"

    try:
      child2 = Child2()
    except TypeError:
      self.fail("Child2 class should not raise TypeError when implementing abstract method")

if __name__ == "__main__":
  unittest.main()

