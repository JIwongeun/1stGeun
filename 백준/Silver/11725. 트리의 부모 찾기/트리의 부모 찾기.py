import sys
from collections import deque

def find(tree:dict ,result:list):

    queue=deque([1])

    while queue:
        parent=queue.popleft()
        for child in tree[parent]:
            if not result[child]:
                result[child]=parent
                queue.append(child)
    
    return
    
def main():
  
    input=sys.stdin.readline

    N=int(input().strip())

    result=[0]*(N+1)
    tree={i:[] for i in range(1, N+1)}

    

    for _  in range(N-1):

        u, v=map(int, input().split())

        tree[u].append(v)
        tree[v].append(u)

    find(tree ,result)
    
    for i in range(2, N+1):
        print(result[i])
        
if __name__ == "__main__":
    main()