import sys


def main():

    input=sys.stdin.readline

    N, M=map(int, input().split())

    N_list=set()
    NM_list=[]
    NM_cnt=0

    for _ in range(N):
        N_list.add(input().strip())

    for _ in range(M):
        M_name=input().strip()
        if M_name in N_list:
            NM_list.append(M_name)
            NM_cnt+=1

    print(NM_cnt)

    NM_list.sort()
    for name in NM_list:
        print(name)


if __name__ == "__main__":
    main()