#!/usr/bin/python3
import random


def primeInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)
    return prime_list


prime_list = primeInRange(2, 14)
randomPrime_p = random.choice(prime_list)
randomPrime_q = random.choice(prime_list)

print(randomPrime_p)
print(randomPrime_q)

N = randomPrime_p * randomPrime_q
print(N)

phi_N = (randomPrime_p - 1) * (randomPrime_q - 1)
print(phi_N)

list_all = []


for i in range(2, N):
    list_all.append(i)


def factors(number):
    list1 = []
    for i in range(2, number):
        if number % i == 0:
            list1.append(i)
    return (list1)


def remove_co_prime(list):
    for i in list:
        for ii in range(1, N//2):
            if i*ii in list_all:
                list_all.remove(i*ii)


def remove_bigger(list):
    for i in list:
        if i in list_all:
            list_all.remove(i)


def decrypt(enc_key):
    i = 1
    while i > 0:
        formulae = (1+phi_N*i) % enc_key
        decrypt = int(i+phi_N*i)/enc_key
        if formulae == 0:
            return(decrypt)
        i += i


def ascii():
    ascii_list = []
    for char in message:
       
        ascii = ord(char)
        ascii_list.append(ascii)
    print(ascii_list)    


list_N = factors(N)
list_phi_N = factors(phi_N)


remove_co_prime(list_N)
remove_co_prime(list_phi_N)

list_bigger = []

for i in list_all:
    if i > phi_N:
        list_bigger.append(i)


remove_bigger(list_bigger)

enc_key = list_all[0]
dec_key = decrypt(enc_key)

print(enc_key)
print(dec_key)

print("Enter text to be encypted :", end="")
message = input()
textlenth = len(message)
conv = ascii()
print(conv)
