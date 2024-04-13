import time


second = time.time()
print(f'Количество {second = }')
local_time = time.ctime(second)
print()
print(local_time)
time.sleep(5)
print(time.ctime())