def swap_case(s):
    new_str = ''
    for i in s :
        if i.isupper() == True :
            new_str += i.lower()
        elif i.islower() == True :
            new_str += i.upper()
        elif i.isspace() == True :
            new_str += i
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)