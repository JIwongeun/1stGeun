import sys

def dfs(row, n, columns, diag1, diag2):
    if row == n:
        return 1
    
    count = 0
    for col in range(n):
        if columns[col] or diag1[row + col] or diag2[row - col + n - 1]:
            continue
        
        # 현재 열, 대각선을 사용 중으로 표시
        columns[col] = diag1[row + col] = diag2[row - col + n - 1] = True
        
        count += dfs(row + 1, n, columns, diag1, diag2)
        
        # 되돌리기
        columns[col] = diag1[row + col] = diag2[row - col + n - 1] = False
    
    return count

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    
    # 각 열과 대각선의 사용 여부를 나타내는 배열
    columns = [False] * N
    diag1 = [False] * (2 * N - 1)  # / 방향 대각선
    diag2 = [False] * (2 * N - 1)  # \ 방향 대각선
    
    result = dfs(0, N, columns, diag1, diag2)
    
    print(result)

if __name__ == "__main__":
    main()
