
import unittest
import inspect
import time
import cProfile
from sieve_of_eratosthenes import soe, swigsoe
import cysoe
import csoe
import cycsoe

MAX_NO = 10000000
#MAX_NO = 30
 
class SoeTest(unittest.TestCase):
    def test_soe(self):
        
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
        
        swigsoe_pr = cProfile.Profile()
        swigsoe_pr.enable()
        t = time.time()
        swigsoe_result = swigsoe.find(MAX_NO)
        swigtotal = time.time() - t
        swigsoe_pr.disable()
        swigsoe_pr.print_stats()
        
        cycsoe_pr = cProfile.Profile()
        cycsoe_pr.enable()
        t = time.time()
        cycsoe_result = cycsoe.find2(MAX_NO)
        cycsoetotal = time.time() - t
        cycsoe_pr.disable()
        cycsoe_pr.print_stats()
        
        pr = cProfile.Profile()
        pr.enable()
        t = time.time()
        soe_result = soe.find(MAX_NO)
        total = time.time() - t
        pr.disable()
        pr.print_stats()
        
        print 'py/c %s' % (total / ctotal)
        print 'py/cython_c %s' % (total / cycsoetotal)
        print 'py/cython %s' % (total / cytotal)
        print 'py/swig %s' % (total / swigtotal)
        print 'found: %d' % soe_result
        self.assertEqual(soe_result, cysoe_result)
        self.assertEqual(soe_result, csoe_result)
        self.assertEqual(soe_result, swigsoe_result)
        self.assertEqual(soe_result, cycsoe_result)
        
