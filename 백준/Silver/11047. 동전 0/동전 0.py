import sys


def main():
    input=sys.stdin.readline

    N,K=map(int, input().split())

    coin_list=[]

    for _ in range(N):
        coin_list.append(int(input().strip()))

    coin_list.reverse()

    coin_cnt=0

    for coin in coin_list:
        if K//coin!=0:
            coin_cnt+=K//coin
            K%=coin
    
    print(coin_cnt)



    
if __name__ == "__main__":
    main()
