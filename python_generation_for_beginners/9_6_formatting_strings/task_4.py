message = ["Что-то пошло не так", "Все идет по плану"]
weight_loss_step = (100 - 88) / 60
day = int(input())
weight = float(input())
aim = 100 - weight_loss_step * day
print(message[weight <= aim])
print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {aim} кг")
