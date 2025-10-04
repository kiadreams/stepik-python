from queue import Queue

q = Queue(maxsize=3)
q.put(1, block=False)
q.put(2, block=False)
q.put(3, block=False) # Очередь стала полной после этой команды
print(q.queue)

# Выполнение операции ниже очередь не блокируется, сразу получаем ошибку
q.put(4, block=False)
