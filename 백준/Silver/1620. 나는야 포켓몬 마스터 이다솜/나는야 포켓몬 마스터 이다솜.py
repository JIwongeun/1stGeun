import sys

def main():
    
    input=sys.stdin.readline

    N,M=map(int, input().split())

    poketmon_id={}
    poketmon_name={}

    for i in range(1, N+1):
        poketmon=input().strip()
        poketmon_id[i]=poketmon
        poketmon_name[poketmon]=i

    for _ in range(M):
        x=input().strip()
        if x.isdigit()==True:
            print(poketmon_id[int(x)])
        else:
            print(poketmon_name[x])



   

if __name__=="__main__":
    main()