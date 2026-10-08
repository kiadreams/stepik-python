cars_arrive_time = {}

for _ in range(int(input())):
    car_id, arrive_data = input().split(": ")
    hours, minute = map(int, arrive_data.split(":"))
    cars_arrive_time[car_id] = hours * 60 + minute

for _ in range(int(input())):
    car_id, leave_data = input().split(": ")
    if car_id not in cars_arrive_time:
        continue
    hours, minute = map(int, leave_data.split(":"))
    lv_time = hours * 60 + minute
    ar_time = cars_arrive_time[car_id]
    total_time = 24 * 60 - ar_time + lv_time if lv_time < ar_time else lv_time - ar_time
    if total_time <= 120:
        print(f"{car_id}: плата не взимается")
    else:
        print(f"{car_id}: {(total_time - 120) * 3}₽")
