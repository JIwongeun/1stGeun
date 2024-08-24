import sys
from collections import deque

def main():
  
    input=sys.stdin.readline

    n,m=map(int,input().split())

    board=[list(map(int, input().split())) for _ in range(n)]

    queue=deque(tuple(map(int,input().split())) for _ in range(m))

    dp=[[0]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j]=board[i-1][j-1]+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]

    while queue:

        x1,y1,x2,y2=queue.popleft()

        result=dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
        print(result)
    

if __name__ == "__main__":
    main()
