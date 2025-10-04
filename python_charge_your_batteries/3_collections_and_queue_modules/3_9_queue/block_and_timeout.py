from queue import Queue

q = Queue(maxsize=3)
q.put(1)
q.put(2)
q.put(3) # Очередь стала полной после этой команды

# Выполнение операции ниже блокируется, так как block по умолчанию True и нет timeout.
q.put(4, timeout=10)
