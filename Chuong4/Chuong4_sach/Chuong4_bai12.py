def combine_dict(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        if k in result:
            result[k] = max(result[k], v)
        else:
            result[k] = v
    return result

d1 = {'a':100, 'b':200}
d2 = {'a':300, 'y':200}
print(combine_dict(d1, d2))
