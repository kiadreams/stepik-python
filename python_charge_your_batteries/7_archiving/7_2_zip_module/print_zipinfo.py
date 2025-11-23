import os
from datetime import datetime
from zipfile import ZipFile


if not os.path.exists('FastAndTheFurious.zip'):
    import task_7_2_4

with ZipFile('FastAndTheFurious.zip', mode="r") as archive:
    for info in archive.infolist():
        print(f"Filename: {info.filename}")
        print(f"Modified: {datetime(*info.date_time)}")
        print(f"Normal size: {info.file_size} bytes")
        print(f"Compressed size: {info.compress_size} bytes")
        print(f"Is directory: {info.is_dir()}")
        print("-" * 20)
