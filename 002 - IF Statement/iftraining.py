opening = "Welcome to Discount Shopping Apps \n You Will Get Discount As Much 10% If The Price More Than 100.000"
opening = opening.upper()
print(opening)
print("".center(50,'='))

price = int(input('Input total shopping = '))

if price >= 100000 :
    discount = price * 0.1
    total = price - discount
    print('YOU GET THE DISCOUNT 10%!')
    print("Your total shopping is", total)
else :
    print('Your total shopping is', price)