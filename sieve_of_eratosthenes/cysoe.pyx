
cdef extern from "math.h":
    double sqrt(double arg)

from libc.stdlib cimport malloc, free
    
def find(int n):
    
    cdef int i, ip2, jj, j, r
    
    ## list of boolean indexed from 0..n; only from 2 will used
    #array = [True for i in range(0, n+1)]
    # implement of the line above; use 1 or 0 instead
    cdef int* array
    array = <int*> malloc(n * sizeof(int))
    for i in range(0, n+1):
        array[i] = 1
    
    i = 2
    cdef int nsqrt = <int> sqrt(n)
    while i <= nsqrt:
        if array[i]:
            ip2 = i * i
            j = ip2
            jj = 1
            while j <= n:
                array[j] = 0
                j = ip2 + jj * i
                jj += 1
        
        i += 1
        
    r = 0
    for i in range(2, n+1):
        if array[i]:
            r += 1
    
    free(array)
    
    return r