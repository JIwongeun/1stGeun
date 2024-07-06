import sys

def main():
   
    input=sys.stdin.readline

    N=int(input().strip())

    str=input().strip()

    sum=0
    i=0

    for ch in str:
        sum+=(ord(ch)-ord('a')+1)*pow(31,i)
        i+=1
    
    print(sum%1234567891)

if __name__ == "__main__":
    main()