import sys


def zfs(n,r,c):

    if n==0:
        return 0
    
    half = 2 ** (n - 1)

    if r < half and c < half:
        # 1사분면
        return zfs(n - 1, r, c)
    elif r < half and c >= half:
        # 2사분면
        return half * half + zfs(n - 1, r, c - half)
    elif r >= half and c < half:
        # 3사분면
        return 2 * half * half + zfs(n - 1, r - half, c)
    else:
        # 4사분면
        return 3 * half * half + zfs(n - 1, r - half, c - half)



def main():
    
    input=sys.stdin.readline


    N,r,c=map(int, input().split())


    print(zfs(N,r,c))



if __name__=="__main__":
    main()