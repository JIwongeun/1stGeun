import sys

def main():

    input=sys.stdin.readline
    N = int(input().strip())

    target = []
    
    for i in range(N):
        target.append(int(input().strip()))
    
    stack = []
    operations = []
    cur = 1
    idx = 0

    while idx < N:
        if stack and stack[-1] == target[idx]:
            stack.pop()
            operations.append('-')
            idx += 1
        else:
            if cur > N:
                print("NO")
                return
            stack.append(cur)
            operations.append('+')
            cur += 1

    print('\n'.join(operations))

if __name__ == "__main__":
    main()