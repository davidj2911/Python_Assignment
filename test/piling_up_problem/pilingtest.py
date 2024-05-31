import unittest
from src.piling_up_problem.utils import piling_up


class MyTestCase(unittest.TestCase):
    def test_case(self):

        actual_output = piling_up(1,[[4, 3, 2, 1, 3, 4]])

        expected_output = "Yes"
        self.assertEqual(actual_output, expected_output)  # add assertion here

    def test_case2(self):

        actual_output = piling_up(2,[[1,3,2]])

        expected_output = "No"
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
