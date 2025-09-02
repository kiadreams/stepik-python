# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список строк lst_in)
# for lst in zip(*(i.split() for i in lst_in)):
#     print(*lst)


[print(*i) for i in zip(*map(str.split, __import__('sys').stdin.read().splitlines()))]
# ДЛЯ ОСТАНОВКИ СЧИТЫВАНИЯ ИЗ ПОТОКА ВВОДА НЕОБХОДИМО ввести Ctrl +
# D (если работаете в консоли Linux или IDE PyCharm),
# либо Ctrl + Z , затем Enter (если работаете в консоли Windows).