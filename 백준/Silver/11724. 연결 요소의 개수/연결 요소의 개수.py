import sys

def dfs(start:int, visited:list, graph:list):

    stack=[]
    stack.append(start)

    while stack:
        node=stack.pop()
        if visited[node]==0:
            visited[node]=1
            for v in graph[node]:
                if visited[v]==0:
                    stack.append(v)


def main():
    
    input=sys.stdin.readline

    N,M=map(int,input().split())

    graph = {i: [] for i in range(1, N+1)}

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)


    visited=[0]*(N+1)
    visited[0]=1

    con_comp=0
    
    for i in range(len(visited)):
        if visited[i]==0:
            con_comp+=1
            dfs(i, visited, graph)

    print(con_comp)

if __name__=="__main__":
    main()