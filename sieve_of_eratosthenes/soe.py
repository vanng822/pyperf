
import math

def find(n):
    ## list of boolean indexed from 0..n; only from 2 will used
    array = [True for i in range(0, n+1)]
    i = 2
    while i <= math.sqrt(n):
        if array[i]:
            ip2 = i * i
            j = ip2
            jj = 1
            while j <= n:
                array[j] = False
                j = ip2 + jj * i
                jj += 1
        
        i += 1
        
    r = 0
    for i in range(2, n+1):
        if array[i]:
            r += 1
            
    return r