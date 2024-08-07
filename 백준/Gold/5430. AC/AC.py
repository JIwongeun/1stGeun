import sys
from collections import deque

def R(reverse_flag : bool):

    return not reverse_flag


def D(q:deque, reverse_flag : bool):

    if not len(q):
        return 1
    else:
        if reverse_flag:
            q.pop()
        else:
            q.popleft()
    
    return 0

def main():
    input = sys.stdin.readline

    T=int(input().strip())

    for _ in range(T):
        functions=input().strip()
        n=int(input().strip())
        num_list=input().strip()

        key=0 
        reverse_flag=False

        if num_list=='[]':
            q=deque()
        else:
            q=deque(list(map(int, num_list.strip('[]').split(','))))

        for func in functions:
            if func=='R':
                reverse_flag=R(reverse_flag)
            else:
                key=D(q, reverse_flag)
                if key:
                    print("error")
                    break

        if not key:
            if reverse_flag:
                q.reverse()
            print(f"[{','.join(map(str, q))}]")
        
    
if __name__ == "__main__":
    main()