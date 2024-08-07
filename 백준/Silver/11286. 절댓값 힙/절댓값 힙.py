import sys
import heapq

def main():
    input = sys.stdin.readline

    N=int(input().strip())

    heap=[]

    for _ in range(N):
        num=int(input().strip())

        if num!=0:
            heapq.heappush(heap, (abs(num), num))
        
        else:
            if heap:
                print(heapq.heappop(heap)[1])
            else:
                print(0)
    
if __name__ == "__main__":
    main()