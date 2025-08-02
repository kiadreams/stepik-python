def custom_settings(host='127.0.0.1', port=10):
    def decorator(cls):
        cls.host = host
        cls.port = port
        return cls
    return decorator


@custom_settings(port=99)
class Settings:
    pass


@custom_settings(host='10.32.2.43', port=19)
class Setting2:
    pass


print(Settings.host, Settings.port)
print(Setting2.host, Setting2.port)