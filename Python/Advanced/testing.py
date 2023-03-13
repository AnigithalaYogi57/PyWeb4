from factorial import factoral, division
import unittest

print("in testing file",__name__)


class MyTest(unittest.TestCase):
    '''our basic test class'''
    def test_fact(self):
        res = factoral(5)
        self.assertEqual(res,120)
    def test_div(self):
        res1 = division(5)
        self.assertEqual(res1,2)
    def test_sum(self):
        assert sum([1, 2, 3]) == 6
        
if __name__ == "__main__":
    unittest.main()