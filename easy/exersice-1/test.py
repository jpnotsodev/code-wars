import unittest
from app import duplicate_encode
from app import duplicate_encode_refactored

class TestMethod(unittest.TestCase):
    def test_function(self):
        self.assertEqual(duplicate_encode("Summer"), "(())((")
        self.assertEqual(duplicate_encode_refactored("recede"), "()()()")
        self.assertEqual(duplicate_encode("succeed"), "(())))(")
        self.assertEqual(duplicate_encode_refactored("seeds"), ")))()")
        self.assertEqual(duplicate_encode("Warriors"), "(())(()(")
        self.assertEqual(duplicate_encode_refactored("Elements"), ")()()(((")
        
if __name__ == "__main__":
    unittest.main()