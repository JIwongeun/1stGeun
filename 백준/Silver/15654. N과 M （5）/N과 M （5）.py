import sys

def DFS(m, s, num_list):
    
    if len(s)==m:
        print(' '.join(map(str, s)))
        return
    
    for num in num_list:
        if num not in s:
            s.append(num)
            DFS(m, s, num_list)
            s.pop()

def main():
    input = sys.stdin.readline

    N, M = list(map(int, input().rstrip().split()))

    num_list=list(map(int, input().split()))

    num_list.sort()
    
    s=[]

    DFS(M, s, num_list)
    
if __name__ == "__main__":
    main()