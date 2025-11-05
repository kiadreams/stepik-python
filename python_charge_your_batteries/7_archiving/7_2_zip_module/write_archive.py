from zipfile import ZipFile, is_zipfile


with ZipFile('my_archive.zip') as my_archive:
    my_archive.printdir()
print()

if is_zipfile('my_archive.zip'):
    with ZipFile('my_archive.zip') as my_archive:
        my_archive.printdir()

with ZipFile('my_archive.zip', mode='w') as my_archive:
    my_archive.write('./my_archive/taken.txt')
    print()
    my_archive.printdir()
