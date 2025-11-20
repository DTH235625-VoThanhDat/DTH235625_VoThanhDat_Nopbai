def concatenate_dict(d1, d2):
    result = d1.copy()
    result.update(d2)
    return result

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
print(concatenate_dict(dic1, dic2))
