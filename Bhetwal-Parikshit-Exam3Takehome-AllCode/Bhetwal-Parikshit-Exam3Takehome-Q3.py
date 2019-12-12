# Python imports 
import random

def EPIC(Cards, p, r):
  """
  This function calculates the sum of player 1's hand 
  at the end of a game of EPIC! given that the size of 
  the cards is even. This is NOT a greedy algorithm. 
  
  :param Cards: (Required) The array of cards 
  :param p: (Required) The leftmost index of the 
        array or sub-array 
  :param r: (Required) The rightmost index of the 
            array or sub-array 
  :returns M[p][r]: The sum of player 1's hand

  NOTE: SHIV SAID IT WAS OKAY TO SOLVE THIS 
  PROBLEM USING TOP-DOWN WITH MEMOIZATION.
  """
  # Points matrix 
  global M 
  # One card remaining
  # (This is only for completness)
  # (This won't happen if even sized array) 
  if(p == r):
    return Cards[p]
  # Two cards remaining 
  # Can be written as: p == r - 1
  elif(p + 1 == r):
    return min(Cards[p], Cards[r])
  # More than two cards remaining 
  elif(M[p][r] == None):
    # Player 2 picks p+1 card when player 1 picks p card 
    if(Cards[p+1] < Cards[r]):
      frontend = Cards[p] + EPIC(Cards, p+2, r)
    # Player 2 picks r card when player 1 picks p card 
    else:
      frontend = Cards[p] + EPIC(Cards, p+1, r-1)

    # Player 2 picks p card when player 1 picks r card 
    if(Cards[p] < Cards[r-1]): 
      backend = Cards[r] + EPIC(Cards, p+1, r-1)
    # Player 2 picks r-1 card when player 1 picks r card 
    else:
      backend = Cards[r] + EPIC(Cards, p, r-2)
    
    # Take the minimum from the possible recursive calls 
    M[p][r] = min(frontend, backend)
  return M[p][r]

def Driver(Cards):
  """
  This function prints the cards that a single 
  game of EPIC! is using and the sum of the hands 
  of the two players at the end of that game. 
  
  :param Cards: (Required) The array of cards 
  :returns None: Nothing is returned 
  """ 
  global M
  n = len(Cards)
  M = [[None for _ in range(n)] for _ in range(n)]

  print("BEGIN EPIC!\n")

  print("CARDS =", *Cards)
  player1 = EPIC(Cards, 0, n-1)
  print("Sum of player 1's hand:", player1)
  player2 = sum(Cards)-player1
  print("Sum of player 2's hand:", player2) 

  if(player1 < player2):
    print("Player 1 won!")
  elif(player2 < player1):
    print("Player 2 won!")
  else:
    print("The game was a tie")

  print("\nEND EPIC!\n")

"""
SIMULATION 
"""
# Guarantee that deck size is always even 
# When deck size is even, player 1 always wins
sample_size = 1
while(sample_size % 2 != 0):
  sample_size = random.randint(1, 100)
# Randomly generate deck of cards from sample size
Cards = random.sample(range(1,101), sample_size)
# Run EPIC!
Driver(Cards)
"""
SIMULATION 
"""


"""
TESTS
# Test Case from write-up 
Driver([4, 2, 6, 5])

# More Test Cases 
Driver([35, 83, 47, 37, 90, 10, 13, 2, 96, 50, 93, 36, 64, 95])
"""
