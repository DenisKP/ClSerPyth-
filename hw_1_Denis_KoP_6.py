# 6.Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор»
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.


f_n = open("test_file.txt", "w")

f_n.write("сетевое программирование\nсокет\nдекоратор\n")
f_n.close()
print(f_n)

with open('test_file.txt', encoding='utf-8') as book:
    for el_str in book:
        print(el_str, end='')
