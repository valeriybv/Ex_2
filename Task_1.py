# Дана переменная, в которой хранится слово из латинских букв. Напишите код, который выводит на экран:

# среднюю букву, если число букв в слове нечетное;
# две средних буквы, если число букв четное.


def find_median(word):
    letter_list = list(word)
    if len(letter_list)%2 == 0:
        return ''.join(letter_list[int((len(letter_list))/2 - 1):int((len(letter_list))/2 + 1)])
    else:
        return ''.join(letter_list[int((len(letter_list) - 1)/2)])


word = input("Введите слово:")
median = find_median(word)
print (median)