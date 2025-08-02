class UserMail:
    logins = {}

    def __init__(self, user_login, email):
        self.login = user_login
        self.email = email

    @property
    def login(self):
        return UserMail.logins.get(self)

    @login.setter
    def login(self, user_login):
        if not isinstance(user_login, str):
            raise TypeError(f'{user_login} не является строкой')
        elif user_login in UserMail.logins.values():
            raise ValueError(f'Логин {user_login} уже имеется в системе')
        else:
            UserMail.logins.update({self: user_login})

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        if (
            isinstance(new_email, str)
            and len(new_email.split("@")) == 2
            and "." in new_email.split("@")[1]
        ):
            self.__email = new_email
        else:
            print(f"ErrorMail:{new_email}")


# -------------------------------------------------------------------------
# тест №1
jim = UserMail("aka47", 'hello@com.org')
print(isinstance(type(jim).login, property))
print(f'Jim login is {jim.login}')
try:
    bim = UserMail("aka47", 'world@com.org')
except ValueError as e:
    print(e)
jim.login = 'aka48'
print(f'Jim login is {jim.login}')
bim = UserMail("aka47", 'world@com.org')
print(f'Bim login is {bim.login}')

# -------------------------------------------------------------------------
# тест №2
users = [
    UserMail("person", "hello@com.org"),
    UserMail("person1", "hello1@com.org"),
    UserMail("person2", "hello2@com.org"),
]
try:
    UserMail("person1", "hello3@com.org")
except ValueError as e:
    print(e)

try:
    UserMail("person2", "hello4@com.org")
except ValueError as e:
    print(e)

r = UserMail("person3", "hello5@com.org")
print(r.login)
