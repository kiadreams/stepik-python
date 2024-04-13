numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35,
           95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

result = {key: [i for i in range(1, key // 2 + 1) if key % i == 0] + [key]
          for key in numbers}
