import math
import random

#Returns true if the number is prime, false otherwise
def is_prime(num):
    if num & 1 == 0:
        return False


    for i in xrange(3,int(math.ceil(math.sqrt(num))+1),2):
        if(num % i == 0):
            return False
    return True

#Returns the largest value for a prime number that we want
def get_max(digit):
    size = 1
    for i in range(digit):
        size = size * 10
    return size

#Gets two prime numbers of the specified size
def get_prime_numbers(digits):
    digits = get_max(digits)
    key1 = 2
    while(is_prime(key1) == False):
        key1 = random.randint(1,digits)

    key2 = 2
    while(is_prime(key2) == False):
        key2 = random.randint(1,digits)

    return key1,key2

#calculate the modulus of two values
def modulus(key1,key2):
    return key1* key2

#calculate the totient of two values
def totient(key1,key2):
    return (key1-1)*(key2 -1)

#Gets the factors of a given number
def get_factors(n):
    return set(reduce(list.__add__,
    ([i,n//i] for i in range(1,int(n**0.5)+1) if n % i ==0)))

#Checks to see if the values are co_primes
def is_coprime(value1,value2):
    factors1 = get_factors(value1)
    factors2 = get_factors(value2)
    factors1.remove(1)
    factors2.remove(1)
    for spot in factors1:
        for factor in factors2:
            if(spot == factor):
                return False

    return True

#Gets a valid value for e, which needs to be co_prime to the totient of p, q
def get_e(key1,key2):
    flag = False
    while(flag == False):
        e = random.randint(1,modulus(key1,key2))
        flag = is_coprime(e,totient(key1,key2))
    return e

#Calculates the inverse modulo of a to m
def invereMod(a,m):
    for i in range(1,m):
        if(m*i + 1) % a ==0:
            return (m*i +1) //a
    return None

#Gets all of the values to their correct spots in the process
def make_key_set(digits):
    key1, key2 = get_prime_numbers(digits)
    #key1 = 3
    #key2 = 11
    print key1,key2
    n = modulus(key1,key2)
    e = get_e(key1,key2)
    #e = 7
    tot = totient(key1,key2)
    d = invereMod(e,tot)
    print "D: ",d
    return (e,n), (d,n)

#Given the public key, the function encrypts the value
def encrypt(value, e,n):
    return (value**e) % n

#Given the private key and modulus, it decrypts the value
def decrypt(value,d,n):
    #print value ** d
    return (value**d) % n


def main():
    M = 8
    pub, pri = make_key_set(3)
    C = encrypt(8,pub[0],pub[1])
    D = decrypt(C,pri[0],pri[1])
    print D
     #print C, decrypt(C,13,33)


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
