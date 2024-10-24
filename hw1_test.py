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

    def test_add_prices_1(self):
        dollars = 20.00
        cents = 120
        result = hw1.add_prices(dollars,cents)
        expected = 21.20
        self.asserEqual(expected,result)

    def test_add_prices_2(self):
        dollars = 20.00
        cents = 60
        result = hw1.add_prices(dollars,cents)
        expected = 20.60
        self.assertEqual(expected,result)

    # Part 5

    def test_rectangle_area_1(self):
        top_left = [2,4]
        bottom_right = [5,3]
        result = hw1.rectangle_area(top_left,bottom_right)
        expected = 3
        self.assertEqual(expected,result)

    def test_rectangle_area_2(self):
        top_left = [3,5]
        bottom_right = [5,3]
        result = hw1.rectangle_area(top_left,bottom_right)
        expected = 4
        self.assertEqual(expected,result)


    # Part 6

    def test_books_by_author_1(self):
        book1 = data.Book(["Roald Dahl", "another author"],"Charlie & the Chocolate Factory")
        book2 = data.Book(["J.K. Rowling","diff author"], "Harry Potter & the Sorcerer's Stone")
        result = hw1.books_by_author("Roald Dahl",[book1,book2])
        expected = ["Charlie & the Chocolate Factory"]
        self.assertEqual(expected,result)

    def test_books_by_author_1(self):
        book1 = data.Book(["J.K. Rowling", "another author"],"Harry Potter & the Sorcerer's Stone")
        book2 = data.Book(["Roald Dahl","diff author"], "James & the Giant Peach")
        result = hw1.books_by_author("Roald Dahl",[book1,book2])
        expected = ["James & the Giant Peach"]
        self.assertEqual(expected,result)

    # Part 7

    def test_circle_bound_1(self):
        rect = data.Rectangle((0,6),(4,0))
        result = hw1.circle_bound(rect)
        expected = data.Circle((2,3),6.0)
        self.assertEqual(expected,result)

    # couldn't figure out the bug, so no second test

    # Part 8

    def test_below_pay_average_1(self):
        list = [
            data.Employee("Sally",18),
            data.Employee("Henry",15),
            data.Employee("Ron",20),
            data.Employee("Sarah",16),
            data.Employee("Missy",18),
            data.Employee("Will",19)]
        result = hw1.below_pay_average(list)
        expected = ["Henry","Sarah"]
        self.assertEqual(expected,result)


   # couldn't figure out the bug, so no second test

if __name__ == '__main__':
    unittest.main()
