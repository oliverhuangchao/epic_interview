# Two Primes 
# Goldbach's conjecture : Every even integer greater than 2 can be expressed as the sum of 
# two primes. Write a function which takes a number as input, verify if is an even number 
# greater than 2 and also print at least one pair of prime numbers. 

import math

def isPrime(num,primelist):
	if num == 0 or num == 1:
		return False
	z = int(math.sqrt(num))
	for i in primelist:
		if i > z:
			return True
		else:
			if num % i == 0:
				return False
	return True

def twosum(nums,target):
	check = set(nums)
	for i in nums:
		if target-i in check:
			return (i,target-i)



def Goldbach(nums):
	if nums % 2 != 0 or nums == 2:
		print "invalid input"
		return False
	else:
		print "even number"
	z = nums
	primelist = []
	for i in range(2,z):
		if isPrime(i,primelist):
			primelist.append(i)

	res = twosum(primelist,nums)
	print str(nums) + " = " + str(res)

	#print primelist

for i in range(100):
	if i % 2 == 0:
		Goldbach(i)