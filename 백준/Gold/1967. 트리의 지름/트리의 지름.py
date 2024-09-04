import sys

sys.setrecursionlimit(10**6) 

def dfs(root:int, tree:dict, visited:list):

    visited[root]=1
    farthest_node=root
    max_dist=0

    for neighbor, weight in tree[root]:
        if not visited[neighbor]:
            dist, end_node=dfs(neighbor, tree, visited)
            dist+=weight
            if dist>max_dist:
                max_dist=dist
                farthest_node=end_node

    return max_dist, farthest_node

def main():

    input = sys.stdin.readline

    N = int(input().strip())
    
    tree={i:[] for i in range(1, N+1)}

    for _ in range(N-1):
        u, v, weight=map(int, input().split())

        tree[u].append((v, weight))
        tree[v].append((u, weight))

    visited=[0]*(N+1)
    _, farthest_node=dfs(1, tree, visited)

    visited=[0]*(N+1)
    max_dist, _=dfs(farthest_node, tree, visited)

    print(max_dist)


if __name__ == "__main__":
    main()

