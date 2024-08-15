import sys

def fac(n:int):

    num=1

    for i in range(1,n+1):
        num*=i

    return num


def main():
    input = sys.stdin.readline

    N=int(input().strip())

    for _ in range(N):
        n,m=map(int, input().split())
        count=fac(m)//(fac(n)*fac(m-n))
    
        print(count)


if __name__ == "__main__":
    main()