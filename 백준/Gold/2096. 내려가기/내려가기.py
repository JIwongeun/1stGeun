import sys
input = sys.stdin.readline

def main():

    N=int(input().strip())

    num=list(map(int, input().split()))

    dp_max=num
    dp_min=num

    for _ in range(N-1):
        num=list(map(int, input().split()))

        dp_max=[num[0]+max(dp_max[0], dp_max[1]),num[1]+max(dp_max[0], dp_max[1], dp_max[2]),num[2]+max(dp_max[1], dp_max[2])]
        dp_min=[num[0]+min(dp_min[0], dp_min[1]),num[1]+min(dp_min[0], dp_min[1], dp_min[2]),num[2]+min(dp_min[1], dp_min[2])]

    print(max(dp_max), min(dp_min))
    
if __name__ == "__main__":
    main()