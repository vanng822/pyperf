
import os

from setuptools import setup, find_packages

from distutils.core import Extension

cmandelbrot = Extension('cmandelbrot', sources = ['mandelbrot/cmandelbrot.c']) 
cymandelbrot = Extension('cymandelbrot', ['mandelbrot/cymandelbrot.c'])

cysoe = Extension('cysoe', sources = ['sieve_of_eratosthenes/cysoe.c'])
cycsoe = Extension('cycsoe', sources = ['sieve_of_eratosthenes/cycsoe.c'])

csoe = Extension('csoe', sources = ['sieve_of_eratosthenes/csoe.c'])

here = os.path.abspath(os.path.dirname(__file__))


setup(name='pyperf',
      version='0.1',
      author='',
      author_email='',
      url='',
      packages=find_packages(),
      test_suite="tests",
      ext_modules = [cymandelbrot, cmandelbrot, cysoe, csoe, cycsoe],
)