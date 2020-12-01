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
stack = []
start_node = "B"



def visitNextNode(node, gph):
	#all of the nodes connected to the current node
	possible_nodes = gph[node]

	#add the current node to a list of visited nodes
	visited.append(node)

	#if nodes connected to the current node have not being visited 
	#and are yet to be added to the stack, add them to the stack
	for i in possible_nodes:
		if not i in visited and not i in stack:
			stack.append(i)

	#while there are still nodes to visit in the stack,
	#pop the latest element and visit it
	if len(stack) > 0:
		n = stack.pop()
		visitNextNode(n, gph)

	#if there are no elements left than all the nodes have being visited
	else: 
		print("Visited all")
		print("Visited nodes:" + str(visited))


visitNextNode(start_node, graph)

		








