try:
    file = open('pentagon_secrets.txt', 'r')
except FileNotFoundError:
    print("Эх, не судьба тайны пентагона узнать")
else:
    print(file.read())