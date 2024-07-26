import sys

def cut_wood(trees, height):
    total=0
    for tree in trees:
        if tree>height:
            total+=tree-height
    return total

def BFS(trees:list, target:int):

    start, end=0, max(trees)
    result=0

    while start<=end:
        mid=(start+end) // 2
        wood=cut_wood(trees, mid)

        if wood>=target:
            result=mid
            start=mid+1
        else:
            end=mid-1

    return result
    
def main():

    input=sys.stdin.readline

    n,m=map(int, input().split())

    trees=list(map(int,input().split()))

    print(BFS(trees, m))


if __name__ == "__main__":
    main()
