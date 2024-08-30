import sys
from collections import deque

MAX = 10 ** 5

def bfs(n:int, k:int):
		
    visited=[0]*(MAX+1)

    q=deque()
    
    if n==0:
        q.append(1)
    else: 
        q.append(n)

    visited[n]=0

    while q:
        
        cur=q.popleft()

        if cur==k:
            return visited[cur]
        
        for i in (cur-1, cur+1, cur*2):
            if 0<=i<=MAX and visited[i]==0:
                if i==cur*2:
                    visited[i]=visited[cur]
                    q.appendleft(i)
                else:
                    visited[i]=visited[cur]+1
                    q.append(i)

def main():

    input=sys.stdin.readline

    n, k=map(int, input().split())

    if n==0:
        if k==0:
            print(0)
        else:
            print(bfs(n,k)+1)
    else:
        print(bfs(n,k))
                
if __name__ == "__main__":
    main()

