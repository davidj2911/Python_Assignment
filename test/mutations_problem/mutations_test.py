import unittest
from src.mutations_problem.utils import mutations


class MyTestCase(unittest.TestCase):
    def test_case(self):

        actual_output = mutations("abcdexyz", 5,'M')

        expected_output = "abcdeMyz"
        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
