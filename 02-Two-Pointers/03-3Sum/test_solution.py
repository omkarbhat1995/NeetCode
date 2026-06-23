import unittest
from solution import threeSum

class TestThreeSum(unittest.TestCase):
    def test_01_example_1(self):
        self.assertCountEqual(threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])

    def test_02_example_2(self):
        self.assertEqual(threeSum([0,1,1]), [])

    def test_03_example_3(self):
        self.assertEqual(threeSum([0,0,0]), [[0,0,0]])
        
    def test_04_all_zeros(self):
        self.assertEqual(threeSum([0,0,0,0]), [[0,0,0]])
        
    def test_05_no_solution(self):
        self.assertEqual(threeSum([1,2,3,4,5]), [])
        
    def test_06_negative_no_solution(self):
        self.assertEqual(threeSum([-5,-4,-3,-2,-1]), [])
        
    def test_07_multiple_duplicates(self):
        self.assertCountEqual(threeSum([-2,-2,-2,0,0,0,2,2,2]), [[-2,0,2], [0,0,0]])
        
    def test_08_large_numbers(self):
        self.assertEqual(threeSum([-100000, 0, 100000]), [[-100000, 0, 100000]])
        
    def test_09_three_elements(self):
        self.assertEqual(threeSum([1,-1,0]), [[-1,0,1]])
        
    def test_10_target_zero_with_multiple_pairs(self):
        self.assertCountEqual(threeSum([-3, 1, 2, -2, 0, 2]), [[-3, 1, 2], [-2, 0, 2]])
        
    def test_11_all_same_non_zero(self):
        self.assertEqual(threeSum([1, 1, 1, 1]), [])
        
    def test_12_mixed_array(self):
        self.assertCountEqual(threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]), 
                              [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], 
                               [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]])

    def test_13_symmetric_array(self):
        self.assertCountEqual(threeSum([-4, -2, -1, 0, 1, 2, 4]), [[-4, 0, 4], [-2, 0, 2], [-1, 0, 1]])
        
    def test_14_distant_elements(self):
        self.assertCountEqual(threeSum([-10, -5, -1, 2, 8, 11]), [[-10, -1, 11], [-10, 2, 8]])

    def test_15_duplicates_in_middle(self):
        self.assertCountEqual(threeSum([-1, -1, 2, 2]), [[-1, -1, 2]])

if __name__ == '__main__':
    unittest.main()