import sys

def DFS(start, n, m, s):
    
    if len(s)==m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n+1):
    
        s.append(i)
        DFS(i, n, m, s)
        s.pop()

def main():
    input = sys.stdin.readline

    N, M = list(map(int, input().rstrip().split()))
    
    s=[]

    DFS(1, N, M, s)
    
if __name__ == "__main__":
    main()