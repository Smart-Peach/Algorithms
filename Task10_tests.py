from unittest import TestCase, main
from Task10 import merge_sort
from Task10 import lsd_radix_sort


class SolutionTest(TestCase):
    def test1(self):
        self.assertEqual(lsd_radix_sort(['za', 'yd', 'zb']), merge_sort(['za', 'yd', 'zb']))

    def test2(self):
        self.assertEqual(lsd_radix_sort([]), merge_sort([]))

    def test3(self):
        self.assertEqual(lsd_radix_sort(['abcdew', 'thsyfg', 'wirtyr', 'jsyrhs', 'sdfghj']),
                         merge_sort(['abcdew', 'thsyfg', 'wirtyr', 'jsyrhs', 'sdfghj']))

    def test4(self):
        self.assertEqual(lsd_radix_sort(['qwertyu', 'asdfghj', 'zxcvbnm', 'fghdtry', 'poiuytr', 'asdfghj']),
                         merge_sort(['qwertyu', 'asdfghj', 'zxcvbnm', 'fghdtry', 'poiuytr', 'asdfghj']))

    def test5(self):
        self.assertEqual(lsd_radix_sort(['ab', 'ac', 'as', 'al', 'op']), merge_sort(['ab', 'ac', 'as', 'al', 'op']))

    def test6(self):
        self.assertEqual(lsd_radix_sort(['abc', 'acb', 'bca', 'bac', 'cab', 'cba']),
                         merge_sort(['abc', 'acb', 'bca', 'bac', 'cab', 'cba']))

    def test7(self):
        self.assertEqual(lsd_radix_sort(['123sb&4', '56sd^3*', 'sjd7#&(']),
                         merge_sort(['123sb&4', '56sd^3*', 'sjd7#&(']))

    def test8(self):
        self.assertEqual(lsd_radix_sort(['654', '123', '987', '456', '234']),
                         merge_sort(['654', '123', '987', '456', '234']))

    def test9(self):
        self.assertEqual(lsd_radix_sort(['!@#^%', ')($%^', '^%$#&', '!$#%^', '@&^%*']),
                         merge_sort(['!@#^%', ')($%^', '^%$#&', '!$#%^', '@&^%*']))

    def test10(self):
        self.assertEqual(lsd_radix_sort(['ghfurjdkgl', 'dhtyvnfidy', 'asdfghjkl;']),
                         merge_sort(['ghfurjdkgl', 'dhtyvnfidy', 'asdfghjkl;']))


if __name__ == '__main__':
    main()
