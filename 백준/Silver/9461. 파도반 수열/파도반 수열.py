import sys

def padoban_sequence(n, dp):

    if dp[n]:
        return dp[n]
    else:
        dp[n]=padoban_sequence(n-2, dp)+padoban_sequence(n-3,dp)
        return dp[n]

def main():  

    input=sys.stdin.readline

    test=int(input().strip())

    padoban=[0,1,1,1]+[0 for i in range(97)]

    for _ in range(test):
     
        N=int(input().strip())

        print(padoban_sequence(N, padoban))

if __name__ == "__main__":
    main()