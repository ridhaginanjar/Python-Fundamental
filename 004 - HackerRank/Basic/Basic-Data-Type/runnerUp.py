if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(set(sorted(arr)))
    print(scores[-2])