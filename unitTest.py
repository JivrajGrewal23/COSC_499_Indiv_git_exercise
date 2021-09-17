import unittest
#unit tests
from unittest import result
import intSort
import stringSort
import mainSort

class testStringSort(unittest.TestCase):
    
    def test_sortStr(self):
        result = stringSort.quickString(mainSort.stringArr)
        self.assertTrue

    def test_sortInts(self):
        result = intSort.intsorter(mainSort.randomList)
        self.assertTrue

if __name__ == '__main__':
    unittest.main()
