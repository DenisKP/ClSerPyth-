with open('test_file.txt', 'w', encoding='cp1251') as f:
    f.write("сетевое программирование\nсокет\nдекоратор")
    print(f'Кодировка по умолчанию {f.encoding=}')
    f.close()

with open('test_file.txt', "rb", encoding='UTF-8') as t_f:
    for row in t_f:
        print(row)
