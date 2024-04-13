# with open('17_3_files/population.txt', encoding='utf-8') as f:
#     for line in f:
#         country, population = line.rstrip().split('\t')
#         if country.startswith('G') and int(population) > 500_000:
#             print(country)


with open('17_3_files/population.txt', encoding='utf-8') as f:
    result = (c for c, p in map(lambda x: x.split('\t'), f)
              if c.startswith('G') and int(p) > 500_000)
    print(*result, sep='\n')
