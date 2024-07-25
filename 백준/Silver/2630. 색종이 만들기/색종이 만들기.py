import sys

def cutting(paper, size, result):

    all_zero = all(cell == 0 for row in paper for cell in row)
    all_one = all(cell == 1 for row in paper for cell in row)

    if all_zero:
        result[0] += 1
        return
    elif all_one:
        result[1] += 1
        return
    else:
        mid = size // 2
        top_left = [row[:mid] for row in paper[:mid]]
        top_right = [row[mid:] for row in paper[:mid]]
        bottom_left = [row[:mid] for row in paper[mid:]]
        bottom_right = [row[mid:] for row in paper[mid:]]
        
        cutting(top_left, mid, result)
        cutting(top_right, mid, result)
        cutting(bottom_left, mid, result)
        cutting(bottom_right, mid, result)

def main():

    input=sys.stdin.readline

    size=int(input().strip())

    paper=[]
    
    for row in range(size):
        paper.append((list(map(int, input().split()))))

    result=[0,0]

    cutting(paper, size, result)

    print(result[0])
    print(result[1])

if __name__ == "__main__":
    main()
