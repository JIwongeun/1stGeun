import sys

def main():
    input=sys.stdin.readline

    K, N=map(int,input().split())

    cable_list=[]

    for i in range(K):
        cable_length=int(input().strip())
        cable_list.append(cable_length)

    end=max(cable_list)
    start=1

    while start<=end:
        cable_cnt=0
        mid=(start+end)//2

        for cable in cable_list:
            cable_cnt+=cable//mid
        
        if cable_cnt>=N:
            start=mid+1
        else:
            end=mid-1

    print(end)
    
    

if __name__=="__main__":
    main()