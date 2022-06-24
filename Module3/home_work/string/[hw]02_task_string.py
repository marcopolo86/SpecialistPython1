# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"



new_string = input("строка: ")
# new_string = 'привет бла бба пока'
index_b = (new_string.find('б'))
index_0 = (new_string.find(' ', index_b))
# print(index_b)
# print(index_0)
print(new_string[index_b:index_0])
