import sys

def main():
    
    input=sys.stdin.readline

    N=int(input().strip())

    meeting_time=[]

    for _ in range(N):
        start, end=map(int, input().split())

        meeting_time.append((start, end))

    meeting_time.sort(key=lambda x:(x[1], x[0]))

    result=0

    last_end_time=0

    for start, end in meeting_time:
        if start>=last_end_time:
            result+=1
            last_end_time=end
    
    print(result)

if __name__=="__main__":
    main()