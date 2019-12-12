# Python imports 
import random 
import copy

def QuickSort(Bottles, Caps, p, r): 
  """
  Performs quick sort on the Bottles and Caps using Caps[r] as a 
  pivot for Bottles and Bottles[r] as a pivot for Caps on each 
  recursive call. Then, finding matching Bottles and Caps will 
  be trivial since both arrays will be sorted. 
  
  :param Bottles: (Required) The bottles array 
  :param Caps: (Required) The caps array 
  :param p: (Required) The leftmost index of the 
            array or sub-array 
  :param r: (Required) The rightmost index of the 
            array or sub-array
  :returns Bottles: The sorted Bottles array 
  :returns Caps: The sorted Caps array 
  """ 
  if(p < r): 
    # Partition Bottles using Caps[r] as pivot
    # Partition Caps using Bottles[q] as pivot 
    q_Caps = Caps[r] 
    q = Partition(Bottles, p, q_Caps, r)
    q_Bottles = Bottles[q]
    Partition(Caps, p, q_Bottles, r)
    # Recurse left   
    QuickSort(Bottles, Caps, p, q-1)
    # Recurse right 
    QuickSort(Bottles, Caps, q+1, r)
  return Bottles, Caps

def Partition(A, p, q, r): 
  """
  Performs the partition algorithm for Bottles and Caps using 
  a pivot from the opposite array, respectively. 
  
  :param A: (Required) The bottles or caps array to be partitioned 
  :param p: (Required) The leftmost index of the 
            array or sub-array 
  :param q: (Required) The pivot (either Caps[r] or Bottles[r], respectively) 
  :param r: (Required) The rightmost index of the 
            array or sub-array
  :returns i+1: Returns the index to be used in the 
                two recursive Quicksort calls 
  """ 
  # The pivot that was passed in as a parameter 
  x = q 
  # Init i 
  i = p-1
  # Loop through for sub-array or array A[p..r]
  for j in range(p, r): 
    # If pivot equals a value A[j] in A[p..r], swap with A[r]
    if(A[j] == x): 
      A[j], A[r] = A[r], A[j]
    # If value is less than or equal to pivot, increment i and swap(A[j], A[i])
    if(A[j] <= x):
      i = i + 1
      A[j], A[i] = A[i], A[j]
  # Swap A[i+1] and A[r]
  A[i+1], A[r] = A[r], A[i+1]
  return i + 1

Bottles = [i for i in range(1, 100+1)]
random.shuffle(Bottles)
testB = copy.deepcopy(Bottles)

Caps = [i for i in range(1, 100+1)]
random.shuffle(Caps)
testC = copy.deepcopy(Caps)

p, r = 0, len(Bottles + Caps)//2

B, C = QuickSort(Bottles, Caps, p, r-1)


""" 
Test Code - These correctly sorted lists will be
compared with the sorted arrays from the QuickSort 
that I implemented. 
""" 
testB.sort()
testC.sort()

# *** BEGIN TESTS ***
# Check to see if Bottles, Caps are both sorted 
if(B == C == testB == testC):
  print("The two lists, Bottles and Caps, are now sorted and thus have trivial matches.")
else:
  print("The algorithm is incorrect, the two lists are not sorted.")
# *** END TESTS ***