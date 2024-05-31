import unittest
from src.namedTuple_problem.utils import avg_namedTuple


class MyTestCase(unittest.TestCase):
    def test_case(self):

        actual_output = avg_namedTuple([
            "5",
            "ID MARKS NAME CLASS",
            "1 80 ram 6",
            "2 69 john 7",
            "3 74 jack 9",
            "4 90 ravi 10",
            "5 95 abdul 8"
        ])

        expected_output = "81.60"

        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
