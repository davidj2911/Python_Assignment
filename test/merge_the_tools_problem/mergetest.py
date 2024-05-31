import unittest
from src.merge_the_tools_problem.utils import merge_the_tools

class MyTestCase(unittest.TestCase):
    def test_case(self):

        actual_output = merge_the_tools("AABCXXADA",3)

        expected_output = "AB\nCX\nAD"

        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
