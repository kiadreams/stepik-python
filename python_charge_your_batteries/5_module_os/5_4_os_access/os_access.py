import os

print('Файл:', __file__)
print('Существует:', os.access(__file__, os.F_OK))
print('Право на чтение:', os.access(__file__, os.R_OK))
print('Право на запись:', os.access(__file__, os.W_OK))
print('Право на исполнение:', os.access(__file__, os.X_OK))

print('Чтение и исполнение:', os.access(__file__, os.R_OK | os.X_OK))
print('Чтение и запись:', os.access(__file__, os.R_OK | os.W_OK))
