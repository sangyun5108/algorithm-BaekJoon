import unittest
from Sol_10828 import Solution

class Test_10828(unittest.TestCase):
    def test1_10828(self):
        S = Solution()
        S.push(1)
        S.push(2)
        self.assertEqual(S.top(),2)
        self.assertEqual(len(S),2)
        self.assertEqual(S.isEmpty(),0)
        self.assertEqual(S.pop(),2)
        self.assertEqual(S.pop(),1)
        self.assertEqual(S.pop(),-1)
        self.assertEqual(len(S),0)
        self.assertEqual(S.isEmpty(),1)
        self.assertEqual(S.pop(),-1)
        S.push(3)
        self.assertEqual(S.isEmpty(),0)
        self.assertEqual(S.top(),3)
        
    def test2_10828(self):
        S = Solution()
        self.assertEqual(S.pop(),-1)        
        self.assertEqual(S.pop(),-1)
        S.push(123)
        self.assertEqual(S.top(),123)
        self.assertEqual(S.pop(),123) 
        self.assertEqual(S.top(),-1)
        self.assertEqual(S.pop(),-1)      
         
unittest.main()
