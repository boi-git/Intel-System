# Using a Python dictionary to act as an adjacency list
graph = {
    '4' : ['1','2'],
    '1' : ['5', '3'],
    '2' : [],
    '5' : [],
    '3' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, '4')