pyperf
======

for some simple performance test on python
# assume python 2.7

> virtualenv -p python python2.7

> source python2.7/bin/activate

> pip install cython

# for compiling latest version of cymandelbrot
> cython mandelbrot/cymandelbrot.pyx

# run the test code
> python setup.py test -s tests.test_mandelbrot_compare.MandelbrotTest
