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

# Compiling using swig on Mac but inchecked binary should work if you don't have swig
> cd mandelbrot

> swig -python swigmandelbrot.i 

> gcc -c mandelbrot.c swigmandelbrot_wrap.c -I../python2.7/lib/python2.7/

> gcc -bundle `python-config --ldflags` mandelbrot.o swigmandelbrot_wrap.o -o _swigmandelbrot.so