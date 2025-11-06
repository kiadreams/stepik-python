import os
from zipfile import ZipFile


if not os.path.exists('FastAndTheFurious.zip'):
    import task_7_2_4

all_bytes = 0
with ZipFile('FastAndTheFurious.zip', mode="r") as archive:
    for file_info in archive.infolist():
        if file_info.filename.endswith('.txt'):
            all_bytes += file_info.compress_size

print(all_bytes)
