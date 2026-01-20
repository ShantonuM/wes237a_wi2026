#include <unistd.h>
   
int myAdd(int a, int b) {
    sleep(2);
    return (a + b);
}

int myMult(int a, int b) {
    /* Skipping sanity check(s) and integer overflows */
    sleep(2);
    return (a * b);
}