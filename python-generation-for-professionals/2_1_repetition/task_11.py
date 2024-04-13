
# Первый мой вариант...
# def get_biggest(numbers: list) -> int:
#     if not numbers:
#         return -1
#     result = []
#     for i in range(9, -1, -1):
#         temp = [str(x) for x in numbers if str(x)[0] == str(i)]
#         if temp:
#             m_len = len(max(temp))
#             temp.sort(
#                 key=lambda x: ((x * (m_len // len(x) + 1))[:m_len + 1], x[-1]),
#                 reverse=True)
#             result.extend(temp)
#     return int(''.join(result))



# Второй мой вариант
def get_biggest(numbers: list) -> int:
    if numbers:
        m_len = len(str(max(numbers)))
        numbers = list(map(str, sorted(numbers, key=lambda x: str(x) * m_len)))
        return int(''.join(numbers[::-1]))
    return -1

# Чужой вариант
# def get_biggest(numbers: list):
#     if numbers:
#         lenght = max(len(str(x)) for x in numbers)
#         new_numbers = list(
#             map(str, sorted(numbers, key=lambda x: str(x) * lenght, reverse=True)))
#         return int("".join(new_numbers))
#     return -1

# Проверка тустов
my_path = '2_1_repetition/tests_2310080/'
for i in range(1, 16):
    with (open(f'{my_path}{i}', encoding='utf-8') as f_1,
          open(f'{my_path}{i}.clue', encoding='utf-8') as f_2):
        data_1 = [int(s) for s in f_1.read()[19:-3].split(',') if s]
        b = f_2.read()
        a = str(get_biggest(data_1))
        for j in range(len(a)):
            # print(a[j], b[j])
            if a[j] != b[j]:
                print(j, a[j], b[j])
        # print(b)
        # print(data_1)
        # print(a, b)
 
        result = (a if data_1 else '-1') == b
        print(f'Test_{i}: {result}')
    
