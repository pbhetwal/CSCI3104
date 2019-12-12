def existsSubset(S,t,k):
	"""
    This function uses dynamic programming to check if there 
    is a subset of S of size k that sums to t. If one exists, 
    it will return the subset otherwise it will return False. 
  
  	:param S: (Required) The array to check 
  	:param t: (Required) The target value 
  	:param k: (Required) The restraint on subset size 
  	:returns M[n][t][k]: False if not possible 
  	:returns subset: The subset if it is possible 
  	""" 
	n = len(S)
	# M[n+1][t+1][k+1]
	M = [[[False for _ in range(k+1)]for _ in range(t+1)]for _ in range(n+1)]
	
	# Base: if k is 0 and t is 0 
	# For any n, we can achieve 0 with size 0 subset 
	# Otherwise, every other cell is False   
	for i in range(n+1): 
		M[i][0][0] = True

	# Fill M[n][t][k]
	# The run-time of this algorithm is O(ntk)
	# because at worst we are filling in a 3D array 
	# of size n*t*k
	for i in range(1, n + 1):
		for j in range(1, t + 1):
			for l in range(1, k + 1):
				# Total target so far is less than array element 
				if(j < S[i-1]):
					M[i][j][l] = M[i-1][j][l]
				# Total target so far is greater (or equal) than array element 
				elif(j >= S[i-1]):
					# Leave 
					leave = M[i-1][j][l]
					# Take 
					take = M[i-1][j - S[i-1]][l-1]
					# Only False or False will be False 
					M[i][j][l] = leave or take 

	# If possible, back track 
	# We are still basing back-tracking 
	# off of the array of size ntk 
	# so run-time remains at O(ntk)
	if(M[n][t][k]):
		# Initialize subset array 
		subset = [] 
		# Initialize i, j, and l 
		i, j, l = n, t, k
		# While i, j, and l are all greater than 0 
		while(i != 0 and j != 0 and l != 0):
			# Check if M[i][j][l] == take 
			if(M[i][j][l] == M[i-1][j - S[i-1]][l-1]):
				# Add to subset 
				subset += [S[i-1]]
				# Decrement relevant indices 
				j -= S[i-1]
				i -= 1 
				l -= 1
			else:
				i -= 1
		# Since we backtracked, reverse the subset
		subset.reverse()
		return subset 
	# If not possible, return False 
	return M[n][t][k]

def Tests(): 
	"""
    This function is used for testing existsSubset. 
    It prints the input and output for each test. 
  
  	:returns None: Nothing is returned 
  	""" 
	# Test 1 
	S = [2,1,5,7]
	t = 4
	k = 2
	print("Input: s = " + str(S) + ", " + "t = " + str(t) + ", " + "k = " + str(k))
	print("Output:", existsSubset(S, t, k), "\n")

	# Test 2
	S = [2,1,5,7]
	t = 6
	k = 2
	print("Input: s = " + str(S) + ", " + "t = " + str(t) + ", " + "k = " + str(k))
	print("Output:", existsSubset(S, t, k), "\n")


	# Test 3
	S = [2,1,5,7]
	t = 6
	k = 3
	print("Input: s = " + str(S) + ", " + "t = " + str(t) + ", " + "k = " + str(k))
	print("Output:", existsSubset(S, t, k), "\n")

	# Test 4
	S = [3,2,7,1]
	t = 7
	k = 1
	print("Input: s = " + str(S) + ", " + "t = " + str(t) + ", " + "k = " + str(k))
	print("Output:", existsSubset(S, t, k), "\n")

	# Test 5
	S = [3,2,7,1]
	t = 4
	k = 3
	print("Input: s = " + str(S) + ", " + "t = " + str(t) + ", " + "k = " + str(k))
	print("Output:", existsSubset(S, t, k), "\n")

	# Test 6
	S = [3,2,7,1]
	t = 4
	k = 2
	print("Input: s = " + str(S) + ", " + "t = " + str(t) + ", " + "k = " + str(k))
	print("Output:", existsSubset(S, t, k), "\n")

	# Test 7
	S = [2,4,7,8,9]
	t = 11
	k = 3
	print("Input: s = " + str(S) + ", " + "t = " + str(t) + ", " + "k = " + str(k))
	print("Output:", existsSubset(S, t, k), "\n")

	# Test 8
	S = [2,4,7,8,9]
	t = 11
	k = 2
	print("Input: s = " + str(S) + ", " + "t = " + str(t) + ", " + "k = " + str(k))
	print("Output:", existsSubset(S, t, k), "\n")


	# Test 9
	S = [3,6,2,1]
	t = 3
	k = 2
	print("Input: s = " + str(S) + ", " + "t = " + str(t) + ", " + "k = " + str(k))
	print("Output:", existsSubset(S, t, k), "\n")

	# Test 10
	S = [3,6,2,1]
	t = 3
	k = 1
	print("Input: s = " + str(S) + ", " + "t = " + str(t) + ", " + "k = " + str(k))
	print("Output:", existsSubset(S, t, k), "\n")
 
Tests()