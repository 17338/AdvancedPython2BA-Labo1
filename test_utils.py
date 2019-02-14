# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(5),120)
        self.assertEqual(utils.fact(0),1)
        with self.assertRaises(ValueError):
            utils.fact(-5)
        # À compléter...
    
    def test_roots(self):
        # À compléter...
        self.assertEqual(utils.roots(1,2,1),(-1.0))
        self.assertEqual(utils.roots(1,1,1),())
        self.assertEqual(utils.roots(1,-1,-6),(3.0,-2.0))
    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
