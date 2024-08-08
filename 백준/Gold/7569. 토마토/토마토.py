import sys
from collections import deque

def main():
    input = sys.stdin.readline

    cols, rows, heights=map(int,input().split())

    boxes=[]
    

    for _ in range(heights):
        box=[]
       
        for _ in range(rows):
            box.append(list(map(int, input().split())))
            
        boxes.append(box)
       


    queue=deque()

    for h in range(heights):
        for r in range(rows):
            for c in range(cols):
                if boxes[h][r][c]==1:
                    queue.append((h,r,c))

    directions=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

    days=-1

    while queue:
        for _ in range(len(queue)):
            height, row, col = queue.popleft()

            for dh, dr, dc in directions:
                nh=height+dh
                nr=row+dr
                nc=col+dc

                if 0<=nh<heights and 0<=nr<rows and 0<=nc<cols and boxes[nh][nr][nc]==0:
                    boxes[nh][nr][nc]=1
                    queue.append((nh,nr,nc))
        days+=1

    for box in boxes:
        for row in box:
            if 0 in row:
                print(-1)
                return
            
    if days==-1:
        print(0)
    else:
        print(days)

if __name__ == "__main__":
    main()