exchange_rates = {
    "USD": 1.0,
    "EUR": 0.861775,
    "GBP": 0.726763,
    "INR": 75.054725,
    "AUD": 1.333679,
    "CAD": 1.237816,
    "SGD": 1.346851,
}


def convert(cur1, cur2, value):
    return round(exchange_rates[cur2] / exchange_rates[cur1] * value, 2)


currency = convert("USD", "EUR", 100)
print(currency)

currency = convert("EUR", "USD", 100)
print(currency)