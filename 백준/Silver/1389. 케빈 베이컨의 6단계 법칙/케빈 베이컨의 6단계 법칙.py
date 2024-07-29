import sys
from collections import deque
import math

def bfs(start:int, n:int, graph:dict):

    visited=[0]*(n+1)
    visited[0]=1

    q=deque([start])
    visited[start]=1

    cnt=0
    result=0

    while q:
        cnt+=1
        for _ in range(len(q)):
            u=q.popleft()
            for v in graph[u]:
                if not visited[v]:
                    q.append(v)
                    visited[v]=1
                    result+=cnt

    return result


def main():
    input = sys.stdin.readline

    n, e = map(int, input().split())

    graph={i : [] for i in range(1,n+1)}

    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    temp=math.inf

    for i in range(1,n+1):
        min_=bfs(i, n, graph)
        if temp>min_:
            temp=min_
            result=i

    print(result)

if __name__ == "__main__":
    main()
