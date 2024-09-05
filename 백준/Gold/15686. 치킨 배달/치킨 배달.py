import sys

min_ans=99999999

def dfs(idx:int, cnt:int, m:int, home:list, chicken:list, visited:list):

    global min_ans

    if cnt==m:

        ans=0

        for i in home:
            distance=9999999
            for j in range(len(visited)):
                if visited[j]:
                    check_num=abs(i[0]-chicken[j][0])+abs(i[1]-chicken[j][1])
                    distance=min(distance, check_num)
            ans+=distance
        min_ans=min(ans, min_ans)

    
        return

    for i in range(idx, len(chicken)):
        if not visited[i]:

            visited[i]=1
            dfs(i+1, cnt+1, m, home, chicken, visited)
            visited[i]=0 

def main():

    input=sys.stdin.readline

    N,M=map(int, input().split())

    home=[]

    chicken=[]

    for i in range(N):
        row=list(map(int, input().split()))

        for j in range(N):
            if row[j]==1:
                home.append((i,j))
            elif row[j]==2:
                chicken.append((i,j))

    visited=[0]*len(chicken)
        
    dfs(0, 0, M, home, chicken, visited)

    print(min_ans)

if __name__ == "__main__":
    main()

