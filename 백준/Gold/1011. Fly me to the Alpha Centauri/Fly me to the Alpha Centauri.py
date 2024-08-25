import sys
from collections import deque

def main():
  
    input=sys.stdin.readline

    T = int(input().strip())

    for _ in range(T):
        x, y = map(int, input().split())
        
        distance = y - x 
        tmp = 0 
        cnt = 0 
        moving = 0 

        while tmp < distance:
            cnt += 1
            if cnt % 2 != 0:
                moving += 1
            tmp += moving
        print(cnt)
    

if __name__ == "__main__":
    main()
