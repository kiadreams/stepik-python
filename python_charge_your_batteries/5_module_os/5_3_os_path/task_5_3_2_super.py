import os
import time
from dataclasses import dataclass


@dataclass
class File:
    path: str
    name: str
    access_time: float
    modified_time: float
    change_time: float
    size: int
    is_type_file: bool

    def __str__(self):
        return (
            f'File         : {self.name}\n'
            f'Access time  : {time.ctime(self.access_time)}\n'
            f'Modified time: {time.ctime(self.modified_time)}\n'
            f'Change time  : {time.ctime(self.change_time)}\n'
            f'Size         : {self.size}'
        )


@dataclass
class FileManager:
    files: list[File] = None

    def search_all_element(self, path: str):
        self.files = []
        for e in os.listdir(path):
            full_path = os.path.join(path, e)
            file = self.__create_file(e, full_path)
            self.files.append(file)

    def print_files(self, is_dir=True, is_file=True):
        for f in self.files:
            if is_dir and is_file:
                self.__print_file(f)
            elif is_file and f.is_type_file:
                self.__print_file(f)
            elif is_dir and not f.is_type_file:
                self.__print_file(f)

    @staticmethod
    def __create_file(name, full_path) -> File:
        return File(
            path=full_path,
            name=name,
            access_time=os.path.getatime(full_path),
            modified_time=os.path.getmtime(full_path),
            change_time=os.path.getctime(full_path),
            size=os.path.getsize(full_path),
            is_type_file=os.path.isfile(full_path),
        )

    @staticmethod
    def __print_file(file: File) -> None:
        print("-".ljust(39, "-"))
        print(file)


if __name__ == '__main__':
    file_manager = FileManager()
    file_manager.search_all_element(os.getcwd())
    file_manager.print_files(is_dir=True, is_file=True)
