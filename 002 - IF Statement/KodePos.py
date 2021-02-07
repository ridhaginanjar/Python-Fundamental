print("Menentukan Kode POS")
print("".center(20,'='))

nama = input("Masukan Nama Kota = ")

if nama.lower() in ['Padang', 'padang'] :
    print(25000)
elif  nama.lower() in ['Bandung', 'bandung']:
    print(40100)
elif nama.lower() in ['Solo', 'solo']:
    print(51000)
elif nama.lower() in ['Denpasar', 'denpasar']:
    print(72000)
elif nama.lower() in ['Palu', 'palu']:
    print(92300)
else :
    print("Kota tersebut belum tersedia")