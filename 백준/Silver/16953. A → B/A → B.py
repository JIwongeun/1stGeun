import sys
from collections import deque

def main():
  
    input=sys.stdin.readline

    n,m = map(int, input().split())

    queue=deque([(n, 1)])
    visited=set([n])

    while queue:
        num, count=queue.popleft()

        if num==m:
            print(count)
            return

        next_num1=2*num
        next_num2=int(str(num)+'1')

        if next_num1<=m and next_num1 not in visited:
            queue.append((next_num1, count+1))
            visited.add(next_num1)

        if next_num2<=m and next_num2 not in visited:
            queue.append((next_num2, count+1))
            visited.add(next_num2)
        
    print(-1)

  
if __name__ == "__main__":
    main()
