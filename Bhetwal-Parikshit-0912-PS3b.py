# NOTE: Collaborated with **Clint Eisenzimmer** on 09/12/2019 at 2pm office hours with TA Brooks. 
def GreedyAlgo(k, arr):
	#Initialize the output 
	output = []

	charge = k 
	# We start at 1 because the first index is the start 
	for i in range(1, len(arr)): 
		# Check if we're out of charge 
		if(charge - arr[i] < 0): 
			# So we know we had to charge at previous index 
			output += [arr[i-1]]
			# Increase the range of the robot by charging 
			charge  = arr[i-1] + k
	# Output 
	print(output)

# Additional test case 
GreedyAlgo(20, [0,10,15,18,22,37,39,50])

# Test cases from assignment 
GreedyAlgo(40, [0,20,37,54,70,90])
GreedyAlgo(20, [0,18,21,24,37,56,66])
GreedyAlgo(20, [0,10,15,18])