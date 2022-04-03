# https://www.acmicpc.net/problem/2606

computer_num = int(input())
network = int(input())
graph = [[]for _ in range(computer_num+1)]
visited = [False] * (computer_num+1)

for _ in range(network):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

            
dfs(graph, 1, visited)

print(visited.count(True)-1)
