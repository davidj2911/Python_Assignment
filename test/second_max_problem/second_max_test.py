import unittest
from src.second_max_problem.utils import sec_max


class MyTestCase(unittest.TestCase):
    def test_case(self):

        actual_output = sec_max([13,24,55,6,34,55,76,89,22])

        expected_output = 76
        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
