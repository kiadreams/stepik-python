import sys

# for line in sys.stdin:
#     print(line.strip('\n'))

print('Hello')
sys.stdout.write('world!')
print('from')
sys.stdout.write('python\n')
print('Bye-bye')

temp = sys.stdout               # сохраняем исходный потоковый вывод
 # перенаправляем потоковый вывод в файл
sys.stdout = open('4_1_stdin_and_stdout/log.txt', 'w')
print('testing123')
print('another line')
sys.stdout.close()
sys.stdout = temp               # восстанавливаем исходный потоковый 