# Key pad permutation

# Phone has letters on the number keys. forexample, number 2 has ABC on it, number 3 has 
# DEF, 4 number has GHI,... , andnumber 9 has WXYZ. Write a program that will print out all 
# of the possiblecombination of those letters depending on the input.   


ori = {'2':'ABC','3':'DEF','4':'GHI','5':'JKL','6':'MNO','7':'PQRS','8':'TUV','9':'WXYZ'}
print ori
inputstring = "2345"
print inputstring
result = list()
path = list()

def dfs(ori,inputstring,step,result,path,pos):
	if step == len(inputstring):
		result.append("".join(path))
	else:
		for i in range(pos,len(inputstring)):
			#print inputstring[i]
			for item in ori[inputstring[i]]:
				path.append(item)
				dfs(ori,inputstring,step+1,result,path,i+1)
				path.pop()

	return


dfs(ori,inputstring,0,result,path,0)
print result