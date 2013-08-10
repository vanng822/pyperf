import unittest
import inspect
import cymandelbrot
import cmandelbrot
from mandelbrot import pymandelbrot, swigmandelbrot
import time

import cProfile
 
class MandelbrotTest(unittest.TestCase):
    
    def test_p_c_time(self):
        
        pr = cProfile.Profile()
        pr.enable()
        t = time.time()
        cmandelbrot.draw()
        ctotal = time.time() - t
        
        print '\nMandelbrot C Elapsed %.06f' % ctotal
        
        pr.disable()
        pr.print_stats()
        
        pr = cProfile.Profile()
        pr.enable()
        t = time.time()
        pymandelbrot.draw()
        ptotal = time.time() - t
        print '\nMandelbrot Python Elapsed %.06f' % ptotal
        pr.disable()
        pr.print_stats()
        
        pr = cProfile.Profile()
        pr.enable()
        t = time.time()
        swigmandelbrot.draw()
        swigtotal = time.time() - t
        print '\nMandelbrot Swig Elapsed %.06f' % swigtotal
        pr.disable()
        pr.print_stats()
        
        
        pr = cProfile.Profile()
        pr.enable()
        t = time.time()
        cymandelbrot.draw()
        cytotal = time.time() - t
        
        print '\nMandelbrot Cython Elapsed %.06f' % cytotal
        
        pr.disable()
        pr.print_stats()
        
        print '\n %f times slower' % (ptotal / cytotal)
        
        
if __name__ == "__main__":
    MandelbrotTest()