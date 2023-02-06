def main():
    file1 = open('russian.txt')
    file2 = open('noun-r.txt', 'a')

    strings = file1.readlines()

    for string in strings:
        if len(string) == 6:
            file2.write(string.upper())
    print('ok')

if __name__ == '__main__':
    main()