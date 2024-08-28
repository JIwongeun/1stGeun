import sys
import heapq
import math

def Dijkstra(start, city_cost, dist, visited):
    
    dist[start]=0

    for _ in range(len(dist)-1):

        min_dist=math.inf
        min_idx=-1

        for i in range(1, len(dist)):
            if not visited[i] and dist[i]<min_dist:
                min_dist=dist[i]
                min_idx=i

        if min_idx == -1:  
            break

        visited[min_idx]=1

        for neighbor, cost in city_cost[min_idx]:
            if not visited[neighbor]:
                if dist[min_idx]+cost<dist[neighbor]:
                    dist[neighbor] = dist[min_idx] + cost

def main():

    input = sys.stdin.readline

    N=int(input().strip())

    M=int(input().strip())

    city_cost={i:[] for i in range(1, N+1)}

    for _ in range(M):

        u,v,cost=map(int, input().split())
        
        city_cost[u].append((v, cost))

    start, end=map(int, input().split())

    dist=[math.inf]*(N+1)
    visited=[0]*(N+1)


    Dijkstra(start, city_cost, dist, visited)
            
    print(dist[end])

if __name__ == "__main__":
    main()
