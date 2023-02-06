def main():
    #file = open('noun.txt', 'r')
    file = open('noun-r.txt', 'r')
    file2 = open('answers.txt', 'w')

    words = file.readlines()
    items = words
    print(items)
    
    def variants():
        d = str(input('Какую букву ты знаешь? Введи желтая, белая, серая или серые: '))
        if d == 'желтая':
            yellow()
        elif d == 'серая':
            grey()
        elif d == 'белая':
            white()
        elif d == 'серые':
            greys()

    def yellow():
        
        letter = input('Введите букву: ')
        letter = letter.upper()
        place = int(input('Введите номер буквы: '))
        for item in items:
            if item != '':
                if item[place-1] != letter:
                    index = items.index(item)
                    items[index] = ''
        txt = ''
        for i in items:
            if i != '':
               i = i.replace('\n', '') 
               txt = txt +i
               txt = txt+ ', '
        print(txt) 
        #print(items)
        #answer = input('Продолжить? (Да или Нет): ')
        #if answer == 'Да':
            #variants()
        variants()
            
        
    def white():
        letter = input('Введите букву: ')
        letter = letter.upper()
        place = int(input('Введите номер буквы где она не стоит: '))
        for item in items:
            if item != '':
                if item[place-1] == letter:
                    index = items.index(item)
                    items[index] = ''
        txt = ''
        for i in items:
            if i != '':
               txt = txt +i
               txt = txt+ ', '
        print(txt) 
        print(items)
        #answer = input('Продолжить? (Да или Нет): ')
        #if answer == 'Да':
            #variants()
        variants()


    def grey():
        letter = str(input('Введите букву: '))
        letter = letter.upper()
        for item in items:
            if item != '':
                if item.find(letter) != -1:
                    index = items.index(item)
                    items[index] = ''
        print(items)
        #answer = input('Продолжить? (Да или Нет): ')
        #if answer == 'Да':
            #variants()
        variants()

    def greys():
        letter = str(input('Введите буквы через пробел: '))
        letters = letter.split(' ')
        for i in letters:
            i = i.upper()
            print(i)
            for item in items:
                    if item != '':
                        if item.find(i) != -1:
                            index = items.index(item)
                            items[index] = ''                           
        print(items)
        variants()

    def yellow1():
        letter = input('Введите букву: ')
        letter = letter.upper()
        place = int(input('Введите номер буквы: '))
        x = 0
        for item in items:
            if item[place-1] != letter:
                    items.pop(x)
            elif item[place-1] == letter:
                x += 1
        print(items)
        variants()


        


    variants()
    
    

    file.close()
    file2.close()
    

if __name__ == '__main__':
    
    main()