import sys

def main():
    input = sys.stdin.readline

    
    
    N = int(input())
    arr = list(map(int,input().split()))
    
    l,r,count = 0,0,0
    
    answer = 0

    infos={i : 0 for i in range(1, 10)}

    while r<N:
        if infos[arr[r]] == 0:
            count += 1
        infos[arr[r]] += 1
    
        while count > 2:
            infos[arr[l]] -= 1
            if infos[arr[l]] == 0:
                count -= 1
            l += 1
    
        answer = max(answer,r-l+1)
        r += 1
        
    
    print(answer)

if __name__ == "__main__":
    main()