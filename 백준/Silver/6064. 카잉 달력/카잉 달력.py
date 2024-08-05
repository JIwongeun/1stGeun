import sys

def kaing(M,N,x,y):

    while x<=M*N:
        if (x-y)%N==0:
            return x
        x+=M
    return -1


def main():
    input = sys.stdin.readline

    T=int(input().strip())

    for _ in range(T):
        M,N,x,y=map(int, input().split())
        print(kaing(M,N,x,y))
    

if __name__ == "__main__":
    main()