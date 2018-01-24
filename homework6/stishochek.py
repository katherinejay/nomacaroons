# coding=utf-8
import random
# Эта программа генерирует стихотворение с соблюдением метрической схемы - ямб (двухсложный).
# А ещё эту программу со мной писал студент-ИТМО-недоучка, и возможно, мы что-то делали не так.
# Заморачиваться со знаками препинания я не стала, поэтому все строчки - утвердительные предложения.


# Обозначим функцию, что будет выбирать одно слово из файла.
def choose_word(filename):
    with open(filename, encoding='utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words += [line]
        return random.choice(words)

# Используя в дальнейшем эту функцию, выберем нужные нам для составления строчек слова.
# Их тоже обозначим как функции, чтобы в дальнейшем использовать для составления строчек.
# Мне сказали, что я так начну вводить функции для всего подряд, но так реально удобнее.

def adverb():
    return choose_word('slovechki/adverbs.txt')

def agent():
    return choose_word('slovechki/agent.txt')

def indef1():
    return choose_word('slovechki/indef1.txt')

def infinit2():
    return choose_word('slovechki/infinit2.txt')

def indef2():
    verb = infinit2()
    if verb.endswith('сть'):
            verb = verb[:-3]+'л'
    elif verb.endswith('ть'):
            verb = verb[:-2]+'л'
    return verb

def pref():
    return 'за'+indef1()

def move():
    return choose_word('slovechki/move.txt')

def modal():
    return choose_word('slovechki/modal.txt')
    
def location():
    return choose_word('slovechki/location.txt')

def object1():
    return choose_word('slovechki/object1.txt')

def object2():
    return choose_word('slovechki/object2.txt')

def prtc():
    return choose_word('slovechki/prtc.txt')

def profession():
    return choose_word('slovechki/profession.txt')

def verb():
    return choose_word('slovechki/verb.txt')

# Введём функцию, делающую букву в начале строки заглавной.

def capitalization(sentence):
    return sentence[0].upper() + sentence[1:]

# Начинаем формировать строчки, исходя из выбранного размера стихотворения.
# Дабы стишочки не получались однообразными, сделаем несколько вариаций каждой строки (так чтобы они укладывались в размер!)

def oddline1():
    number = random.choice([1,2])
    if number == 1:
        sentence = agent() + ' ' + indef1() + ', ' + prtc() + ' ' + object2() + ','
    else:
        sentence = indef1() + ' ' + agent() + ', ' + prtc() + ' ' + object2() + ','   
    return capitalization(sentence)

def oddline2():
    number = random.choice([1,2])
    if number == 1:
        sentence = indef2() + ' ' + object1() + ' ' + agent() + '-' + profession() + ','
    else:
        sentence = object1() + ' ' + indef2() + ' ' + agent() + '-' + profession() + ','
    return capitalization(sentence)

def oddline():
    number = random.choice([1,2])
    if number == 1:
        return oddline1()
    else:
        return oddline2()

    
def evenline1():
    number = random.choice([1,2])
    if number == 1:
        sentence = indef2() + ' ' + object1() + ' и ' + pref() + '.' 
    else:
        sentence = object1() + ' ' + indef2() + ' и ' + pref() + '.'
    return capitalization(sentence)
       
def evenline2():
    number = random.choice([1,2])
    if number == 1:
        sentence = move() + ' ' + location() + ' и вдруг ' + verb() + '.'
    else:
        sentence = location() + ' ' + move() + ' как вдруг ' + verb() + '.' 
    return capitalization(sentence)

def evenline3():
    number = random.choice([1,2,3])
    if number == 1:
        sentence = adverb() + ' ' + modal() + ' ' + infinit2() + ' ' + object1() + '.'
    elif number == 2:
        sentence = adverb() + ' ' + modal() + ' ' + object1() + ' ' + infinit2() + '.'
    else:
        sentence = adverb() + ' ' + object1() + ' ' + modal() + ' ' + infinit2() + '.'
    return capitalization(sentence)

def evenline():
    number = random.choice([1,2,3])
    if number == 1:
        return evenline1()
    elif number == 2:
        return evenline2()
    else:
        return evenline3()

# Собираем наш стишочек!

for i in range(2):
    print(oddline()+'\n'+ evenline())

# Браво, вы великолепны! Пушкин и Лермонтов вертятся в гробах, слыша вашу поэзию, но их реакция - результат временного разрыва. Любое творчество имеет право на жизнь!
