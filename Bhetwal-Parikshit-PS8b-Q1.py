# Python imports 
import math 
import random
import matplotlib.pyplot as plt 
import sys 
import io 

count = 0 # Initialize the number of comparisons 
def Partition(A, p, r):
  """
  This function, 'Partition', is used by QuickSelect 
  to find a suitable pivot for QuickSort 
  
  :param A: (Required) The array to perform
            Partition on  
  :param p: (Required) The leftmost index of the 
            array or sub-array 
  :param r: (Required) The rightmost index of the 
            array or sub-array 
  :returns i+1: The index used by QuickSelect 
  """ 
  global count # The number of comparisons will be global 
  x = A[r] # This is the pivot 
  i = p-1 # Initialize i 

  for j in range(p, r): # Loop from p to r 
    count = count + 1 # Increment the number of comparisons 
    if(A[j] <= x): # If the element at A[j] is <= the pivot 
      i = i + 1 # Increment i 
      A[j], A[i] = A[i], A[j] # Swap A[j] and A[i] 

  A[i+1], A[r] = A[r], A[i+1] # Swap A[i+1] and A[r]
  return i + 1 # Return i+1 (Partition returns an index)

def QuickSort(A, p, r):
  """
  This function, 'QuickSort', utilizes QuickSelect to 
  get a roughly 0.25-0.75 split
  
  :param A: (Required) The array to perform 
            QuickSort on  
  :param p: (Required) The leftmost index of the 
            array or sub-array 
  :param r: (Required) The rightmost index of the 
            array or sub-array 
  """ 
  if(p < r): # If the left index is less than the right index

    split = ((0.25 * (r-p+1)) + p) / len(A) # The left split 

    q = QuickSelect(A, p, r, split) # Call QuickSelect with split 
    print("Array after QuickSelect:", A, "p =", p, "r =", r) # Print the array after QuickSelect 
    QuickSort(A, p, q-1) # Recurse left  
    QuickSort(A, q+1, r) # Recurse right 

def QuickSelect(A, p, r, split): 
  """
  This function, 'QuickSelect', converts the split 
  parameter to a 'k' in order to return the index 
  of the kth smallest element to split on  
  
  :param A: (Required) The array to perform 
            QuickSelect on 
  :param p: (Required) The leftmost index of the 
            array or sub-array 
  :param r: (Required) The rightmost index of the 
            array or sub-array 
  :param split: (Required) The split that will 
                be converted to a 'k' for QuickSelect 
  :returns q: If 'k' equals the value returned by 'Partition'
  :returns r: If the length of the array or sub-array is 
              greater than 1, return the rightmost index
  """
  if(r-p+1 > 1): # If the size of the array or sub-array is greater than 1

    k = math.floor(split * len(A)) # This will be our k 
    q = Partition(A, p, r) # Partition for QuickSelect 

    if(q == k): # If we have our k equal to q 
      return q # Return q 
    elif(q > k): # If q is greater than k
      return QuickSelect(A, p, q-1, split) # Recurse left 
    else: # Otherwise 
      return QuickSelect(A, q+1, r, split) # Recurse right 

  else: # If the size of the array or sub-array is not greater than 1
    return r # Return the rightmost index (this can also be p)

def Driver(n):
  """
  This function, 'Driver', creates and shuffles an array 
  such that we have elements [1,...,n] within it and then 
  calls QuickSort on that array 
  
  :param n: (Required) The size of the array in question 
  :returns count: Returns the number of comparisons done 
                  with an array of size n 
  """
  global count # The global variable for comparisons 
  A = [_ for _ in range(1, n+1)] # Initialize A[1,...,n]
  random.shuffle(A) # Shuffle A 
 
  p, r = 0, len(A)-1 # Left index and right index of A 
  count = 0 # Initialize/Reset comparisons to 0 before QuickSort call 

  QuickSort(A, p, r) # Run QuickSort with A, p, and r 
  return count # Return the number of comparisons 
 
suppress = io.StringIO() # We'll use this to send sys.stdout to it
sys.stdout = suppress # Use dummy variable to suppress prints for plotting 

x, y = [], [] # Arrays for x and y points 
for i in range(1, 11): # Loop from 1 to 10 
  x += [2**i] # The array of x points (size of arrays - n)
  y += [Driver(2**i)] # The array of y points (comparisons) 

plt.plot(x, y) # Plot results with the x and y points 
plt.xlabel("n") # The x label  
plt.ylabel("Comparisons") # The y label
plt.title("Number of Comparisons for QuickSort (Modified)") # The title 
plt.show() # Show the plot 

"""
THE EXPERIMENT IS IN THE CODE BELOW THIS COMMENT 
AS DIRECTED BY THE INSTRUCTIONS FOR PSBQ1a 
"""
sys.stdout = sys.__stdout__ # Enable prints since they were directed to a dummy variable earlier 
for i in [5, 10, 20]: # Loop through the n values specified  
  A = [_ for _ in range(1, i+1)] # Initialize A[1,...,n]
  random.shuffle(A) # Shuffle A 

  p, r = 0, len(A)-1 # Left index and right index of A
  print("Shuffled array before QuickSort:", str(A) + ",","n =", i) # Array before QuickSort 
  QuickSort(A, p, r) # Call QuickSort with A, p, and r
  print("Array after QuickSort:", A, "\n") # Array after Quicksort 
