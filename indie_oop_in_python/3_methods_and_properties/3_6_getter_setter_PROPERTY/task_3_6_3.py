# Напишите определение класса UserMail
class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if (
            isinstance(new_email, str)
            and len(new_email.split("@")) == 2
            and "." in new_email.split("@")[1]
        ):
            self.__email = new_email
        else:
            print(f"ErrorMail:{new_email}")

    email = property(get_email, set_email)


# Ниже код для проверки методов класса UserMail

jim = UserMail("aka47", "hello@com.org")
assert jim.login == "aka47"
assert jim._UserMail__email == "hello@com.org"
assert isinstance(jim, UserMail)
assert isinstance(type(jim).email, property), "Вы не создали property email"

jim.email = [1, 2, 3]  # печатает ErrorMail:[1, 2, 3]
jim.email = "hello@@re.ee"  # печатает ErrorMail:hello@@re.ee
jim.email = "hello@re.w3"
assert jim.email == "hello@re.w3"

k = UserMail("belosnezhka", "prince@wait.you")
assert k.email == "prince@wait.you"
assert k.login == "belosnezhka"
assert isinstance(k, UserMail)

k.email = {1, 2, 3}  # печатает ErrorMail:{1, 2, 3}
k.email = "prince@still@.wait"  # печатает ErrorMail:prince@still@.wait
k.email = "prince@stillwait"  # печатает ErrorMail:prince@stillwait
k.email = "prince@still.wait"
assert k.get_email() == "prince@still.wait"
k.email = "pri.nce@stillwait"  # печатает ErrorMail:pri.nce@stillwait
assert k.email == "prince@still.wait"
