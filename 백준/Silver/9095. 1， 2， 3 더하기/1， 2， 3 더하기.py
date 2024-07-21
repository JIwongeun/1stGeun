import sys

def f(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return f(n-3)+f(n-2)+f(n-1)


def main():
    
    input=sys.stdin.readline
    test=int(input().strip())



    for _ in range(test):

        num=int(input().strip())

        print(f(num))


if __name__ == "__main__":
    main()

