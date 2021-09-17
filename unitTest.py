import unittest
from unittest import result
import intSort
import stringSort
import mainSort

class testStringSort(unittest.TestCase):
    
    def test_sortStr(self):
        result = stringSort.stringSorted(mainSort.stringArr)
        self.assertTrue

    def test_sortInts(self):
        result = intSort.intSorted(mainSort.randomList)
                
if __name__ == '__main__':
    unittest.main()
