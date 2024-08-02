import sys

def main():
    input = sys.stdin.readline

    n=int(input().strip())
    length=int(input().strip())
    string=input().strip()

    Pn='IO'*n+'I'
    size=2*n+1   

    result=0

    for i in range(len(string)-size+1):
        if string[i:size]==Pn:
            result+=1
        size+=1

    print(result)
    

if __name__ == "__main__":
    main()