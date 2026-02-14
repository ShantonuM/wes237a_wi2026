#! /usr/bin/python

import sys, time, ctypes

_libInC = ctypes.CDLL('./libMyCycletime.so')

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

if __name__ == "__main__":
    # nterms is passed as an argument to this script
    nterms = int(sys.argv[1])

    # Reset the counters
    _libInC.my_init_counters(1, 0)
    start_time = time.time() # "Before" time
    start_cyccnt = _libInC.my_get_cyclecount() # "Before" cycle count

    # check if the number of terms is valid
    if nterms <= 0:
       print("Please enter a positive integer")
    else:
       recur_fibo(nterms)

    end_time = time.time() # "After" time
    end_cyccnt = _libInC.my_get_cyclecount() # "After" cycle count

    print(f"{end_time - start_time}, {end_cyccnt - start_cyccnt}")