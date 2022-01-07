if __name__ == '__main__':
    N = int(input())
    array = []
    for _ in range(N) :
        command, *line = input().split()
        num = list(map(int, line))
        if command == "append" :
            array.append(num[0])
        elif command == "insert" :
            array.insert(num[0], num[1])
        elif command == "remove" :
            array.remove(num[0])
        elif command == "pop" :
            array.pop()
        elif command == "sort" :
            array.sort()
        elif command == "reverse" :
            array.reverse()
        elif command == "print" :
            print(array)