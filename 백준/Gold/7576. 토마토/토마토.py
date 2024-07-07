import sys
from collections import deque

def main():
    input = sys.stdin.readline
    cols, rows = map(int, input().split())

    box = []
    for _ in range(rows):
        row = [int(x) for x in input().split()]
        box.append(row)

    
    queue = deque()
    for row in range(rows):
        for col in range(cols):
            if box[row][col] == 1:
                queue.append((row, col))
    

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    days = -1
    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and box[nr][nc] == 0:
                    box[nr][nc] = 1
                    queue.append((nr, nc))
        days += 1
    
    for row in box:
        if 0 in row:
            print(-1)
            return
    
    if days == -1:
        print(0)
    else:
        print(days)

if __name__ == "__main__":
    main()