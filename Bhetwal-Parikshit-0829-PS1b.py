import random 
import matplotlib.pyplot as plt 

# Takes as input an integer 'n'
def CountFlip(n):
	# Ensure n is a positive integer
	assert(n > 0)

	# Initialize array from 1 to n
	A = [i for i in range(1, n+1)]

	# Randomly shuffle array 
	random.shuffle(A)

	# Count total number of flips in shuffled array
	count = 0 
	for i in range(len(A)):
		j = i + 1
		while j < len(A):
			if A[i] > A[j] and i < j:
				count += 1
			j += 1
	print(count)
	return count

i = 1
x = []
y = []
while i <= 12:
	x += [2**i]
	y += [CountFlip(2**i)]
	i += 1
	
plt.plot(x,y)
plt.xlabel("n")
plt.ylabel("Number of flips")
plt.show()