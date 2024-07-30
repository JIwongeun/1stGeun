from collections import deque
import sys

def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    campus = [input().strip() for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    
    for i in range(len(campus)):
        if 'I' in campus[i]:
            start=(i, campus[i].index('I'))
            
    queue = deque([start])
    visited[start[0]][start[1]] = 1

    direction = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    result=0

    while queue:

        row, col = queue.popleft()
        
        if campus[row][col]=='P':
            result+=1

        for dr, dc in direction:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < m and (campus[nr][nc] == 'O' or campus[nr][nc] == 'P') and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = 1

    if not result:
        print("TT")
    else:
        print(result)

if __name__ == "__main__":
    main()