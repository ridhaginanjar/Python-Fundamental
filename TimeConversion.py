opening = "Time Conversion Program From Second to Days,Hours,Minute,Second"
opening = opening.upper()
print(opening)
print("".center(50,'='))

waktu = int(input('Input Your Times (in second) = '))

hari = waktu//86400
modhari = waktu%86400
jam = modhari //3600
modjam = modhari%3600
menit = modjam//60
detik = modjam%60

print('The conversion of time is : ')
print(hari, " Days")
print(jam, " Hours")
print(menit, " Minute")
print(detik, " Second")