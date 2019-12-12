def DFS(G, i, j): 
 	# Check for out of bounds 
	if(i < 0 or i >= len(G)):
		return 0 
	# Check for out of bounds 
	elif(j < 0 or j >= len(G[i])):
		return 0
	# We know we only want 0's 
	elif(G[i][j] != 0):
		return 0
	# True evaluates to 1, AKA: count as land (visited)
	G[i][j] = True
	# Call DFS recursively, checking all valid neighbors 
	return 1 + DFS(G, i+1, j) + DFS(G, i-1, j) + DFS(G, i, j+1) \
			 + DFS(G, i, j-1) + DFS(G, i+1, j+1) \
			 + DFS(G, i+1, j-1) + DFS(G, i-1, j+1) \
			 + DFS(G, i-1, j-1)
# Substitute for any 2D array here
G = [[0,2,1,0], 
	 [0,1,0,1], 
	 [1,1,0,1], 
	 [0,1,0,1]]
Lakes = []
for i in range(len(G)): 
	for j in range(len(G[i])):
		if(G[i][j] == 0): 
			Lakes.append(DFS(G, i, j)), Lakes.sort()
print(*[lake for lake in Lakes], sep=', ')
