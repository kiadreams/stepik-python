def uppercase_elements(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, dict):
            return {
                k.upper() if isinstance(k, str) else k: v
                for k, v in res.items()
            }
        res_type = type(res)
        return res_type(
            e.upper() if isinstance(e, str) else e for e in res
        )

    return wrapper
