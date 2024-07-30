from collections import deque
import sys

def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    miro = [input().strip() for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    
    queue = deque([(0, 0)])
    visited[0][0] = 1

    direction = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    while queue:
        row, col = queue.popleft()
        
        if row == n-1 and col == m-1:
            print(visited[row][col])
            return

        for dr, dc in direction:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < m and miro[nr][nc] == '1' and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = visited[row][col] + 1

if __name__ == "__main__":
    main()