opening = "Make star"
opening = opening.upper()
print(opening)
print("".center(50,"="))

#Perulangan while bertingkat
for i in range(5):
    for j in range(1 + i):
        print('*', end='')
    print()
for i in range(4):
    for j in range(4 - i):
        print('*', end='')
    print()