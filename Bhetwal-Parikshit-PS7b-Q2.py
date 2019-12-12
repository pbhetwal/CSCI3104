# Python imports 
import random 
import math
import copy
import matplotlib.pyplot as plt 

def NumFlipsNaive(A):
	"""
	This function takes a sequence of n numbers in the range 
	[1,...,n] that were randomly shuffled. Then, it performs
	a sorting routine to count the number of flips in Θ(n²). 

	:param A: (Required) The array to perform a sorting 
			  routine on   
	:returns count: The number of flips 
	"""
	assert(n > 0)

	count = 0 
	for i in range(len(A)):
		j = i + 1
		while(j < len(A)):
			if(A[i] > A[j] and i < j):
				count += 1
			j += 1

	return count

def NumFlipsMerge(A, p, q, r):
	"""
	This function performs the merge portion of the NumFlipsMergeSort
	method that is called before this.   
	
	:param A: (Required) The array to perform a sorting 
			  routine on 
	:param p: (Required) The leftmost index (inclusive) of the 
			  array or sub-array 
	:param q: (Required) The middle index of the array A 
	:param r: (Required) The rightmost index (exclusive) of the 
	          array or sub-array 
	:returns count: The number of flips 
	:returns A: The array after this merge function executes 
	"""
	Low, High = copy.deepcopy(A[p:q+1]), copy.deepcopy(A[q+1:r+1])
	count =  0

	i, j, k = 0, 0, p

	while(i < len(Low) and j < len(High)):

		if(Low[i] <= High[j]):
			A[k] = Low[i]
			i += 1
		else:
			A[k] = High[j]
			j += 1
			count += (len(Low)-i)
		k += 1

	while(i < len(Low)):
		A[k] = Low[i]
		i+=1
		k+=1

	while(j < len(High)):
		A[k] = High[j]
		j+=1
		k+=1

	return A, count 

def NumFlipsMergeSort(A, p, r):
	"""
	This function takes a sequence of n numbers in the range 
	[1,...,n] that were randomly shuffled. Then, it performs
	a sorting routine to count the number of flips in Θ(nlog(n)). 
	
	:param A: (Required) The array to perform a sorting 
			  routine on 
	:param p: (Required) The leftmost index (inclusive) of the 
			  array or sub-array 
	:param r: (Required) The rightmost index (exclusive) of the 
	          array or sub-array 
	:returns count: The number of flips 
	:returns A1_A2: The final sorted array 
	"""
	assert(n > 0)

	if(p >= r):
		return A, 0

	A1_A2 = []
	count = 0 

	q = math.floor((p+r)/2)

	A1, A1_count = NumFlipsMergeSort(A, p, q)
	A2, A2_count = NumFlipsMergeSort(A, q+1, r) 
	A1_A2, merge_count = NumFlipsMerge(A, p, q, r)

	count += A1_count + A2_count + merge_count

	return A1_A2, count 

i = 1
x, y, y2 = [], [], [] 
while i <= 12:
	A = [i for i in range(1, (2**i)+1)]
	random.shuffle(A)
	x += [2**i]
	y += [NumFlipsNaive(A)]
	p, r = 0, len(A)
	y2 += [NumFlipsMergeSort(A, p, r-1)[1]] 
	i += 1

# After the figure appears, maximize the window for a clearer view 
fig, axes = plt.subplots(nrows=1, ncols=2)
plt.subplots_adjust(wspace = 0.45)
axes[0].plot(x,y)
axes[0].set_xlabel("n")
axes[0].set_ylabel("Number of flips (Naive)")

axes[1].plot(x, y2)
axes[1].set_xlabel("n")
axes[1].set_ylabel("Number of flips (Merge)")
plt.show()