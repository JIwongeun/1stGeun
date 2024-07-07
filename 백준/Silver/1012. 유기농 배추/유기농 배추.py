import sys
from collections import deque

def main():
    input = sys.stdin.readline

    T = int(input().strip())

    for _ in range(T):
        rows, cols, napa_cnt = map(int, input().split())
        ground = []
        visit = []
        for _ in range(rows):
            ground.append([0 for _ in range(cols)])
            visit.append([0 for _ in range(cols)])

        for _ in range(napa_cnt):
            row, col = map(int, input().split())
            ground[row][col] = 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        earthworm = 0

        for row in range(rows):
            for col in range(cols):
                if visit[row][col] == 0 and ground[row][col] == 1:
                    queue = deque()
                    queue.append((row, col))
                    visit[row][col] = 1
                    while queue:
                        current_row, current_col = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = current_row + dr, current_col + dc
                            if 0 <= nr < rows and 0 <= nc < cols and ground[nr][nc] == 1 and visit[nr][nc] == 0:
                                visit[nr][nc] = 1
                                queue.append((nr, nc))
                    earthworm += 1
        
        print(earthworm)

if __name__ == "__main__":
    main()


