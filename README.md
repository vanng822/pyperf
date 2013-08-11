pyperf
======

for some simple performance test on python

# How to
	# assume python 2.7
	
	> virtualenv -p python python2.7
	
	> source python2.7/bin/activate
	
	> pip install cython
	
	# for compiling latest version of cymandelbrot
	> cython mandelbrot/cymandelbrot.pyx
	
	# run the test code
	> python setup.py test -s tests.test_mandelbrot_compare.MandelbrotTest
	
	# Compiling using swig on Mac but inchecked binary may work if you don't have swig
	> cd mandelbrot
	
	> swig -python swigmandelbrot.i 
	
	> gcc -c mandelbrot.c swigmandelbrot_wrap.c -I../python2.7/include/python2.7/
	
	> gcc -bundle `python-config --ldflags` mandelbrot.o swigmandelbrot_wrap.o -o _swigmandelbrot.so


# Result
## Mandelbrot

C-module

4 function calls in 0.015 seconds

Cython

4 function calls in 0.018 seconds

Swig on same c code as C-module

4 function calls in 0.027 seconds

Python

12329 function calls in 2.347 seconds

## Sieve of Eratosthenes

Python

7 function calls in 9.984 seconds

Cython

4 function calls in 0.180 seconds
 
C-module

4 function calls in 0.173 seconds

Swig

4 function calls in 0.269 seconds
