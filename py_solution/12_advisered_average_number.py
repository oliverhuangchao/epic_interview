# Advisered Average Number 
# Write aprogram to display the advisered average for the list of numbers my omittingthe three 
# largest number in the series. 
# E.g:3,6,12,55,289,600,534,900,172.  avg=(3+6+12+55+289+172) /6and 
# eliminating534,900,600 


import heapq
def advisered_average(nums):
	# O(nlog(n)) solution
	#nums.sort()
	#return sum(nums[:len(nums)-3])/(len(nums)-3)

	# O(n) solution
	# using heap
	if len(nums) <= 3:
		return 0
	x = nums[:3]
	heapq.heapify(x)
	for i in nums[3:]:
		heapq.heappush(x,i)
		heapq.heappop(x)

	res = (sum(nums)-sum(x))/(len(nums)-3)
	return res




nums = [3,6,12,55,289,600,534,900,172]
print advisered_average(nums)