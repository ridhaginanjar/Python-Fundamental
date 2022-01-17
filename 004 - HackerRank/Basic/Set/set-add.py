# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
stamps = set()

for i in range(n) :
    country = input()
    stamps.add(country)
    
print(len(stamps))