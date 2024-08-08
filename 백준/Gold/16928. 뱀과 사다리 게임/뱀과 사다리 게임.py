import sys
from collections import deque

def bfs(graph:dict):

    visited=[0]*101
    visited[0]=1

    queue=deque([(1, 0)])
    visited[1]=1

    while queue:
        u, count=queue.popleft()

        if u==100:
            return count
        
        for v in range(u+1, u+7):
            if v <= 100:
                next_pos = graph.get(v, v)
                if not visited[next_pos]:
                    visited[next_pos] = 1
                    queue.append((next_pos, count + 1))


def main():
    
    input=sys.stdin.readline

    N, M=map(int,input().split())

    graph={i : i for i in range(1,101)}

    for _ in range(N):
        u,v=map(int,input().split())
        graph[u]=v

    for _ in range(M):
        u,v=map(int,input().split())
        graph[u]=v

    print(bfs(graph))
          

if __name__ == "__main__":
    main()