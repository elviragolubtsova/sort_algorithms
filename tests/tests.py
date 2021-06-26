import unittest
from sort_algorithms.sort_algorithms import SortAlgorithms

data = [2, -6, 8.05, 65, 78, 2, -98]


class TestSortAlgotithms(unittest.TestCase):

    def test_bubble(self):
        for i in data:
            self.assertEqual(type(SortAlgorithms.bubble(i)), int)
    def test_insertation(self):
        for i in data:
            self.assertEqual(type(SortAlgorithms.insertation(i)), int)
    def test_pyramid(self):
        for i in data:
            self.assertEqual(type(SortAlgorithms.pyramid(i)), int)
    def test_quick(self):
        for i in data:
            self.assertEqual(type(SortAlgorithms.quick(i)), int)
    def test_selection(self):
        for i in data:
            self.assertEqual(type(SortAlgorithms.selection(i)), int)
    def test_shell(self):
        for i in data:
            self.assertEqual(type(SortAlgorithms.shell(i)), int)
