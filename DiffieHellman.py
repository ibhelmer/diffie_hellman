# DiffieHellman.py
# Example of exchange key using Diffie-Hellman
# Ib Helmer Nielsen, UCN october 2020

def main():
    # Public know Variables
    n = 1423453  # large shared prime number, use PrimGen.py fot making prime number
    g = 17       # small shared prime number also called generator

    ibsPriKey = 7913   # only known by Ib
    bosPriKey = 1123   # only known by Bo

    # Info about global variables
    print("-----++++Example of how Diffie-Hellman works++++-----")
    print("Publicly Shared Variables:")
    print("    Publicly Shared Prime Number: ", n)
    print("    Publicly Shared Generator:    ", g)
    print("-----+++Exchange of public Key over network+++-------")

    # Ib Sends to Bo A = g^ibsPriKey mod n (** = exponentiation in Python)
    A = (g ** ibsPriKey) % n
    print("Ib Sends to Bo over Public Chanel: ", A)

    # Bo Sends to Ib B = g^boPriKey mod n (** = exponentiation in Python)
    B = (g ** bosPriKey) % n
    print("Bo Sends to Ib over Public Chanel: ",B)
    print("----++Privately Calculated Common Shared Secret++----")
    print("Privately Calculated Common Shared Secret:")

    # Ib's Computes Shared Secret: s = B^ibsPriKey mod n
    ibSharedSecret = (B ** ibsPriKey) % n
    print("Ibs Shared Secret: ", ibSharedSecret)

    # Bo's Computes Shared Secret: s = A^bosPriKey mod n
    bobSharedSecret = (A ** bosPriKey) % n
    print("Bob Shared Secret: ", bobSharedSecret)
    print("---------------------+++++++++++---------------------")

if __name__ == "__main__":
    main()