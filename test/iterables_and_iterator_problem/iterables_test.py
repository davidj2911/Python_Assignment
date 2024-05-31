import unittest
from src.iterables_and_iterator_problem.utils import iter_func


class MyTestCase(unittest.TestCase):
    def test_case(self):

        actual_output = iter_func(4, "aacd", 2)

        expected_output = 0.833
        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
