def flatten_dict(d):
    res = {}
    for key, val in d.items():
        if isinstance(val, dict):
            res.update({f'{key}_{k}': v for k, v in flatten_dict(val).items()})
        else:
            res[key] = val
    return res


# print(flatten_dict({'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}))
print(flatten_dict({'Germany_berlin': 7,
                    'Europe_italy_Rome': 3,
                    'USA_washington': 1,
                    'USA_New York': 4}))
print(flatten_dict({'Q': {'w': 123, 'a': 1}}))

print(flatten_dict({"a": 1,
                    "b": {
                        "c": 2,
                        "d": 3,
                        "e": {
                            "f": 4,
                            '6': 100,
                            '5': {"g": 6},
                            "l": 1,
                        }
                    }}))