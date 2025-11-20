def sum_and_product(dic):
    total = sum(dic.values())
    product = 1
    for v in dic.values():
        product *= v
    return total, product

# Ví dụ
d = {'a': 2, 'b': 3, 'c': 4}
tong, tich = sum_and_product(d)
print("Tổng:", tong)
print("Tích:", tich)
