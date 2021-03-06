import unittest
from quadtree.quadtree import QuadTree, Point

class TestBasicFunctionality(unittest.TestCase):
  def setUp(self):
    self.qt = QuadTree()
    self.points = []
    for x in range(100):
      for y in range(100):
        self.points.append(Point(x, y, 100 * x + y))


  def test_is_inside(self):
    self.assertTrue(self.qt.is_inside(Point(0, 0, "123")))

  def test_quadtree_type(self):
    self.assertEqual(type(self.qt), QuadTree)

  def test_point_type(self):
    self.assertEqual(type(self.points[0]), Point)

  def test_add_point(self):
    qt = QuadTree()
    qt.add_point(Point(20, 20, ''))
    self.assertEqual(len(qt.points), 1)
    
  def test_add_points(self):
    qt = QuadTree()
    qt.add_point(Point(20, 20, ''))
    qt.add_point(Point(20, -20, ''))
    qt.add_point(Point(-20, 20, ''))
    self.assertEqual(len(qt.points), 3)

  def test_split(self):
    qt = QuadTree()
    for p in self.points:
      qt.add_point(p)

    self.assertEqual(type(qt.northWest), QuadTree)
    self.assertEqual(type(qt.northEast), QuadTree)
    self.assertEqual(type(qt.southWest), QuadTree)
    self.assertEqual(type(qt.southEast), QuadTree)


if __name__ == '__main__':
  unittest.main()