import textwrap

def wrap(string, max_width):
    result = [string[i:i+max_width] for i in range(0,len(string)+1,max_width)]
    word = '\n'.join(result)
    return word

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)