import sys

def main():
    input = sys.stdin.readline
    N , M= map(int,input().split())

    site_pass={}

    for _ in range(N):
        site, password=input().split()
        site_pass[site]=password
    
    for _ in range(M):
        site=input().strip()
        if site in site_pass:
            print(site_pass[site])

        

if __name__ == "__main__":
    main()

