import sys

def main():
    
    input=sys.stdin.readline
    n=int(input().strip())
    
    for i in range(1,n+1):
        A,B=map(int, input().split())
        print(f'Case #{i}: {A} + {B} = {A+B}')
    
if __name__=="__main__":
    main()