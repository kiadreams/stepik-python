class User:

    def __init__(self, name, role):
        self.name = name
        self.role = role


class Access:
    __access_list = ["admin", "developer"]

    @staticmethod
    def __check_access(role):
        return role in Access.__access_list

    @staticmethod
    def get_access(user):
        if isinstance(user, User):
            if Access.__check_access(user.role):
                print(f"User {user.name}: success")
            else:
                print("AccessDenied")
        else:
            print("AccessTypeError")
