import sys

def power(x, m, c):

    if m==1:
        return x%c
    else:
        tmp=power(x,m//2,c)

        if m%2==0:
            return (tmp*tmp)%c
        else:
            return (x*tmp*tmp)%c

def main():
  
    input=sys.stdin.readline

    A,B,C=map(int,input().split())

    print(power(A,B,C))
    

if __name__ == "__main__":
    main()