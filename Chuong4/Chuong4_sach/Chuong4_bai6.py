import random

def tao_list_random(n):
    return [random.randint(0, 100) for _ in range(n)]

def xoa_phan_tu(lst, k):
    return [x for x in lst if x != k]

def doi_xung(lst):
    return lst == lst[::-1]
