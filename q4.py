# Write a generator prime_generator(n) that yields the first n prime numbers efficiently.
# Write a decorator measure_time that prints how long it takes to generate those primes.

import time


def prime_generator(n):
    ctr, num = 0, 2

    while ctr < n:
        for i in range(2, (num**0.5) + 1):
            if num % i == 0:
                break
            else:
                yield num
                ctr += 1

            num += 1


# def measure_time():
