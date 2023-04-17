from unittest import TestCase, main
from Task18 import to_polish_entry


class SolutionTest(TestCase):
    def test1(self):
        self.assertEqual(to_polish_entry('1 - 5 ** 3 * 2'), ['1', '5', '3', '**', '2', '*', '-'])

    def test2(self):
        self.assertEqual(to_polish_entry('3 + 4 * 2 / 1 - 5 ** 2'),
                         ['3', '4', '2', '*', '1', '/', '+', '5', '2', '**', '-'])

    def test3(self):
        self.assertEqual(to_polish_entry('3 + 4 * 2 / ( 1 - 5 ) ** 2'),
                         ['3', '4', '2', '*', '1', '5', '-', '2', '**', '/', '+'])

    def test4(self):
        self.assertEqual(to_polish_entry('12 + 75 * 5 + ( 3 - 2 * 5 ) * 8 ** 2'),
                         ['12', '75', '5', '*', '+', '3', '2', '5', '*', '-', '8', '2', '**', '*', '+'])

    def test5(self):
        self.assertEqual(to_polish_entry('4 ** 5 ** 7'),
                         ['4', '5', '7', '**', '**'])


if __name__ == '__main__':
    main()
