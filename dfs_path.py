def dfsUtil(cur, nodes, adj, visited, road_used, parent):
	c = 0

	for node in nodes:
		if (visited[node]):
			c += 1
 
	if (c == len(nodes)):
		return
 
	visited[cur] = True
 
	road_used.append([parent, cur])
 
	for x in adj[cur]:
		if not visited[x]:
			dfsUtil(x, nodes, adj, visited, road_used, cur)
 
	for y in road_used:
		if (y[1] == cur):
			dfsUtil(y[0], nodes, adj, visited, road_used, cur)

def dfs(start, nodes, adj):
	visited = {p:False for p in nodes}
	road_used = []
 
	dfsUtil(start, nodes, adj, visited, road_used, None)

	return road_used