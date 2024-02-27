#prime checker in pnc
#having any combination of integer in num that is prime

from itertools import permutations
def primeee(num):
    return num > 1 and all(num%i != 0 for i in range(2, int(num**0.5 +1)))

def check_primeee(num):
    x = [int(''.join(perm)) for perm in permutations(str(num))]
    a = 0
    for i in x:
        if primeee(i):
            a += 1
    if a == 0:
        return 0
    else:
        return 1

print(check_primeee(130))
