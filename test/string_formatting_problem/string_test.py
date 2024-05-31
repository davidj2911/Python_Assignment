import unittest
from src.string_formatting_problem.utils import string_format


class MyTestCase(unittest.TestCase):
    def test_case(self):

        actual_output = string_format(5)

        expected_out = ('1     1     1     1\n'
                        '2     2     2    10\n'
                        '3     3     3    11\n'
                        '4     4     4   100\n'
                        '5     5     5   101')

        self.assertEqual(actual_output, expected_out)  # add assertion here


if __name__ == '__main__':
    unittest.main()
