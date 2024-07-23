import sys

def main():  
    input = sys.stdin.readline
    test = int(input().strip())

    for _ in range(test):
        costume = {}
        N = int(input().strip())
        
        for i in range(N):
            wear, kind = input().split()
            if kind not in costume:
                costume[kind] = 1
            else:
                costume[kind] += 1
        
        
        combinations = 1
        for kind in costume:
            combinations *= (costume[kind] + 1)
        
        
        combinations -= 1
        
        print(combinations)

if __name__ == "__main__":
    main()
