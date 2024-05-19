import string


# Напишите определение класса Registration
class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login: str):
        if not isinstance(login, str):
            raise TypeError("Логин должен быть строкой")
        if login.count("@") != 1:
            raise ValueError("Логин должен содержать только один символ '@'")
        if "." not in login.partition("@")[2]:
            raise ValueError("В логине нет символа '.' после символа '@'")
        self.__login = login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой")
        if len(password) < 5 or len(password) > 11:
            raise ValueError("Пароль должен быть более 4 и менее 12 символов")
        if not Registration.is_include_digit(password):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        if not Registration.is_include_all_register(password):
            raise ValueError("Пароль должен включать символы обоих регистров")
        if not Registration.is_include_only_latin(password):
            raise ValueError("Пароль включает не только латинский алфавит")
        if Registration.check_password_dictionary(password):
            raise ValueError("Ваш пароль содержится в списке самых легких")
        self.__password = password

    @staticmethod
    def is_include_digit(password):
        for symbol in password:
            if symbol.isdigit():
                return True
        return False

    @staticmethod
    def is_include_all_register(password):
        low_letters = 0
        up_letters = 0
        for symbol in password:
            if symbol.islower():
                low_letters += 1
            elif symbol.isupper():
                up_letters += 1
        return low_letters and up_letters

    @staticmethod
    def is_include_only_latin(password):
        for symbol in password:
            if symbol not in "".join([string.ascii_letters, string.digits]):
                return False
        return True

    @staticmethod
    def check_password_dictionary(password):
        with open("easy_passwords.txt", encoding="utf-8") as f:
            return password in f.read().split("\n")


# Ниже код для проверки класса Registration
try:
    s2 = Registration("fga", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError(
        "Registration('fga', 'asd12') как можно записать такой логин?"
    )

try:
    s2 = Registration("fg@a", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError(
        "Registration('fg@a', 'asd12') как можно записать такой логин?"
    )

s2 = Registration("translate@gmail.com", "as1SNdf")
try:
    s2.login = "asdsa12asd."
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12asd как можно записать такой логин?")

try:
    s2.login = "asdsa12@asd"
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12@asd как можно записать такой логин?")

assert Registration.check_password_dictionary(
    "QwerTy123"
), "проверка на пароль в слове не работает"

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError(
        "QwerTy123 хранится в словаре паролей, как его можно было сохранить?"
    )


try:
    s2.password = "KissasSAd1f"
except ValueError as e:
    pass
else:
    raise ValueError(
        "KissasSAd1f хранится в словаре паролей, как его можно было сохранить?"
    )

try:
    s2.password = "124244242"
except ValueError as e:
    pass
else:
    raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "RYIWUhjkdbfjfgdsffds"
except ValueError as e:
    pass
else:
    raise ValueError(
        "RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?"
    )

try:
    s2.password = "CaT"
except ValueError as e:
    pass
else:
    raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "monkey"
except ValueError as e:
    pass
else:
    raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")

try:
    s2.password = "HelloQEWq"
except ValueError as e:
    pass
else:
    raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = [4, 32]
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

try:
    s2.password = 123456
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

print("U r hacked Pentagon")
