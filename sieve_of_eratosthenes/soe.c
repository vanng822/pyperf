#include <math.h>

#include <stdlib.h>

int find(int n) {
	if (n < 2) {
		return 0;
	}

    int i, ip2, jj, j, r;
    int* array;

    array = ( int*) malloc(n * sizeof(int));

    for (i = 0; i <= n; i++){
        array[i] = 1;
    }

    i = 2;
    int nsqrt = (int) sqrt(n);

    while (i <= nsqrt) {
        if (array[i]) {
            ip2 = i * i;
            j = ip2;
            jj = 1;
            while (j <= n) {
                array[j] = 0;
                j = ip2 + jj * i;
                jj++;
            }
        }
        i++;
    }
    r = 0;
    for (i = 2; i <= n; i++) {
        if (array[i]) {
            r++;
        }
    }

    free(array);

    return r;
}
