import sys

def main():
    
    stack=[]

    input=sys.stdin.readline().rstrip()

    result=0

    

    for ch in input:
        if(ch=='('):
            stack.append(ch)
            check=1
        elif(ch==')'):
            stack.pop()
            if(check==1):
                result+=len(stack)
                check=0
            else:
                result+=1
        
    print(result)

if __name__=="__main__":
    main()