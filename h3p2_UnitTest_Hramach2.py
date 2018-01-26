#DO NOT CHANGE ANY CODE IN THIS FILE
#YOU DO NOT HAVE TO SUBMIT THIS FILE. IT IS MEANT FOR TESTING OF YOUR CODE
import unittest
import sys
from h3p2_recursive_hramach2 import Recursion as recu
from h3p2_dp_hramach2 import dp as dp
from h3p2_memoized_hramach2 import Memoization as memo

class TestCases(unittest.TestCase):

    def testcase1(self):
        mm_instance1 = recu()
        mm_instance2 = dp()
        mm_instance3 = memo()
        p = [5, 2, 4, 7, 7, 3, 9, 7, 8, 8, 6, 3, 7, 5, 5]
        i = 1
        j = len(p)-1
        answer_recursive = 2315
        answer_dynamic = 960
        answer_memoized = 960
        answer_recursive_output = mm_instance1.recursive(p, i, j)
        answer_dynamic_output = mm_instance2.dynamic(p, j)
        answer_memoized_output = mm_instance3.memoized(p, i, j)
        print("Recursive output = ", answer_recursive_output)
        print("Dynamic output = ", answer_dynamic_output)
        print("Memoized output = ", answer_memoized_output)
        self.assertEqual(answer_recursive_output,answer_recursive)
        self.assertEqual(answer_dynamic_output,answer_dynamic)
        self.assertEqual(answer_memoized_output,answer_dynamic)


if __name__ == '__main__':
    unittest.main()
