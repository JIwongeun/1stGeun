import sys

def dfs(graph, visit, start):

    visit[start] = 1
    for next_node in sorted(graph[start]):
        if not visit[next_node]:
            dfs(graph, visit, next_node)

def main():

    input = sys.stdin.readline
    V=int(input().strip())
    E=int(input().strip())

    graph = {i: [] for i in range(1, V + 1)}

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visit = [0] * (V + 1)
    dfs(graph, visit, 1)

    print(visit.count(1)-1)
    
    

if __name__ == "__main__":
    main()