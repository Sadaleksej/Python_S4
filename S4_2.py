def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(key, (int, float, complex)):
            key = str(key)
        result[value] = key
    return result

params_dict = create_dict(a=1, b='hello', c=3.14)

for key, value in params_dict.items():
    print(f"{key}: {value}")