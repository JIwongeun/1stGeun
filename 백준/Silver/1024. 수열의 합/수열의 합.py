import sys

def main():
    input = sys.stdin.readline
    N, L = map(int, input().split())

    for i in range(L, 101):
        num = N - (i * (i + 1) // 2)
        
        if num % i == 0:
            x = num // i
            if x >= -1: 
                print(*(x + j + 1 for j in range(i)))
                return
    
   
    print(-1)

if __name__ == "__main__":
    main()
