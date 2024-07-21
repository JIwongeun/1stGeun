import sys


def main():
    
    input=sys.stdin.readline
    size=int(input().strip())

    tile_cnt=[0, 1, 3]

    for i in range(3, size+1):
    
        tile_cnt.append(tile_cnt[i-1]+2*tile_cnt[i-2])
       
    print(tile_cnt[size]%10007)


if __name__ == "__main__":
    main()