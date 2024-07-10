import sys

def main():
    
    input=sys.stdin.readline

    N, K=map(int,input().split())

    queue=[]

    for i in range (1, N+1):
        queue.append(i)

    idx=0

    print('<', end='')
    for i in range(N):
        idx=(idx+K-1)%len(queue)
        print(queue.pop(idx), end='')
        if i<N-1:
            print(', ', end='')
    print('>')

if __name__=="__main__":
    main()