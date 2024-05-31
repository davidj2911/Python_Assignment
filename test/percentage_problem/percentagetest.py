import unittest
from src.percentage_problem.utils import percentage_cal


class MyTestCase(unittest.TestCase):
    def test_case(self):

        actual_output = percentage_cal({'John' :[50,60,70], 'Max' :[60,70,80],
                                        'Jim' :[70,80,90]},'Max')

        expected_output = "70.00"
        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
