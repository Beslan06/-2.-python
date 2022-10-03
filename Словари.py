dictionary = {} #пустой словарь
# чтобы не писать в одну строчку \
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }

# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}  #      вывод 1
# или так - print(dictionary['left']) # ←        вывод 2
# типы ключей могут отличаться

##### или так 3 вывод 
for k in dictionary.keys(): #если нужно получить только значение вместо keys написать values, вывод 3
    print(k)


###############################################
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
 print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →