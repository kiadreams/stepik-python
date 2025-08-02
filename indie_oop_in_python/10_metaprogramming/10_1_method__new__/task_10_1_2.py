class BaseConfig:
    def __new__(cls, *args, **kwargs):
        instance = super(BaseConfig, cls).__new__(cls)
        instance.debug = False
        instance.log_level = "INFO"
        return instance


class EmailConfig(BaseConfig):
    def __new__(cls, *args, **kwargs):
        instance = super(EmailConfig, cls).__new__(cls)
        attrs = {
            "smtp_server": "smtp.gmail.com",
            "smtp_port": 587,
            "username": "boss_of_gym@gmail.com",
            "password": "",
        }
        instance.__dict__.update(attrs)
        return instance


class DatabaseConfig(BaseConfig):
    def __new__(cls, *args, **kwargs):
        instance = super(DatabaseConfig, cls).__new__(cls)
        attrs = {
            "db_host": "127.0.0.1",
            "db_port": 5432,
            "db_name": "cookies",
            "db_user": "admin",
            "db_password": "admin",
        }
        instance.__dict__.update(attrs)
        return instance


# Проверка работы кода-------------------------------------------------------
database_config = DatabaseConfig()

print("Database Configuration:")
print(f"Host: {database_config.db_host}")
print(f"Port: {database_config.db_port}")
print(f"Database name: {database_config.db_name}")
print(f"User: {database_config.db_user}")
print(f"Password: {database_config.db_password}")
print(f"Debug: {database_config.debug}")
print(f"Logger: {database_config.log_level}")

print()

email_config = EmailConfig()
print("SMTP server Configuration:")
print(f"Server: {email_config.smtp_server}")
print(f"Port: {email_config.smtp_port}")
print(f"User: {email_config.username}")
print(f"Password: {email_config.password}")
print(f"Debug: {email_config.debug}")
print(f"Logger: {email_config.log_level}")
