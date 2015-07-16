# Spiral Matrix 
# Given aNXN matrix, starting from the upper right corner of the matrix start printingvalues in a 
# counter-clockwise fashion.  
# E.g.: Consider N = 4  
# Matrix= {a, b, c, d,  
#         e, f, g, h,  
#         i, j, k, l, . visit 1point3acres.com for more. 
#         m, n, o, p}  
# Your function should output: dcbaeimnoplhgfjk 


def spiral_matrix(matrix):
	res = []
	while matrix:
		for i in matrix[0]:
			res.append(i)
		#print res
		del matrix[0]
		for i in matrix:
			res.append(i.pop())
		if matrix:
			res.extend(matrix.pop()[::-1])

		for i in matrix:
			res.append(i[0])
			del i[0]
		#print res
	return res

matrix = [[1,2,3,11],[8,9,4,12],[7,6,5,13]]
for i in matrix:
	print i
print spiral_matrix(matrix)