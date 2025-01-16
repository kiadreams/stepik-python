def get_data(value):
    match value:
        # здесь продолжайте программу
        case int() | str() if isinstance(value, str) or value > 0:
            return value
        case float() if -100 <= value <= 100:
            return value
    return None


print(get_data('-1'))
