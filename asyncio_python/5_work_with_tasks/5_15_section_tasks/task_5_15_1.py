import asyncio
import random
from itertools import product


shapes = ["circle", "star", "square", "diamond", "heart"]
colors = ["red", "blue", "green", "yellow", "purple"]
actions = ["change_color", "explode", "disappear"]


async def launch_firework(firework):
    shape, color, action = firework
    print(f"Запущен {color} {shape} салют, в форме {action}!!!")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Салют {color} {shape} завершил выступление {action}")


async def main():
    fireworks = list(product(shapes, colors, actions))
    random.shuffle(fireworks)
    tasks = [launch_firework(firework) for firework in fireworks]
    await asyncio.gather(*tasks)


asyncio.run(main())
