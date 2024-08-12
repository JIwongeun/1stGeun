import sys

def DFS(n, m, s, num_list, visited):
    
    if len(s)==m:
        print(*s)
        return
    
    remember_num=0

    for i in range(n):
        if not visited[i] and remember_num!=num_list[i]:
            visited[i]=1
            s.append(num_list[i])
            remember_num=num_list[i]
            DFS(n, m, s, num_list, visited)
            visited[i]=0
            s.pop()

def main():
    input = sys.stdin.readline

    N, M = list(map(int, input().rstrip().split()))

    num_list=list(map(int, input().split()))

    num_list.sort()
    
    s=[]

    visited=[0]*N

    DFS(N, M, s, num_list, visited)
    
if __name__ == "__main__":
    main()
