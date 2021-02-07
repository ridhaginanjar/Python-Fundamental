opening = "Ideal Weight Calculation Program"
opening = opening.upper()
print(opening)
print("".center(50,'='))

weight = int(input('Input Your Weight = '))
height = int(input('Input Your Height = '))

height1 = height - 100
sepersepuluh = height1*0.1
totalheight = height1 - sepersepuluh

print("Your Weight right now is = ", weight)
print("Your Ideal Weight is = ", totalheight)

idealweight = weight - totalheight
print("".center(50,'_'))
if idealweight <=2 :
    print('Your weight is IDEAL!')
else :
    print("You need reducing your weight as much ", idealweight)

