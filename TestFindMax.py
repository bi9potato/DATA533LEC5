

import unittest
from FindMax import find_max

class TestFindMax(unittest.TestCase):
    
    def test_find_max(self):
        self.assertEqual(find_max(1,2), 2)
        self.assertEqual(find_max(10,2), 10)
        
unittest.main(argv=[''], verbosity=2, exit=False)