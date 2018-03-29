# This file was *autogenerated* from the file RSA.sage
from sage.all_cmdline import *   # import sage library
_sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_4 = Integer(4); _sage_const_8 = Integer(8); _sage_const_10 = Integer(10); _sage_const_0p5 = RealNumber('0.5'); _sage_const_300 = Integer(300)
import math
import random

#Returns true if the number is prime, false otherwise
def is_prime_max(num):
    if is_prime(num):
        return True
    return False

#Returns the largest value for a prime number that we want
def get_max(digit):
    size = _sage_const_1 
    for i in range(digit):
        size = size * _sage_const_10 
    return size

#Gets two prime numbers of the specified size
def get_prime_numbers(digits):
    digits = get_max(digits)
    key1 = _sage_const_4 
    while(is_prime_max(key1) == False):
        key1 = random.randint(_sage_const_1 ,digits)

    key2 = _sage_const_4 
    while(is_prime_max(key2) == False):
        key2 = random.randint(_sage_const_1 ,digits)

    return key1,key2

#calculate the modulus of two values
def modulus(key1,key2):
    return key1* key2

#calculate the totient of two values
def totient(key1,key2):
    return (key1-_sage_const_1 )*(key2 -_sage_const_1 )

#Gets the factors of a given number
def get_factors(n):
    return set(reduce(list.__add__,
    ([i,n//i] for i in range(_sage_const_1 ,int(n**_sage_const_0p5 )+_sage_const_1 ) if n % i ==_sage_const_0 )))

#Checks to see if the values are co_primes
def is_coprime(value1,value2):
    if(gcd(value1,value2) == _sage_const_1 ):
        return True
    return False

#Gets a valid value for e, which needs to be co_prime to the totient of p, q
def get_e(key1,key2):
    flag = False
    while(flag == False):
        e = random.randint(_sage_const_1 ,modulus(key1,key2))
        flag = is_coprime(e,totient(key1,key2))
    return e

#Calculates the inverse modulo of a to m
def invereMod(a,m):
    return inverse_mod(a,m)

#Gets all of the values to their correct spots in the process
def make_key_set(digits):
    key1, key2 = get_prime_numbers(digits)

    #key1 = 3
    #key2 = 11
    print "Primes: ", key1,key2
    n = modulus(key1,key2)
    print "n: ", n
    e = get_e(key1,key2)
    print "e: ",e
    #e = 7
    tot = totient(key1,key2)
    d = invereMod(e,tot)
    print "D: ",d
    return (e,n), (d,n)

#Given the public key, the function encrypts the value
def encrypt(value, e,n):
    return pow(value,e,n)
    #return (value**e) % n

#Given the private key and modulus, it decrypts the value
def decrypt(value,d,n):
    #print value ** d
    return pow(value,d,n)
    #return (value**d) % n


def main():
    M = _sage_const_8 
    pub, pri = make_key_set(_sage_const_300 )
    C = encrypt(_sage_const_8 ,pub[_sage_const_0 ],pub[_sage_const_1 ])
    D = decrypt(C,pri[_sage_const_0 ],pri[_sage_const_1 ])
    print "Encrypted Value: ", C
    print "Decrypted value: ", D
    #print is_prime_max(11)

    #C = encrypt(5,17,77)
    #print C
    #D = decrypt(C,53,77)
    #print D


    '''
    C = encrypt(2,pub[0],pub[1])
    print C
    D = decrypt(C,pri[0],pri[1])
    print 2, D
    '''

    #print is_coprime(get_factors(21),get_factors(28))

main()
