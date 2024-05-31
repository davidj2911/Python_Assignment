import unittest
from src.mean_var_std_problem.utils import mean_var_std


class MyTestCase(unittest.TestCase):
    def test_case(self):

        actual_output = mean_var_std([[1,2],[3,4],[5,6]])

        expected_output = '[1.5 3.5 5.5]\n[2.66666667 2.66666667]\n1.708'


        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
