import sys

def prec(ch):
    if ch=='*' or ch=='/':
        return 2
    elif ch=='+' or ch=='-':
        return 1
    elif ch=='(' or ch==')':
        return 0
    else:
        return -1
    
def main():

    input=sys.stdin.readline

    str=input().strip()

    stack=[]
    result=[]
    
    for ch in str:
        if ch=='+' or ch=='-' or ch=='*' or ch=='/':
            while(len(stack)!=0 and prec(stack[-1])>=prec(ch)):
                result.append(stack.pop())
            stack.append(ch)
        
        elif ch=='(':
            stack.append(ch)

        elif ch==')':
            top_ch=stack.pop()
            while(top_ch != '('):
                result.append(top_ch)
                top_ch=stack.pop()
        else:
            result.append(ch)

    while(len(stack)!=0):
        result.append(stack.pop())
            
    for i in result:
        print(i,end='')
    
if __name__ == "__main__":
    main()