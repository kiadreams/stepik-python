import os
from zipfile import ZipFile


path = 'temp'
os.mkdir(path)

files = ["BananaPeel_Slippery.doc", "DiscoDancingUnicorn.mp3", "SneezingPanda.gif", "InvisibleCloak.exe",
         "PizzaDelivery_Drone.txt", "LaserCat_Visualization.pdf", "AlienCookbook.txt",
         "ZombieApocalypseSurvivalGuide.docx", "TalkingPotato.mp4", "DancingBroccoli.jpg"]

def create_file(name):
    with open(name, 'w', encoding='utf-8') as f:
        f.write(name)

for file_name in files:
    name = f'./{path}/{file_name}'
    if not os.path.exists(name):
        create_file(name)

with ZipFile('XXX.zip', 'a') as zip:
    for file_name in files:
        name = f'./{path}/{file_name}'
        zip.write(name)

with ZipFile('XXX.zip', 'r') as zip:
    zip.printdir()
