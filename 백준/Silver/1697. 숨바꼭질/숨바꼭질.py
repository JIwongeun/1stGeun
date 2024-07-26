import sys
from collections import deque

MAX = 10 ** 5

def bfs(n:int, k:int, visited:list):
    q=deque()
    q.append(n)
    
    while q:
        cur=q.popleft()
        if cur==k:
            return visited[cur]
        for i in (cur-1, cur+1, cur*2):
            if 0<=i<=MAX and not visited[i]:
                visited[i]=visited[cur]+1
                q.append(i)

def main():

    input=sys.stdin.readline

    n,k=map(int, input().split())
    
    visited = [0] * (MAX + 1)

    print(bfs(n,k, visited))
                
if __name__ == "__main__":
    main()