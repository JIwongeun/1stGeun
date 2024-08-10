import sys
from collections import deque

def D(num:int):

    return 2*num%10000

def S(num:int):

    return (num-1)%10000

def L(num:int):

    return (num%1000)*10 + num//1000

def R(num:int):

    return (num%10)*1000 + num//10

def main():
    input = sys.stdin.readline

    T=int(input().strip())

    for _ in range(T):

        num, target=map(int, input().rstrip().split())

        queue=deque([(num, "")])

        visited=[0]*10000
        
        visited[num]=1

        while queue:

            cur, path=queue.popleft()

            if cur==target:
                print(path)
                break
            
            for func, command in [(D,'D'), (S,'S'),(L,'L'), (R,'R')]:
                next_num=func(cur)
                if not visited[next_num]:
                    visited[next_num]=1
                    queue.append((next_num, path+command))

if __name__ == "__main__":
    main()