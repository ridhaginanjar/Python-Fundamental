def average(array):
    num = set(array)
    return sum(num)/len(num)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)