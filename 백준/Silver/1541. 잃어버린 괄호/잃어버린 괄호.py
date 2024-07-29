import sys

def main():
    input = sys.stdin.readline

    formula=input().strip()
    
    parts=formula.split('-')
    
    result=0
    first=0

    for part in parts:
        nums=part.split('+')
        sum1=0
        for num in nums:
            sum1+=int(num)
        if first==0:
            result+=sum1
            first=1
        else:
            result-=sum1

    print(result)
        

if __name__ == "__main__":
    main()