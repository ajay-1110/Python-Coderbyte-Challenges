#prime_mover
def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

def PrimeMover(num):
    primes = []
    current_num = 2
    while len(primes) < num:
        if is_prime(current_num):
            primes.append(current_num)
        current_num += 1
    return primes[-1]

print(PrimeMover(5)) 
