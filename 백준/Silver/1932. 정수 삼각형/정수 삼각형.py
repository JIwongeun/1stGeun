import sys


def main():
    input = sys.stdin.readline

    N=int(input().strip())

    tree=[list(map(int, input().split())) for _ in range(N)]
    dp=[[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(len(tree[i])):
            if len(tree[i])==1:
                dp[i][j]=tree[i][j]
            else:
                if j==0:
                    dp[i][j]=tree[i][j]+dp[i-1][j]
                elif j==len(tree[i])-1:
                    dp[i][j]=tree[i][j]+dp[i-1][j-1]
                else:
                    dp[i][j]=tree[i][j]+max(dp[i-1][j-1], dp[i-1][j])
    
   
    print(max(dp[N-1]))

if __name__ == "__main__":
    main()
