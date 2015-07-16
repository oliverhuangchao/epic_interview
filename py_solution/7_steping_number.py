# coding = utf-8

# the stepping number:  
# A number is called as a stepping number if the adjacent digits are having adifference of 1. 
# For eg. 8,343,545 are stepping numbers. While 890, 098 arenot. The difference between a 
# '9' and '0' should not be considered as1. Given start number(s) and an end number (e) your 
# function should listout all the stepping numbers in the range including both the numbers s & 
# e. 




def dfs(result,path,step,size,start,end):
	#print path
	if step > size:
		return 
	if (path[-1]+1 == end or path[-1]-1 == end) and step<=size: 
		path = map(lambda x:str(x),path)
		path = "".join(path)
		path = path+str(end)
		result.append(path)
	else:
		path.append(path[-1]+1)
		dfs(result,path,step+1,size,start,end)
		path.pop()
		path.append(path[-1]-1)
		dfs(result,path,step+1,size,start,end)
		path.pop()

def create_step_number(start,end,size):
	result = list()
	path = list()
	path.append(start)
	dfs(result,path,0,size,start,end)
	print result


start = 5
end = 2
size = 7
create_step_number(start,end,size)
