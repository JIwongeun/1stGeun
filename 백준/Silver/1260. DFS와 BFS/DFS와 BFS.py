import sys
from collections import deque

def dfs(graph, visit, start):

    print(start, end=' ')
    visit[start] = 1
    for next_node in sorted(graph[start]):
        if not visit[next_node]:
            dfs(graph, visit, next_node)

def bfs(graph, visit, start):

    queue = deque([start])
    visit[start] = 1
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for next_node in sorted(graph[node]):
            if not visit[next_node]:
                queue.append(next_node)
                visit[next_node] = 1

def main():

    input = sys.stdin.readline
    V, E, start = map(int, input().split())

    graph = {i: [] for i in range(1, V + 1)}

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visit = [0] * (V + 1)
    dfs(graph, visit, start)

    print()
    
    visit = [0] * (V + 1)
    bfs(graph, visit, start)

if __name__ == "__main__":
    main()