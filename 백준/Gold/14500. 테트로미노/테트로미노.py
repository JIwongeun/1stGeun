import sys

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

maximum = 0

def DFS(r, c, temp, count, rows, cols, visited, board):
    global maximum
    if count == 4:
        maximum = max(maximum, temp)
        return

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            DFS(nr, nc, temp + board[nr][nc], count + 1, rows, cols, visited, board)
            visited[nr][nc] = 0

def FY(r, c, rows, cols, board):
    global maximum
    temp = board[r][c]
    arr = []

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            arr.append((board[nr][nc]))
        
    if len(arr) == 4:
        arr.sort(reverse=True)
        arr.pop()
        maximum = max(maximum, sum(arr) + board[r][c])
    
    elif len(arr) == 3:
        maximum = max(maximum, sum(arr) + board[r][c])

    return

def main():
    input = sys.stdin.readline
    N, M = map(int, input().rstrip().split())
    
    global maximum
    maximum = 0
    
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            visited[i][j] = 1
            DFS(i, j, board[i][j], 1, N, M, visited, board)
            FY(i, j, N, M, board)
            visited[i][j] = 0

    print(maximum)

if __name__ == "__main__":
    main()
