import sys

def main():
  
    input=sys.stdin.readline

    T=int(input().strip())

    RGB_cost=[list(map(int, input().split())) for _ in range(T)]

    dp=[[0,0,0] for _ in range(T)]

    dp[0]=RGB_cost[0].copy()

    for i in range(1, T):
        dp[i][0]=RGB_cost[i][0]+min(dp[i-1][1], dp[i-1][2])
        dp[i][1]=RGB_cost[i][1]+min(dp[i-1][0], dp[i-1][2])
        dp[i][2]=RGB_cost[i][2]+min(dp[i-1][1], dp[i-1][0])

    print(min(dp[T-1]))

if __name__ == "__main__":
    main()