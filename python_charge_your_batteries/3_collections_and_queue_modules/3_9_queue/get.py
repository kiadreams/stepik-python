from queue import Queue

q = Queue()
q.put(1)
q.put(2)
print(q.queue)

item = q.get()
print(item)  # Вывод: 1
print(q.get()) # Вывод: 2
print(q.queue)
