'''
В нашей школе мы не можем разглашать персональные данные пользователей, но чтобы преподаватель и ученик смогли 
объяснить нашей поддержке, кого они имеют в виду (у преподавателей, например, часто учится несколько Саш), мы 
генерируем пользователям уникальные и легко произносимые имена. Имя у нас состоит из прилагательного, имени 
животного и двузначной цифры. В итоге получается, например, "Перламутровый лосось 77". Для генерации таких имен
мы и решали следующую задачу: Получить с русской википедии список всех животных (https://inlnk.ru/jElywR) и 
вывести количество животных на каждую букву алфавита. Результат должен получиться в следующем виде:

Вариант решения через API.
'''

import requests
import re 

animals_dict = {}
url = "https://ru.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F%3A%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&prop=categories&cmtype=page&cmlimit=500&format=json"

def is_cyrillic(text):
    return bool(re.search('[\u0400-\u04FF]', text))

def get_animals_count(current_request, items_collected):
    print(f'Отсортированно ≈{items_collected} элементов', end="\r", flush=True)
    
    animals_list = current_request["query"]["categorymembers"]
    for animal in animals_list:
        #пропуск элементов, содержащие латинские символы
        if is_cyrillic(animal["title"].upper()[0]):
            if animal["title"][0].upper() in animals_dict:                    
                animals_dict[animal["title"][0].upper()] = animals_dict.get(animal["title"][0].upper()) + 1
            else:   
                animals_dict[animal["title"][0].upper()] = 1
            
    if 'continue' in current_request:
        get_animals_count(requests.get(f'{url}&cmcontinue={current_request["continue"]["cmcontinue"]}').json(), items_collected+len(animals_list))
    else:
        print("Сортировка элементов окончена!!!")

wiki_request = requests.get(url).json()
get_animals_count(wiki_request, 0)

animals_dict = dict(sorted(animals_dict.items()))
for key in animals_dict:
    print(f'{key}: {animals_dict[key]}')