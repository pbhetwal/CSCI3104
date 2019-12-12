# Author: Aric Hagberg (hagberg@lanl.gov)

#    Copyright (C) 2004-2019 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.

#    Modified by Shivendra Agrawal
import random
import re
import matplotlib.pyplot as plt
import networkx as nx

## DO NOT MODIFY THE CODE WITHIN THIS BLOCK ########################################

def miles_graph():
	""" Return the cites example graph in miles_dat.txt
		from the Stanford GraphBase.
	"""
	# open file miles_dat.txt.gz (or miles_dat.txt)
	import gzip
	fh = gzip.open('miles_dat.txt.gz', 'r')

	G = nx.Graph()
	G.position = {}
	G.population = {}

	cities = []
	for line in fh.readlines():
		line = line.decode()
		if line.startswith("*"):  # skip comments
			continue

		numfind = re.compile("^\d+")

		if numfind.match(line):  # this line is distances
			dist = line.split()
			for d in dist:
				G.add_edge(city, cities[i], weight=int(d))
				i = i + 1
		else:  # this line is a city, position, population
			i = 1
			(city, coordpop) = line.split("[")
			cities.insert(0, city)
			(coord, pop) = coordpop.split("]")
			(y, x) = coord.split(",")

			G.add_node(city)
			# assign position - flip x axis for matplotlib, shift origin
			G.position[city] = (-int(x) + 7500, int(y) - 3000)
			G.population[city] = float(pop) / 1000.0
	return G


def draw_graph(G, kruskal_selected_edges, sorted_edges):
	'''
	Plots the networkx graph with MST selected by Kruskal's as overlay

	:param G: Networkx graph
	:param kruskal_selected_edges: List of edge tuple
	:return: None
	'''
	pos = G.position  # positions for all nodes
	# nodes
	nx.draw_networkx_nodes(G, pos, node_size=10)
	title = ""

	if len(kruskal_selected_edges) > 0:
		non_MST_edges = [edge for edge in sorted_edges if edge not in kruskal_selected_edges]
		
		print("\nNumber of edges selected by Kruskal's = ", len(kruskal_selected_edges))

		nx.draw_networkx_edges(G, pos, edgelist=non_MST_edges,
							   width=0.5, alpha=0.5, edge_color='b')
		nx.draw_networkx_edges(G, pos,
							   edgelist=kruskal_selected_edges, width=1, edge_color='r')
		title = ", Edges in the MST = " + str(len(kruskal_selected_edges))
	else:
		nx.draw_networkx_edges(G, pos, edgelist=sorted_edges,
							   width=1, alpha=0.5, edge_color='b')
	plt.title("Threshold = " + str(EDGE_SELECTION_CRITERIA) + title)
	plt.savefig('MST.png')
	plt.show()


def find(vertex):
	'''
	Function that returns the leader vertex for any 'vertex'
	'''
	return leader_dict[vertex]

####################################################################################


def union(A,B):
	'''
	Function that unifies two components into one 
	'''
	# If A has more components than B, B's components are added to A's 
	# This ensures less leader updates 
	if(len(components[A]) >= len(components[B])):
		components[A] += components[B] 
		for vertex in components[B]:
			leader_dict[vertex] = leader_dict[A]
		del components[B]

	# If B has more components than A, A's components are added to B's 
	# This ensures less leader updates
	elif(len(components[B]) >= len(components[A])):
		components[B] += components[A]
		for vertex in components[A]:
			leader_dict[vertex] = leader_dict[B]
		del components[A]

	return 


if __name__ == '__main__':
	########## DO NOT MODIFY THE CODE IN THIS BLOCK ################################

	EDGE_SELECTION_CRITERIA = random.choice([500 + (i+1)*20 for i in range(4)])

	G = miles_graph()

	print("Loaded miles_dat.txt containing 128 cities.")
	print("digraph has %d nodes with %d edges"
		  % (nx.number_of_nodes(G), nx.number_of_edges(G)))


	edges_to_consider = [(u, v, d) for (u, v, d) in G.edges(data=True)
						 if d['weight'] <= EDGE_SELECTION_CRITERIA]
	sorted_edges = [(u, v) for (u, v, d) in sorted(edges_to_consider,
												   key=lambda x:x[2]['weight'])]
	vertices = []
	for u, v in sorted_edges:
		vertices.append(u)
		vertices.append(v)
	vertices = list(set(vertices))

	print("Edges considered (in ascending order) for this graph = ", len(sorted_edges))

	# A dictionary that has key as edge (u, v) and value as the length of the edge
	length_of_edge = {(u,v):d for (u, v, d) in edges_to_consider}

	# 'Find' function can be easily emulated via dict and
	# initially all vertices form their own component and point to just themselves
	# 'leader_dict' has key as vertex and value as it's leader vertex
	leader_dict = {v : v for v in vertices}

	# 'components' have key as the leader vertex and
	# value as a list of vertices that are in that component
	# Initially all the vertices form their own components
	components = {find(v) : [v] for v in vertices}

	kruskal_selected_edges = []
	################################################################################

	# Write your code below to populate the 'kruskal_selected_edges' list
	# with the edges in the MST using the Kruskal's algorithm

	# Note that after the union call, you need to merge the components and
	# update the relevant leaders in 'leader_dict' otherwise find() won't work as expected

	# Your solution can start after this comment. You should also finish the 'union()' function and
	# you are allowed to change the signature of the union function


	'''
	********** IMPORTANT: Variable below is used for 1.c **********
	'''
	# Change k from 2..10 to find spacing values 
	k = 10
	'''
	********** IMPORTANT: Variable above is used for 1.c **********
	'''

	# This is a counter to see when we stop our iterations k before completion 
	edges_added = 0
	# Loop through sorted edges
	for edge in sorted_edges: 
		# Get vertices from edges
		u,v = edge
		# If the vertices are not in the same component 
		if(find(u) != find(v)):
			# Check to see if we should have stopped k iterations before completion  
			if(edges_added == len(vertices)-1-k): 
				# That edge added would be the spacing 
				getWeight = length_of_edge[edge]
				# Save our spacing value 
				spacing = getWeight['weight']
			# Union the two vertices
			union(find(u), find(v))
			# Add the corresponding edge 
			kruskal_selected_edges.append(edge)
			# Increment the edges added
			edges_added += 1

	# Do not remove this line, it will save the MST as a figure for you
	draw_graph(G, kruskal_selected_edges, sorted_edges)

	# This will print after the figure from draw_graph(...) is closed 
	print("Spacing for when k = " + str(k)+ ": "+ str(spacing))