
import unittest
import inspect
import time
import cProfile
from sieve_of_eratosthenes import soe
import cysoe
import csoe

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
        
        
        csoe_pr = cProfile.Profile()
        csoe_pr.enable()
        t = time.time()
        csoe_result = csoe.find(MAX_NO)
        ctotal = time.time() - t
        csoe_pr.disable()
        csoe_pr.print_stats()
        
        print 'py/cython %s' % (total / cytotal)
        print 'py/c %s' % (total / ctotal)
        print 'found: %d' % soe_result
        self.assertEqual(soe_result, cysoe_result)
        self.assertEqual(soe_result, csoe_result)
        
        
