opening = "find average of your number (using while)"
opening = opening.upper()
print(opening)
print("".center(50,"="))

Perulangan While
z = 1
x = 0
ulang = int(input('Masukan banyaknya perulangan = '))
while (z <= ulang) :
    num = int(input('Masukan bilangan ke-' + str(z) + ' = '))
    x += num
    z += 1
avg = x/ulang
print('rata-rata nya adalah = ' + str(avg))