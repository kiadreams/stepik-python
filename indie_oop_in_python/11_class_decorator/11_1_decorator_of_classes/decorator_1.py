def custom_settings(cls):
    cls.host = '127.0.0.1'
    cls.port = 80
    return cls


@custom_settings
class Settings:
    pass


print(Settings.host)
print(Settings.port)