import random
def alignStrings(x, y, c_insert, c_delete, c_sub):
	"""
	This function fills in a cost matrix, S, that contains 
	the optimal costs for all the subproblems for aligning 
	x and y.

	:param x: (Required) The string to transform from  
	:param y: (Required) The string to transform to
	:param c_insert: (Required) The cost of inserting 
	:param c_delete: (Required) The cost of deleting 
	:param c_sub: (Required) The cost of substituting 
	:returns S: The cost matrix  
	"""
	# Initialize 
	S = [[None for _ in range(len(y)+1)] for _ in range(len(x)+1)]
	S[0][0] = 0

	# First row 
	for i in range(1, len(y)+1):
		S[0][i] = i * c_insert

	# First column 
	for j in range(1, len(x)+1):
		S[j][0] = j * c_delete

	for i in range(1, len(x)+1):
		for j in range(1, len(y)+1):
			# If x[i-1] != y[j-1]
			local_sub = c_sub
			# If no-op, then set substitution cost as 0 
			if(x[i-1] == y[j-1]):
				local_sub = 0
			# Take minimum of sub-problems
			S[i][j] = min(S[i][j-1] + c_insert, 
						  S[i-1][j-1] + local_sub, 
						  S[i-1][j] + c_delete)
	return S

def extractAlignment(S, x, y, c_insert, c_delete, c_sub):
	"""
	This function builds of alignStrings such that it 
	backtracks from the last filled in cell of S to 
	find the optimal operations to transform x to y.

	:param S: (Required) The cost matrix that contains 
	          the optimal costs for all the subproblems 
	          that will transform x to y 
	:param x: (Required) The source string  
	:param y: (Required) The target string 
	:param c_insert: (Required) The cost of inserting 
	:param c_delete: (Required) The cost of deleting 
	:param c_sub: (Required) The cost of substituting 
	:returns a: The optimal operations to transform 
				x to y
	"""
	i, j, a = len(x), len(y), []
	# Back tracking from S[len(x)][len(y)]
	while i != 0 or j != 0: 
		tie, local_sub = [], c_sub

		# Characters are same 
		if(x[i-1] == y[j-1]):
			# Just assign sub cost to 0 
			local_sub = 0 

		# Insert 
		if(S[i][j-1] + c_insert == S[i][j]):
			tie += ['insert']

		# Sub or no-op 
		if(S[i-1][j-1] + local_sub == S[i][j]):
			if(local_sub == 0):
				# Using a special symbol to denote no-ops
				tie += [':']
			else:
				# Substitute 
				tie += ['sub']
		# Delete 
		if(S[i-1][j] + c_delete == S[i][j]):
			tie += ['delete']

		# If tie, choose random 
		op = random.choice(tie)
		# Add to a 
		a += [op]

		# Back track according to added operation 
		# No-op 
		if(op == ':'):
			i -= 1
			j -= 1
		# Sub 
		elif(op == 'sub'):
			i -= 1
			j -= 1
		# Insert 
		elif(op == 'insert'):
			j -= 1
		# Delete
		elif(op == 'delete'):
			i -= 1

	# We started at last element, so reverse a 
	a.reverse()
	return a

def commonSubstrings(x, L, a):
	"""
	This function finds the substrings of at least
	length L in x that aligns exactly, via a run of
	no-ops, to a substring in y.

	:param x: (Required) The source string  
	:param L: (Required) The length (at least) that 
			  the substrings should be   
	:param a: (Required) The optimal operations 
	          to transform x to y
	:returns common: The substrings of at
	                 least length L 
	"""
	# Make a copy of x as a list 
	_x = list(x)
	# Insert a '_' where an insert would take place 
	for i in range(len(a)):
		if(a[i] == 'insert'): 
			_x.insert(i, '_')
	
	i, common = 0, []
	# Loop through a
	while(i < len(a)):
		sub_str = ''
		# While a[i] is a no-op 
		while(a[i] == ':' and i != len(a)-1): 
			sub_str += _x[i]
			i += 1 
		# Getting last element if its no-op
		if(a[i] == ':'):
			sub_str += _x[i]
		# If substring is greater or equal to L 
		if(sub_str != '' and len(sub_str) >= L):
			# It is a common substring
			common += [sub_str]
		i += 1
	return common 

def Driver(s, t, c_insert, c_delete, c_sub, L):
	"""
	This function runs alignStrings, extractAlignment
	and commonSubstrings and prints the return values 
	from those functions in a readable format. 

	:param s: (Required) The source string 
	:param t: (Required) The target string 
	:param c_insert: (Required) The cost of inserting 
	:param c_delete: (Required) The cost of deleting 
	:param c_sub: (Required) The cost of substituting
	:param L: (Required) The L parameter to be passed 
	          into commonSubstrings
	""" 
	# Cost matrix 
	sol = alignStrings(s, t, c_insert, c_delete, c_sub)
	print("c(insert): " + str(c_insert), "c(delete): " + str(c_delete), 
		  "c(substitute): " + str(c_sub), sep='\t'), print()
	print("    ", *t, sep='\t'), print()
	s_aug = " "+s
	print('\n'.join([s_aug[r]+'\t'+'\t'.join([str(cell) for cell in sol[r]]) for r in range(len(sol))]), '\n')

	# Optimal operations 
	ops = extractAlignment(sol, s, t, c_insert, c_delete, c_sub)
	print("Ops:", ops, "\n")

	# Common sub strings of at least length L 
	comm_substrs = commonSubstrings(s, L, ops)
	print("Common substrings of length at least", str(L) + ":") 
	print(*comm_substrs, sep=', ')

'''
Test Code - to be passed into driver  
'''
# Here the source, target and costs are for 1a 
s = "EXPONENTIAL"
t = "POLYNOMIAL"
c_insert, c_delete, c_sub = 2, 1, 2

# Using L = 2 as test
L = 2

# Call Driver function 
Driver(s, t, c_insert, c_delete, c_sub, L), print()


'''
1c) PLAGARISM DETECTOR 
'''
# Open the two files
s1 = open("Song1_Folsom_Prison.txt")
s2 = open("Song2_Crescent_City_Blues.txt")

# Read the two files 
song1 = s1.read()
song2 = s2.read()

# Insert, Delete, and Sub costs 
c_insert, c_delete, c_sub = 1, 1, 1

# Per instructions, L = 10
L = 10

# Source is first song, target is second song 
s = song1
t = song2

# Call our functions 
sol = alignStrings(s, t, c_insert, c_delete, c_sub)
ops = extractAlignment(sol, s, t, c_insert, c_delete, c_sub)
comm_substrs = commonSubstrings(s, L, ops)

# Get the length of the substrings 
lens = []
for j in range(len(comm_substrs)): 
	lens += [len(comm_substrs[j])]

# Print as table 
print(), print("            Plagarism Detector: Folsom Prison vs Crescent City Blues", '\n')
merge = dict(zip(comm_substrs, lens))
print("{:<70} {:<50}".format('Common Substring', 'Length'))
print("------------------------------------------------------------------------------")
for k, v in merge.items():
	print("{:<70} {:<50}".format(k, v))

# Close opened files
s1.close()
s2.close()
