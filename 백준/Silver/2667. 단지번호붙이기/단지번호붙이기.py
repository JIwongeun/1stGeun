import sys
from collections import deque

def main():
    input = sys.stdin.readline

    N = int(input().strip())

    MAP=[input().strip() for _ in range(N)] 
    visited=[[0]*N for _ in range(N)]

    apartment_number=0

    q=deque()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result=[]

    for row in range(N):
        for col in range(N):
            
            if MAP[row][col] == '1' and not visited[row][col]:
                apartment_number+=1
                visited[row][col]=apartment_number
                q.append((row, col))
                cnt=0
                while q:
                    r, c=q.popleft()
                    cnt+=1
                    for dr,dc in directions:
                        nr=r+dr
                        nc=c+dc
                        if 0<=nr<N and 0<=nc<N and MAP[nr][nc]=='1' and visited[nr][nc]==0:
                            visited[nr][nc]=1
                            q.append((nr,nc))
                result.append(cnt)   

    print(apartment_number)
    result.sort()
    for i in result:
        print(i)

if __name__ == "__main__":
    main()