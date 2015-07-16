# Largest Sum Sub Array 
# Find the largest sum contiguous sub array. The length of the returned sub array must beat least 
# of length 2. 


int_min = -2**30

def largestSubarray(nums):
	print nums
	z = [int_min]
	for i in range(1,len(nums)):
		z.append(nums[i]+nums[i-1])
	print z
	res = [int_min]
	subarray= [(int_min,int_min)]
	for i in range(1,len(nums)):
		# if i== len(nums)-1:
		# 	print z[i-1]
		if res[i-1]+nums[i]<z[i]:
			res.append(z[i])
			subarray.append((i-1,2))
		else:
			res.append(res[i-1] + nums[i])
			subarray.append((subarray[i-1][0],subarray[i-1][1]+1))

	index = res.index(max(res))
	print res
	print subarray
	return nums[subarray[index][0]:subarray[index][0]+subarray[index][1]]


nums = [-1,-3,-1,2,-4,6]
print largestSubarray(nums)