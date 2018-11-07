# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:06:34 2018

@author: mdb99
"""
import unittest 
import inc 
# import inc
class MyTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(inc(0), 1)
        self.assertEqual(inc(100), 101)
        self.assertEqual(inc(1), 2)
        self.assertEqual(inc(-1), 0)
        self.assertEqual(inc(3), 4)
        
        
if __name__ == '__main__':
    unittest.main()   
