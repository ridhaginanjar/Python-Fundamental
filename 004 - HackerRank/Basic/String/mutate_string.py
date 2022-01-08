def mutate_string(string, position, character):
    letters = string[:position] + "{}".format(character) + string[position+1:]
    return letters

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)