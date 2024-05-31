import unittest
from src.no_idea_problem.utils import no_idea


class MyTestCase(unittest.TestCase):
    def test_case(self):

        actual_output = no_idea(5,3,[1,2,3,4,5],[1,3,5],[2,7,8])

        expected_output = 2
        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
