import sys

    
def main():

    input=sys.stdin.readline

    n=int(input().strip())

    location=list(map(int,input().split()))

    uni_loc=sorted(list(set(location)))
    
    dic={uni_loc[i] : i for i in range(len(uni_loc))}

    for loc in location:
        print(dic[loc],end=" ")

if __name__ == "__main__":
    main()