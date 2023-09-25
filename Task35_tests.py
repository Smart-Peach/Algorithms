from unittest import TestCase, main
from Task35 import make_plan


class MakePlanTest(TestCase):
    def test1(self):
        self.assertEqual(([3, 1, 4, 2, 5], 20), make_plan([[1, 3, 25], [2, 4, 10], [3, 1, 30], [4, 3, 50], [5, 3, 20]]))

    def test2(self):
        self.assertEqual((['B', 'F', 'E', 'D', 'A', 'C'], 40),
                         make_plan(
                             [['A', 5, 60], ['B', 1, 10], ['C', 1, 10], ['D', 1, 10], ['E', 1, 10], ['F', 1, 10]]))

    def test3(self):
        self.assertEqual((['E', 'C', 'B', 'D', 'A'], 0),
                         make_plan([['A', 5, 45], ['B', 5, 20], ['C', 5, 10], ['D', 5, 30], ['E', 5, 10]]))

    def test4(self):
        self.assertEqual((['A', 'B', 'C'], 0), make_plan([['A', 1, 20], ['B', 2, 30], ['C', 3, 40]]))

    def test5(self):
        self.assertEqual((['A', 'E', 'D', 'C', 'B'], 40),
                         make_plan([['A', 1, 10], ['B', 1, 10], ['C', 1, 10], ['D', 1, 10], ['E', 1, 10]]))


if __name__ == '__main__':
    main()
