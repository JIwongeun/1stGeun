import sys
import heapq

def main():
    
    input=sys.stdin.readline

    T=int(input().strip())

    for _ in range(T):

        N=int(input().strip())

        min_heap=[]
        max_heap=[]
        visited=[0]*N
        

        for i in range(N):

            op, num=map(str, input().split())
            num=int(num)

            if op=='I':
                heapq.heappush(min_heap, (num, i))
                heapq.heappush(max_heap, (-num, i))
                visited[i]=1

            else:
                if num==-1:
                    while min_heap and not visited[min_heap[0][1]]:
                        heapq.heappop(min_heap)
                    if min_heap:
                        visited[min_heap[0][1]]=0
                        heapq.heappop(min_heap)
                else:
                    while max_heap and not visited[max_heap[0][1]]:
                        heapq.heappop(max_heap)
                    if max_heap:
                        visited[max_heap[0][1]]=0
                        heapq.heappop(max_heap)

            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap) 
                

        
        if min_heap and max_heap:
            print(-max_heap[0][0], min_heap[0][0])
        else:
            print("EMPTY")


if __name__ == "__main__":
    main()