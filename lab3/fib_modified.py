#! /usr/bin/python

import sys, time

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

if __name__ == "__main__":
    # nterms is passed as an argument to this script
    nterms = int(sys.argv[1])

    tic = time.time()

    # check if the number of terms is valid
    if nterms <= 0:
       print("Please enter a positive integer")
    else:
       recur_fibo(nterms)

    tac = time.time()
    print('time spent: {}'.format(tac-tic))
