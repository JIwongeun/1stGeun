import sys

def main():
    input = sys.stdin.readline

    n=int(input().strip())
    length=int(input().strip())
    string=input().strip()

    result=0
    count=0
    i=0

    while i<length-1:
        if string[i:i+3]=='IOI':
            count+=1
            i+=2
            if count==n:
                result+=1
                count-=1
        else:
            i+=1
            count=0

    print(result)

if __name__ == "__main__":
    main()