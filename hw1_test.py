import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        input = "super"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected,result)

    def test_vowel_count_2(self):
        input = "DUPER o"
        result = hw1.vowel_count(input)
        expected = 3
        self.assertEqual(expected,result)


    # Part 2
    def test_short_list_1(self):
        input = [[4, 6], [4], [3, 4, 5], [5, 2]]
        result = hw1.short_lists(input)
        expected = [[4,6],[5,2]]
        self.assertEqual(expected, result)

    def test_short_list_2(self):
        input = [[], [3, 4, 5], [5, 2]]
        result = hw1.short_lists(input)
        expected = [[5,2]]
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs_1(self):
        input = [[1,2],[10,9]]
        result = hw1.ascending_pairs(input)
        expected = [[1,2],[9,10]]
        self.assertEqual(expected,result)

    def test_ascending_pairs_2(self):
        input = [[10,9],[3,3],[11,7,6]]
        result = hw1.ascending_pairs(input)
        expected = [[9,10],[3,3],[11,7,6]]
        self.assertEqual(expected,result)


    # Part 4


    # Part 5


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()
