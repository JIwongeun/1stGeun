import sys
import heapq
import math

def Dijkstra(graph:dict, start:int, dist:list, visited:list):

    heap=[]

    heapq.heappush(heap, (0, start))

    dist[start]=0

    while heap:

        cur_dist, cur_node = heapq.heappop(heap)

        if visited[cur_node]:
            continue

        visited[cur_node]=1

        for neighbor, weight in graph[cur_node]:

            new_dist=cur_dist+weight

            if new_dist<dist[neighbor]:
                dist[neighbor]=new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return dist[1:]
    

def main():

    input=sys.stdin.readline

    V, E=map(int, input().split())

    start=int(input().strip())

    graph={i:[] for i in range(1, V+1)}

    for _ in range(E):
        u, v, weight=map(int, input().split())

        graph[u].append((v, weight))

    dist=[math.inf]*(V+1)
    visited=[0]*(V+1)

    result=Dijkstra(graph, start, dist, visited)

    for i in result:
        if i==math.inf:
            print('INF')
        else:
            print(i)
                
if __name__ == "__main__":
    main()
