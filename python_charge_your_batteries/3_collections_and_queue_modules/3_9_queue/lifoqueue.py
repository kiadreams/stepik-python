from queue import LifoQueue

stack = LifoQueue()
print(stack.queue)
for i in [200, [1, 2, 4], 'Not bad']:
    stack.put(i)
print('Наполнили стек', stack.queue)

print('Начинаем доставать элементы')
print(stack.get(), stack.queue)
print(stack.get(), stack.queue)
print(stack.get(), stack.queue)
print(stack.get(timeout=1), stack.queue)
