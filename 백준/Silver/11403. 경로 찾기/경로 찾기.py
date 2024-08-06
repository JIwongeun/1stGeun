import sys



def main():
    input = sys.stdin.readline

    N=int(input().strip())

    graph=[list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if graph[j][i] and graph[i][k]:
                    graph[j][k] = 1
                    
    for g in graph:
        print(*g)
    

if __name__ == "__main__":
    main()