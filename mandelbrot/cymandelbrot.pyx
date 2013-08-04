
import sys

stdout = sys.stdout

cdef int BAILOUT = 16
cdef int MAX_ITERATIONS = 1000

def draw():
    cdef int i, y
    for y in range(-39, 39):
      stdout.write('\n')
      for x in range(-39, 39):
        
        i = mandelbrot(x / 40.0, y / 40.0)
        
        if i == 0:
          stdout.write('*')
        else:
            stdout.write(' ')

cdef inline int mandelbrot(double x, double y):
  cdef double cr, ci, zr
  cdef int i
  
  cr = y - 0.5
  ci = x
  zi = 0.0
  zr = 0.0
  i = 0

  
  cdef double temp, zr2, zi2
  
  while True:
    i += 1
    temp = zr * zi
    zr2 = zr * zr
    zi2 = zi * zi
    zr = zr2 - zi2 + cr
    zi = temp + temp + ci
         
    if zi2 + zr2 > BAILOUT:
      return i
    if i > MAX_ITERATIONS:
      return 0





