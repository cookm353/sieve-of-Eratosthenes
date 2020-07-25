# !/usr/bin/env python3

# sieve_of_eratosthenes.py
# Algorithm for finding prime numbers based on multiples of primes under 10
# m. cook


import numpy as np

N = 40

PRIMES = [2, 3, 5, 7]


def filter_primes(nums):
	"""
	Filter for only prime numbers
	"""
	for prime in PRIMES:
		nums = list(filter(lambda x: x in PRIMES or x % prime != 0, nums))

	return nums


def main():
	nums = list(range(2, N + 1))
	primes = filter_primes(nums)

	print(primes)


if __name__ == "__main__":
	main()