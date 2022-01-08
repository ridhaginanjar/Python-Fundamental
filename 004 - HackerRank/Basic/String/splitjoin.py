def split_and_join(line):
    line = line.split()
    new_line = "-".join(line)
    return new_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)