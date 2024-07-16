import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())

    S = set()

    for _ in range(N):
        inputs = input().split()

        if len(inputs) == 1:
            order = inputs[0]
            num = None
        else:
            order, num = inputs
            num = int(num)

        if order == "add":
            S.add(num)
        elif order == "remove":
            S.discard(num)
        elif order == "check":
            if num in S:
                print(1)
            else:
                print(0)
        elif order == "toggle":
            if num in S:
                S.remove(num)
            else:
                S.add(num)
        elif order == "all":
            S = set(range(1, 21))
        elif order == "empty":
            S.clear()

if __name__ == "__main__":
    main()
