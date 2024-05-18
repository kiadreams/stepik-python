import json


# Напишите определение класса AppConfig
class AppConfig:
    app_config = {}

    @classmethod
    def load_config(cls, json_file):
        with open(json_file, encoding="utf-8") as f:
            cls.app_config = json.load(f)

    @classmethod
    def get_config(cls, key_value):
        keys = key_value.split(".")
        cfg = cls.app_config.get(keys[0])
        for key in keys[1:]:
            if isinstance(cfg, dict):
                cfg = cfg.get(key)
                continue
            return None
        return cfg


# Загрузка конфигурации при запуске приложения
AppConfig.load_config("app_config.json")

# Получение значения конфигурации
assert AppConfig.get_config("database") == {
    "host": "127.0.0.1",
    "port": 5432,
    "database_name": "postgres_db",
    "user": "owner",
    "password": "ya_vorona_ya_vorona",
}
assert AppConfig.get_config("database.user") == "owner"
assert AppConfig.get_config("database.password") == "ya_vorona_ya_vorona"
assert AppConfig.get_config("database.pass") is None
assert AppConfig.get_config("password.database") is None

config = AppConfig()
assert config.get_config("max_connections") == 10
assert config.get_config("min_connections") is None

conf = AppConfig()
assert conf.get_config("max_connections") == 10
assert conf.get_config("database.user") == "owner"
assert conf.get_config("database.host") == "127.0.0.1"
assert conf.get_config("host") is None

print("Good")
