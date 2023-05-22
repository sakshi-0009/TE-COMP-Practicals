# Implement depth first search algorithm

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)

        for neighbour in graph [node]:
            dfs(visited,graph,neighbour)

print("Depth first search of given graph: ")
dfs(visited,graph,'A')