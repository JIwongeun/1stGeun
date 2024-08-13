import sys
import math

def DFS(n, m, s, num_list):

    if len(s)==m:
        print(*s)
        return
    
    rememnber_num=0

    if len(s):
        max_=max(s)
    else:
        max_=0

    for i in range(n):
        if rememnber_num!=num_list[i] and max_<=num_list[i]:
            s.append(num_list[i])
            rememnber_num=num_list[i]
            DFS(n, m, s, num_list)
            s.pop()
    
    
def main():
    input = sys.stdin.readline

    N, M = list(map(int, input().rstrip().split()))

    num_list=list(map(int, input().split()))

    num_list.sort()
    
    s=[]

    DFS(N, M, s, num_list)
    
if __name__ == "__main__":
    main()