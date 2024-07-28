import sys
from collections import deque

def main():
    input = sys.stdin.readline

    row, col = map(int, input().split())

    Map = []
    result = [[-1] * col for _ in range(row)]
    visited = [[0] * col for _ in range(row)]
    
    start = None
    for r in range(row):
        temp = list(map(int, input().split()))
        if 2 in temp:
            start = (r, temp.index(2))
        Map.append(temp)
    
    if start is None:
        return
    
    result[start[0]][start[1]] = 0
    visited[start[0]][start[1]] = 1

    q = deque([start])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        loc_r, loc_c = q.popleft()
        current_dist = result[loc_r][loc_c]

        for dr, dc in directions:
            Nr = loc_r + dr
            Nc = loc_c + dc
            if 0 <= Nr < row and 0 <= Nc < col and Map[Nr][Nc] == 1 and visited[Nr][Nc] == 0:
                result[Nr][Nc] = current_dist + 1
                q.append((Nr, Nc))
                visited[Nr][Nc] = 1
    
    for r in range(row):
        for c in range(col):
            if Map[r][c] == 0:
                result[r][c] = 0

    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()