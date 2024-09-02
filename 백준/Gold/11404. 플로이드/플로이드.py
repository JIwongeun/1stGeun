import sys
import math

def Floyd(graph:list, dist:list, v:int):

    for i in range(v):
        for j in range(v):
            if i==j:
                dist[i][j]=0
            elif graph[i][j]:
                dist[i][j]=graph[i][j]
            else:
                dist[i][j]=math.inf
    
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])
                    

    return dist
    

def main():

    input=sys.stdin.readline

    V=int(input().strip())
    E=int(input().strip())

    graph=[[0]*(V) for _ in range(V)]
    dist=[[0]*(V) for _ in range(V)]


    for _ in range(E):
        u, v, weight=map(int, input().split())

        if graph[u-1][v-1] == 0 or graph[u-1][v-1] > weight:
            graph[u-1][v-1] = weight

    result=Floyd(graph, dist, V)

    for i in range(V):
        for j in range(V):
            if result[i][j] == math.inf:
                print(0, end=" ") 
            else:
                print(result[i][j], end=" ")
        print() 
                
if __name__ == "__main__":
    main()
