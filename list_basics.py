list_org = []

if __name__ == '__main__' :
    N = int(input())
    for _ in N:
        command, *values = input().split()
        if command == "insert":
            list_org.insert(values[1], values[2])
        elif command == "print":
            print(list_org)
        elif command == 'remove':
            list_org.remove(values[1])
        elif command == "append":
            list_org.append(values[1])
        elif command == "sort":
            list_org.sort()
        elif command == "pop":
            list_org.pop()
        elif command == "reverse":
            list_org.reverse()