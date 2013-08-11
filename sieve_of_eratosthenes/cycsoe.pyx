
cdef extern from "soe.c":
    int find(int n)
    
def find2(int n):
    return find(n)