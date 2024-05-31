import unittest
from src.min_max_problem.utils import min_max


class MyTestCase(unittest.TestCase):
    def test_case(self):

        actual_output = min_max()

        expected_output = 3
        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
