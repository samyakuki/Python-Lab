graph = {'A':{'B', 'C'},'B':{'D'},'C': {'E'},'D': {'E'},'E':set()}

def dfs(graph, key, visited = []) -> list:
    visited.append(key)
    for i in graph[key]:
        if i not in visited:
            dfs(graph, i, visited)
    return visited
visited = []
print(dfs(graph,'A', visited))