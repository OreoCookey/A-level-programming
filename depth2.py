#The graph to treverse
graph = {
		
		"H": ["I", "G"],
		"I": ["H", "D"],
		"E": ["D"],
		"D": ["I", "F", "C", "E"],
		"F": ["D", "G"],
		"G": ["F", "C"],
		"C": ["D", "G", "A"],
		"A": ["C", "B"],
		"B": ["A"]
}


visited = []
start_node = "B"



def visitNextNode(node, gph):
	#all of the nodes connected to the current node
	possible_nodes = gph[node]

	#add the current node to a list of visited nodes
	visited.append(node)

	#if nodes connected to the current node have not being visited 
	#and are yet to be added to the stack, visit the nodes connected to i
	for i in possible_nodes:
		if i not in visited:
			visitNextNode(i, gph)

	


visitNextNode(start_node, graph)
print("Visited all")
print("Visited nodes:" + str(visited))

		








