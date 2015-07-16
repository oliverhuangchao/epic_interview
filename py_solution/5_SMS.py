# SMS

# You are given a telephone keyboard 
# 0-0, 1-1, 2-ABC2, 3-DEF3, 4-GHI4, 5-JKL5, 6-MNO6,7-PQRS7, 8-TUV8, 9-WXYZ9, *-space, 
# #-char separater 
# if you type "2", you will get 'A', that is "2"-'A', "22"-'B' ,"222"-'C', "2222"-'D' 
# However, the digits can repeated many times 
# "22222"-you get 'A' again  . Waral 
# You can use "#" to separate characters, for example 
# "2#22", you get "AB" . 
# However, you may also have consecutive different digits without separator:"23"-'AD' 
# If you type "*", it means space. 
# You a given a sequence of digits, translate it into a text message 


import string

#prepare at the begining

ori = {0:'0', 1:'1', 2:'ABC2', 3:'DEF3', 4:'GHI4', 5:'JKL5', 6:'MNO6',7:'PQRS7', 8:'TUV8', 9:'WXYZ9'}
all = string.ascii_uppercase
newdict = dict()
for i in ori:
	newdict[str(i)] = ori[i][-1]

for i in range(2,10):
	count = 1
	for j in ori[i][:-1]:
		newdict[str(i)*count] = j#[str(i) for k in range(count)]
		count+=1


def transform(newdict,inputstring):
	words = inputstring.split("*")
	res = ""
	for item in words:
		z = item.split("#")
		for each in z:
			if each in newdict:
				res += newdict[each]
			else:
				x = each[0]
				for i in range(1,len(each)):
					if each[i] != x:
						res += newdict[each[:i]]
						res += newdict[each[i:]]
						x = each[i]

		res += " "
	print res

inputstring = "12*322#2*33"
print inputstring
transform(newdict, inputstring)

