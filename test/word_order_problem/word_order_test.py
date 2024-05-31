import unittest
from src.word_order_problem.utils import word_order


class MyTestCase(unittest.TestCase):
    def test_case(self):

        actual_output = word_order(5, ['hi', 'hello', 'hi',
                                       'welcome', 'thankyou'])

        expected_output = (4, [2, 1, 1, 1])
        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
