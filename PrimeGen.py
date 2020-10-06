# PrimeGen.pyDiffieHellman.py
# Python Program to find prime numbers in a range
# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes
# Ib Helmer Nielsen, UCN october 2020

def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    i=1
    for p in range(n + 1):
        if prime[p]:
            print("{0:8d}".format(p),end='')
            print(" ",end='')
            if i % 16 == 0:
               print("")
            i+=1
if __name__ == '__main__':
    n = 100000000
    print("Following are the prime numbers smaller")
    print("than or equal to", n)
    SieveOfEratosthenes(n) 