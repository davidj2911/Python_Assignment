import unittest
from src.linear_algebra_problem.utils import linear_alg


class MyTestCase(unittest.TestCase):
    def test_case(self):

        actual_output = linear_alg([[1 , 2.2], [2.3, 1]])

        expected_output = -4.06
        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
