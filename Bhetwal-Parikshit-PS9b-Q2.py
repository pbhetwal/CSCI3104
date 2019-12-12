# Q2b - O(n) space
def MaxPointsTabulation(A):
	"""
	(Assumption) There is more than one assignment 

	This function uses dynamic programming to pick 
	which assignments to complete from 'A' to
	maximize the available points while not
	solving any two consecutive assignments. 
	Here, tabulation is used for O(n) space. 

	:param A: (Required) The array of points 
			  available to perform MaxPointsTabulation on 
	:returns M[len(A)-1]: The maximized value of points  
	""" 
	M = [0]*len(A)
	M[0], M[1] = A[0], max(A[0], A[1])

	for i in range(2, len(A)): 
		M[i] = max(M[i-1], A[i]+ M[i-2])

	return M[len(A)-1]

# Q2c - O(1) space
def MaxPointsO1(A):
	"""
	(Assumption) There is more than one assignment 

	This function uses dynamic programming to pick 
	which assignments to complete from 'A' to 
	maximize the available points while not
	solving any two consecutive assignments. 
	Here, tabulation is not used to reduce space 
	complexity to O(1). 

	:param A: (Required) The array of points 
			  available to perform MaxPointsO1 on 
	:returns take: The maximized value of points  
	""" 
	take, leave = A[0], 0

	for i in range(1, len(A)):
		leave, take = take, max(take, A[i] + leave)

	return take

# IMPORTANT - THIS CAN BE CHANGED TO ANY ARRAY
Input = [7, 2, 9, 3, 1, 9]
# IMPORTANT - THIS CAN BE ChANGED TO ANY ARRAY 

"""
Q2b - Print the array of points passed to MaxPointsTabulation(A)
and the output from this function
"""
Output = MaxPointsTabulation(Input)
print("Input =", Input)
print("Output (With Tabulation) =", Output, '\n')

"""
Q2c - Print the array of points passed to MaxPointsO1(A)
and the output from this function
"""
Output = MaxPointsO1(Input)
print("Input =", Input)
print("Output (Without Tabulation) =", Output)