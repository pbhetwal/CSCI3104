# Python imports 
import math

def CalculateHIndex(A, p, r):
	"""
	(Assumption: A's elements are sorted in descending order)
	This function calculates the h-index for a given 
	array of citations that correspond to a paper.    
	
	:param A: (Required) The array to perform a sorting 
			  routine on 
	:param p: (Required) The leftmost index of the 
			  array or sub-array 
	:param r: (Required) The rightmost index of the 
	          array or sub-array 
	:returns h_index: The h-index  
	""" 
	# Middle index 
	q = math.floor((p+r)/2)
	if(p <= r):
		if(A[q] >= q + 1):
			# Recurse right 
			return CalculateHIndex(A, q+1, r)
		else:
			# Recurse left 
			return CalculateHIndex(A, p, q-1)
	h_index = q + 1
	return h_index

# Replace with any array
A = [6, 5, 3, 1, 0] # h-index should be 3

p, r = 0, len(A) # Initialize p and r 

print(CalculateHIndex(A, p, r-1))