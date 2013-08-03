
import os

from setuptools import setup, find_packages

from distutils.core import Extension

cmandelbrot = Extension('cmandelbrot', sources = ['mandelbrot/cmandelbrot.c']) 
cymandelbrot = Extension('cymandelbrot', ['mandelbrot/cymandelbrot.c'])

here = os.path.abspath(os.path.dirname(__file__))


install_requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'sqlalchemy',
    'couchdb',
    'psycopg2',
    'waitress',
    ]

setup(name='pycrawl',
      version='0.1',
      author='',
      author_email='',
      url='',
      packages=find_packages(),
      test_suite="tests",
      ext_modules = [cymandelbrot, cmandelbrot],
)