def sort_dict_values(dic):
    values = list(dic.values())
    asc = sorted(values)
    desc = sorted(values, reverse=True)
    return asc, desc

# Ví dụ
d = {'a': 12, 'b': 5, 'c': 20, 'd': 7}
tang, giam = sort_dict_values(d)
print("Tăng:", tang)
print("Giảm:", giam)
