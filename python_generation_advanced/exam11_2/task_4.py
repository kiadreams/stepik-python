def build_query_string(params):
    result = [f'{key}={value}' for key, value in params.items()]
    return '&'.join(sorted(result))

