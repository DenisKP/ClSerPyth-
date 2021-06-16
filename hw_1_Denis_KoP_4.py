# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).
enc_words = ['разработка', 'администрирование', 'protocol', 'standard']

for enc_word in enc_words:
    benc = enc_word.encode("utf-8")
    denc = benc.decode("utf-8")
    print(f'Преобразуем слово "{enc_word}" из строкового в байтовое: {benc} {type(benc)} '
          f'и обратно "{denc}" {type(denc)}')
