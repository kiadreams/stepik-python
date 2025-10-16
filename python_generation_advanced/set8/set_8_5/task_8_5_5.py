results = {}

for _ in range(answers := int(input())):
    name, result = input().split(': ')
    results.setdefault(result, []).append(name)
if results.get('Correct', 0):
    print(f"Верно решили {len(set(results['Correct']))} учащихся")
    persent_of_correct = int(len(results['Correct']) / answers * 100 + 0.5)
    print(f'Из всех попыток {persent_of_correct}% верных')
else:
    print('Вы можете стать первым, кто решит эту задачу')
