import sys

def main():  
    input = sys.stdin.readline
    N,M = map(int,input().split())

    
    num_list=list(map(int,input().split()))

    dp=[0]*(N+1)

    for i in range(1, N+1):
        dp[i]=dp[i-1]+num_list[i-1]

    for _ in range(M):
        i,j=map(int,input().split())
        result=dp[j]-dp[i-1]
        print(result)

if __name__ == "__main__":
    main()