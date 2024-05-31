import unittest
from src.floor_ceil_rint_problem.utils import fcr


class MyTestCase(unittest.TestCase):
    def test_case(self):

        actual_output = fcr([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])

        expected_output = ('[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]\n'
                           '[  2.   3.   4.   5.   6.   7.   8.   9.  10.]\n'
                           '[  1.   2.   3.   4.   6.   7.   8.   9.  10.]')

        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
