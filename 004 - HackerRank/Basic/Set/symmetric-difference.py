# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
M = set(list(map(int, input().split())))
b = int(input())
N = set(list(map(int, input().split())))

x = M.difference(N)
y = N.difference(M)
num = sorted(x.union(y))

for item in num :
    print(item)
