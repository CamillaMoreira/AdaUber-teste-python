def detonation(bombs):
    from collections import defaultdict

    n = len(bombs)
    graph = defaultdict(list)

    for i in range(n):
        x1, y1, r1 = bombs[i]
        for j in range(n):
            if i == j:
                continue
            x2, y2, _ = bombs[j]
            if abs(x1 - x2) + abs(y1 - y2) <= r1:
                graph[i].append(j)

    def dfs(start, visited):
        visited.add(start)
        for nei in graph[start]:
            if nei not in visited:
                dfs(nei, visited)

    max_chain = 0
    for i in range(n):
        visited = set()
        dfs(i, visited)
        max_chain = max(max_chain, len(visited))

    return max_chain


print(detonation([[0, 0, 3], [2, 1, 2], [4, 1, 3], [9, 3, 2]]))  
print(detonation([[7, 5, 5], [3, 3, 1], [10, 10, 3]]))       
print(detonation([[0, 0, 99], [1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1]]))  
