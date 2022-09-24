# UNIT TEST
import array as arr
import unittest
from Sum_Subarr import sum_cont_subarr_1
from Sum_Subarr import sum_cont_subarr_2

class Test_sum_cont_arr(unittest.TestCase):

    def test_method_1(self):
        self.assertEqual(sum_cont_subarr_1(arr.array('i', [1,2,3,4,5,6])), ([1,2,3,4,5,6], 21))
        self.assertEqual(sum_cont_subarr_1(arr.array('i', [-1,-2,-3,-5])), (-1, -1))
        self.assertEqual(sum_cont_subarr_1(arr.array('i', [9, -1])), (9, 9))
        self.assertEqual(sum_cont_subarr_1(arr.array('i', [-9,-1,2,5,6,-7])), ([2,5,6], 13))
        self.assertEqual(sum_cont_subarr_2(arr.array('i', [9, -1, 2, -5, 6, -7])), ([9, -1, 2, -5, 6], 11))
        self.assertEqual(sum_cont_subarr_2(arr.array('i', [2])), ([2], 2))
        self.assertEqual(sum_cont_subarr_2(arr.array('i', [-3])), (-3, -3))

    def test_method_2(self):
        self.assertEqual(sum_cont_subarr_2(arr.array('i', [1,2,3,4,5,6])), ([1,2,3,4,5,6], 21))
        self.assertEqual(sum_cont_subarr_2(arr.array('i', [-1,-2,-3,-5])), (-1, -1))
        self.assertEqual(sum_cont_subarr_2(arr.array('i', [9, -1])), (9, 9))
        self.assertEqual(sum_cont_subarr_2(arr.array('i', [-9,-1,2,5,6,-7])), ([2,5,6], 13))
        self.assertEqual(sum_cont_subarr_2(arr.array('i', [9, -1, 2, -5, 6, -7])), ([9, -1, 2, -5, 6], 11))
        self.assertEqual(sum_cont_subarr_2(arr.array('i', [2])), ([2], 2))
        self.assertEqual(sum_cont_subarr_2(arr.array('i', [-3])), (-3, -3))

if __name__ == '__main__':
    unittest.main()