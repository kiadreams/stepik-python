symbols = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
list_value = ['a', 'b', 'v', 'g', 'd', 'e', 'jo', 'zh', 'z', 'i', 'j', 'k',
              'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 'c',
              'ch', 'sh', 'shh', '*', 'y', "'", 'je', 'ju', 'ya']
tr_dic = dict(zip(symbols, list_value))

with open('18_1_exam/cyrillic.txt', encoding='utf-8') as inp_f:
    data = inp_f.read()

result_text = ''
for s in data:
    if (low_s := s.lower()) in tr_dic:
        s = tr_dic[low_s] if s.islower() else tr_dic[low_s].capitalize()
    result_text += s

with open('18_1_exam/transliteration.txt', 'w', encoding='utf-8') as out_f:
    out_f.write(result_text)