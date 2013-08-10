
import unittest
import inspect
import time
import cProfile
from sieve_of_eratosthenes import soe
import cysoe

MAX_NO = 10000000
#MAX_NO = 30
 
class SoeTest(unittest.TestCase):
    def test_soe(self):
        pr = cProfile.Profile()
        pr.enable()
        t = time.time()
        soe_result = soe.find(MAX_NO)
        total = time.time() - t
        pr.disable()
        pr.print_stats()
        
        cysoe_pr = cProfile.Profile()
        cysoe_pr.enable()
        t = time.time()
        cysoe_result = cysoe.find(MAX_NO)
        cytotal = time.time() - t
        cysoe_pr.disable()
        cysoe_pr.print_stats()
        print '%s' % (total / cytotal)
        
        self.assertEqual(soe_result, cysoe_result)
        
