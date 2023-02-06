
def start():
    file = open('noun.txt', 'r')
    file2 = open('answers.txt', 'w')

    words = file.readlines()
    items = words
    return items

'''
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
'''

def yellow(items,letter,place):
        
    #letter = input('Введите букву: ')
    letter = letter.upper()
    #place = int(input('Введите номер буквы: '))
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
    #print(items)
    return txt

            
        
def white(items,letter,place):
    #letter = input('Введите букву: ')
    letter = letter.upper()
    #place = int(input('Введите номер буквы где она не стоит: '))
    for item in items:
        if item != '':
            if item[place-1] == letter:
                index = items.index(item)
                items[index] = ''

    txt = ''
    for i in items:
            if i != '':
               i = i.replace('\n', '') 
               txt = txt +i
               txt = txt+ ', '
    #print(items)  
    return txt



def grey(items, letter):
    #letter = str(input('Введите букву: '))
    letter = letter.upper()
    for item in items:
        if item != '':
            if item.find(letter) != -1:
                index = items.index(item)
                items[index] = ''
    txt = ''
    for i in items:
            if i != '':
               i = i.replace('\n', '') 
               txt = txt +i
               txt = txt+ ', '
    #print(items)
    return txt


def greys(items,letters):
    #letter = str(input('Введите буквы через пробел: '))
    letters = letters.split(' ')
    for i in letters:
        i = i.upper()
        #print(i)
        for item in items:
                if item != '':
                    if item.find(i) != -1:
                        index = items.index(item)
                        items[index] = ''  
    txt = ''
    for i in items:
            if i != '':
               i = i.replace('\n', '') 
               txt = txt +i
               txt = txt+ ', '                         
    #print(items)
    return txt

        


#variants()
    
    

#file.close()
#file2.close()
