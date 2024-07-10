import sys


def fib_list_make():

    fib_memo=[(1,0),(0,1)]+[(0,0)]*(39)

    for i in range(2, 41):
        fib_memo[i]=(fib_memo[i-1][0] + fib_memo[i-2][0], 
                     fib_memo[i-1][1] + fib_memo[i-2][1])
    
    return fib_memo
        

def main():
    
    input=sys.stdin.readline

    T=int(input().strip())

    results=[]

    fib_memorize_list=fib_list_make()

    for _ in range(T):   
        N=int(input().strip())
        results.append(fib_memorize_list[N])

    for result in results:
        print(result[0], result[1])    

        
if __name__=="__main__":
    main()