import unittest
from leapyear import is_leap


class TestIsLeap(unittest.TestCase):
    """Test cases for the is_leap function"""
    
    # Test divisible by 400 (leap year)
    def test_divisible_by_400(self):
        """Years divisible by 400 should be leap years"""
        self.assertTrue(is_leap(2000))
        self.assertTrue(is_leap(2400))
        self.assertTrue(is_leap(1600))
    
    # Test divisible by 100 but not 400 (not leap year)
    def test_divisible_by_100_not_400(self):
        """Years divisible by 100 but not 400 should not be leap years"""
        self.assertFalse(is_leap(1900))
        self.assertFalse(is_leap(2100))
        self.assertFalse(is_leap(2200))
    
    # Test divisible by 4 but not 100 (leap year)
    def test_divisible_by_4_not_100(self):
        """Years divisible by 4 but not 100 should be leap years"""
        self.assertTrue(is_leap(2004))
        self.assertTrue(is_leap(2008))
        self.assertTrue(is_leap(2012))
        self.assertTrue(is_leap(2016))
        self.assertTrue(is_leap(2020))
    
    # Test not divisible by 4 (not leap year)
    def test_not_divisible_by_4(self):
        """Years not divisible by 4 should not be leap years"""
        self.assertFalse(is_leap(2001))
        self.assertFalse(is_leap(2002))
        self.assertFalse(is_leap(2003))
        self.assertFalse(is_leap(2005))
        self.assertFalse(is_leap(2019))
    
    # Test boundary values
    def test_boundary_values(self):
        """Test boundary values"""
        self.assertTrue(is_leap(1900))  # Lower boundary
        self.assertTrue(is_leap(100000))  # Upper boundary
    
    # Test years outside valid range
    def test_year_below_lower_bound(self):
        """Years below 1900 should return False"""
        self.assertFalse(is_leap(1800))
        self.assertFalse(is_leap(1000))
        self.assertFalse(is_leap(1))
    
    def test_year_above_upper_bound(self):
        """Years above 100000 should return False"""
        self.assertFalse(is_leap(100001))
        self.assertFalse(is_leap(200000))


if __name__ == '__main__':
    unittest.main()
