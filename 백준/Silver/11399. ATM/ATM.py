import sys


def main():
    input=sys.stdin.readline

    N=int(input().strip())

    num_list=list(map(int, input().split()))

    num_list.sort()

    result=0
    temp=0

    for i in num_list:
        temp=temp+i
        result+=temp
        
    print(result)



    
if __name__ == "__main__":
    main()