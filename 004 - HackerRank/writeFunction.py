def is_leap(year):
    leap = year % 4 == 0 and (year % 400 == 0 or year % 100 != 0) 
    return leap

year = int(input("Masukan Tahun : "))
is_leaps = is_leap(year)
print (is_leaps)