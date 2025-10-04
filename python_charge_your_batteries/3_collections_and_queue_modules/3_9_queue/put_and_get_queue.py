from queue import Queue

q = Queue()
print(q.queue)
for i in [100, 'Hello', False]:
    q.put(i)
print('Наполнили очередь', q.queue)

print('Начинаем доставать элементы')
print(q.get(), q.queue)
print(q.get(), q.queue)
print(q.get(), q.queue)
# q.put(1)
print(q.get(), q.queue)
