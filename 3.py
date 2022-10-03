# 1
def new_string(symbol, count):
    return symbol * count
print(new_string('!', 5)) # выведет !!!!!
print(new_string('!')) # выведет ошибку TypeError missing 1 required ...

# 2
def new_string(symbol, count = 3):
    return symbol * count
print(new_string('!', 5)) # !!!!!
print(new_string('!')) # !!!
print(new_string(4)) # 12

# 3 работа со строкой 
def concatenatio(*params):
    res: str = "" #res-переменная, str-тип данных или int=0 вместо str для работы с числами, 
    # или вообще убрать указание типапа str, int. - res = 0 
    for item in params:
        res += item #склеивание строк
    return res
print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: .