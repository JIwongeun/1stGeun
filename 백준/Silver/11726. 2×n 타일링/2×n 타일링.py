import sys

def main():
    
    input = sys.stdin.readline

    N = int(input())
    tile_cnt=[0,1,2]

    for i in range(3,N+1):
        tile_cnt.append(tile_cnt[i-1]+tile_cnt[i-2])

    print(tile_cnt[N]%10007)

    
if __name__ == "__main__":
    main()
