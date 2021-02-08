opening = "find average of your number (using for)"
opening = opening.upper()
print(opening)
print("".center(50,"="))

# perulanganFor
z =0
ulang = int(input("Masukan banyaknya perulangan = "))
for i in range(ulang):
    num = int(input("Masukan bilangan ke-"+ str(i) + ' = '))
    z += num
avg = z/ulang
print(avg)