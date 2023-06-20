#Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек.
#Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту
# и познакомим людей с одинаковыми индексами после сортировки!
# Но мы не будем никого знакомить, если кто-то может остаться без пары

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']


def check_arrays(boys, girls):
    if len(boys) == len(girls):
        return 1
    else:
        return 0


def get_pairs(boys, girls):
    p = check_arrays(boys, girls)
    if p == 1:
        boys.sort()
        girls.sort()
        pairs = list(zip(boys, girls))
        print (pairs)
    else:
        print ("Внимание, кто-то может остаться без пары!")


get_pairs(boys, girls)