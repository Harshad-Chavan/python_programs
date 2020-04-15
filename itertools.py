from itertools import combinations

if __name__ == '__main__':
    result = []
    str, num = input().split()
    l = list(str)
    l.sort()
    for _ in range(1,int(num)+1):
        temp = combinations(l,_)
        result.extend(list(temp))
    for tup in result:
        print("".join(tup),end="\n")
