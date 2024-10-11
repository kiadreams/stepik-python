from abc import ABC, abstractmethod


class Database(ABC):

    @abstractmethod
    def connect(self): ...

    @abstractmethod
    def disconnect(self): ...

    @abstractmethod
    def execute(self, query: str): ...


class MySQLDatabase(Database):

    def connect(self):
        print('Connecting to MySQL database...')

    def disconnect(self):
        print('Disconnecting from MySQL database...')

    def execute(self, query: str):
        print(f"Executing query '{query}' in MySQL database...")


class PostgreSQLDatabase(Database):

    def connect(self):
        print('Connecting to PostgreSQL database...')

    def disconnect(self):
        print('Disconnecting from PostgreSQL database...')

    def execute(self, query):
        print(f"Executing query '{query}' in PostgreSQL database...")


print('ЗАМЫКАНИЕ'.center(77, '-'))


def some_func(value):
    counter = value

    def some_func_inner():
        nonlocal counter
        counter += 1
        return counter

    return some_func_inner


a = some_func(0)
print(a())
print(a())

b = some_func(10)
print(b())
print(b())

print(a())
print(a())
