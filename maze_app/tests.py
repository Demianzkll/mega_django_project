from django.test import TestCase
from .maze import Maze

# Create your tests here.


class MazeTestCase(TestCase):
    # def setUp(self):
       
    def test_maze(self):
        m = Maze(4)
        m.generate()
        self.assertEqual(m.get_neighbours((0,0)), [(0,1)])
        self.assertEqual(set(m.get_neighbours((0,3))), set([(0,2), (1,3)]))
        self.assertEqual(set(m.get_neighbours((3,3))), set([(3,2)]))
        self.assertEqual(set(m.get_neighbours((3,0))), set([(2,0), (3,1)]))