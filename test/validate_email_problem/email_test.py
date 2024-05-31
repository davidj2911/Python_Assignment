import unittest
from src.validate_email_problem.utils import email_check


class MyTestCase(unittest.TestCase):
    def test_case1(self):

        actual_output = email_check("random12_3@gmail.com")

        expected_output = True
        self.assertEqual(actual_output, expected_output)  # add assertion here

    def test_case2(self):

        actual_output = email_check("random12_3@gmail.commm")

        expected_output = False
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
