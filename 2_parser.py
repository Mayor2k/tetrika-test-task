'''
В нашей школе мы не можем разглашать персональные данные пользователей, но чтобы преподаватель и ученик смогли 
объяснить нашей поддержке, кого они имеют в виду (у преподавателей, например, часто учится несколько Саш), мы 
генерируем пользователям уникальные и легко произносимые имена. Имя у нас состоит из прилагательного, имени 
животного и двузначной цифры. В итоге получается, например, "Перламутровый лосось 77". Для генерации таких имен
мы и решали следующую задачу: Получить с русской википедии список всех животных (https://inlnk.ru/jElywR) и 
вывести количество животных на каждую букву алфавита. Результат должен получиться в следующем виде:

Вариант решения с помощью парсера.
'''

import requests
import re 
from bs4 import BeautifulSoup

animals_dict = {}

def is_cyrillic(text):
    return bool(re.search('[\u0400-\u04FF]', text))

def get_animals_count(url):
    wiki_respond  = requests.get(url).text
    soup = BeautifulSoup(wiki_respond, 'lxml')
    categories = [category.children for category in soup.find_all(class_='mw-category mw-category-columns')]
    
    for category in categories:
        for elem in category:
            letter = str(elem.h3.string)
            if is_cyrillic(letter):
                print(f'Поиск элементов на букву {letter}', end="\r", flush=True)
                animals_dict[letter] = animals_dict.get(letter, 0) + len(elem.find_all('li'))
            
    url_tag = soup.find(name='a',string="Следующая страница")
    if url_tag != None:
        get_animals_count('https://ru.wikipedia.org/' + url_tag.get('href'))
    else:
        print('Поиск элементов окончен!!!')
    
url = 'https://ru.wikipedia.org//w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
get_animals_count(url)
for key in animals_dict:
    print(f'{key}: {animals_dict[key]}')