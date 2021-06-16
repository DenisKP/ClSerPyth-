# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
bwords = [b'class', b'function', b'method']
for bword in bwords:
    print(f'Содержимое "{bword.decode("utf-8")}" длиной  {len(bword)} имеет тип: {type(bword)}')
