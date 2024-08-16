import sys

def VLR(node:str,tree:dict):

    if node!='.':
         print(node, end='')
         VLR(tree[node][0], tree)
         VLR(tree[node][1], tree)
    
    return


def LVR(node:str,tree:dict):

    if node!='.':
        LVR(tree[node][0], tree)
        print(node, end='')
        LVR(tree[node][1], tree)

    return

def LRV(node:str,tree:dict):
    
    if node!='.':
        LRV(tree[node][0], tree)
        LRV(tree[node][1], tree)
        print(node, end='')

    return


def main():
  
    input=sys.stdin.readline

    N=int(input().strip())

    tree={}

    for _  in range(N):

        u, v1, v2=map(str, input().split())

        if u not in tree:        
                tree[u]=[v1]
                if u not in tree:
                    tree[u]=[v2]
                else:
                    tree[u].append(v2)
        
        else:
            tree[u].append(v1)
            tree[u].append(v2)
    

    VLR('A',tree)
    print()

    LVR('A',tree)
    print()

    LRV('A',tree)

if __name__ == "__main__":
    main()