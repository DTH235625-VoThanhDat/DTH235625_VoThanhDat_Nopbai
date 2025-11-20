def khoi_tao():
    return []

def them(lst, x):
    lst.append(x)

def dem_phan_tu(lst, k):
    return lst.count(k)

def tong_so_nguyen_to(lst):
    def is_prime(n):
        if n < 2: 
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    return sum(x for x in lst if is_prime(x))

def sap_xep(lst):
    lst.sort()

def xoa_list(lst):
    lst.clear()
