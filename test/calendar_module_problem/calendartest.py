import unittest
from src.calendar_module_problem.utils import cal_module


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = cal_module("22 12 1987")

        expected_output = "TUESDAY"
        self.assertEqual(actual_output, expected_output)

    def test_case2(self):
        actual_output = cal_module("31 05 2024")

        expected_output = "FRIDAY"
        self.assertEqual(actual_output, expected_output)
    # add assertion here


if __name__ == '__main__':
    unittest.main()
