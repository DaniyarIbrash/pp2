<<<<<<< HEAD
from math import *
def is_prime (a):
    for i in range (2, int(sqrt(a))+1):
        if a % i == 0:
            return False
    return True
def filter_prime(b):
    c = []
    for i in range(len(b)):
        if is_prime(b[i]) == True:
            c.append(b[i])
    return c
arr = list(map(int, input().split()))
=======
from math import *
def is_prime (a):
    for i in range (2, int(sqrt(a))+1):
        if a % i == 0:
            return False
    return True
def filter_prime(b):
    c = []
    for i in range(len(b)):
        if is_prime(b[i]) == True:
            c.append(b[i])
    return c
arr = list(map(int, input().split()))
>>>>>>> 3e74417b4bbde6c973a867d9d5558965d07a52ed
print(*filter_prime(arr))