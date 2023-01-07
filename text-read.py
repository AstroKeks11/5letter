def main():
    #file1 = open('Словарь-тест.txt', encoding="utf8")
    file1 = open('Словарь.txt', encoding="utf8")
    file2 = open('noun.txt', 'a')

    strings = file1.readlines()

    words = []
    for string in strings:
        if (string.find('м.') != -1) or (string.find('ж.') != -1) or (string.find('ср.') != -1):
            strTest = string.split(',')
            word = strTest[0]
            if len(word) == 6:
                if word.find('\x05') != -1:
                    word1 = word.split('\x05')
                    #print(word1)
                    word2 = word1[0] + word1[1]
                    file2.write(word2 + '\n')
                if word.find('\x02') != -1:
                    word1 = word.split('\x02')
                    #print(word1)
                    word2 = word1[0] + word1[1]
                    if len(word2) == 5:
                        file2.write(word2 + '\n')
           
    file1.close()
    file2.close()

if __name__ == '__main__':
    main()