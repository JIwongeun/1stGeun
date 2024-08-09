import sys
from collections import deque

def colorblind(screen:list, size:int):

    visited=[[0]*size for _ in range(size)]

    queue=deque()

    directions=[(0,1),(0,-1),(1,0),(-1,0)]

    result=0

    for row in range(size):
        for col in range(size):
            if visited[row][col]==0:
                queue.append((row,col))
                visited[row][col]=1
                result+=1
                while queue:
                    r, c=queue.popleft()
                    if screen[r][c]=='B':
                        for dr,dc in directions:
                            nr,nc=dr+r, dc+c
                            if 0<=nr<size and 0<=nc<size and screen[nr][nc]=='B' and visited[nr][nc]==0:
                                visited[nr][nc]=1
                                queue.append((nr,nc))
                    else:
                        for dr,dc in directions:
                            nr,nc=dr+r, dc+c
                            if 0<=nr<size and 0<=nc<size and (screen[nr][nc]=='R' or screen[nr][nc]=='G') and visited[nr][nc]==0:
                                visited[nr][nc]=1
                                queue.append((nr,nc))

    return result

def not_colorblind(screen:list, size:int):

    visited=[[0]*size for _ in range(size)]

    queue=deque()

    directions=[(0,1),(0,-1),(1,0),(-1,0)]

    result=0

    for row in range(size):
        for col in range(size):
            if visited[row][col]==0:
                queue.append((row,col))
                visited[row][col]=1
                result+=1
                while queue:
                    r, c=queue.popleft()
                    if screen[r][c]=='B':
                        for dr,dc in directions:
                            nr,nc=dr+r, dc+c
                            if 0<=nr<size and 0<=nc<size and screen[nr][nc]=='B' and visited[nr][nc]==0:
                                visited[nr][nc]=1
                                queue.append((nr,nc))
                    elif screen[r][c]=='R':
                        for dr,dc in directions:
                            nr,nc=dr+r, dc+c
                            if 0<=nr<size and 0<=nc<size and screen[nr][nc]=='R' and visited[nr][nc]==0:
                                visited[nr][nc]=1
                                queue.append((nr,nc))
                    else:
                        for dr,dc in directions:
                            nr,nc=dr+r, dc+c
                            if 0<=nr<size and 0<=nc<size and screen[nr][nc]=='G' and visited[nr][nc]==0:
                                visited[nr][nc]=1
                                queue.append((nr,nc))

    return result

def main():
    
    input=sys.stdin.readline

    size=int(input().strip())

    screen=[]

    for _ in range(size):
        screen.append(input().strip())

    print(not_colorblind(screen,size), colorblind(screen,size))
    

if __name__ == "__main__":
    main()