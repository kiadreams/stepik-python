import time


start_time_1 = time.time()
start_time_2 = time.monotonic()
start_time_3 = time.perf_counter()


for i in range(5): 
    print(i)
    time.sleep(0.5)

end_time_1 = time.time()
end_time_2 = time.monotonic()
end_time_3 = time.perf_counter()

elapsed_time_1 = end_time_1 - start_time_1
elapsed_time_2 = end_time_2 - start_time_2
elapsed_time_3 = end_time_3 - start_time_3

print(f'Время работы программы по time: {elapsed_time_1 = }')
print(f'Время работы программы по monotonic: {elapsed_time_2 = }')
print(f'Время работы программы по perf_counter: {elapsed_time_3 = }')