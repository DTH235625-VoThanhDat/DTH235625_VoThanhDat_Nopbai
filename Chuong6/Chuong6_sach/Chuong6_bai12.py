# Câu 12a

def doc_danh_sach_so(filename):
    ds = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            nums = list(map(int, line.strip().split(",")))
            ds.append(nums)
    return ds

# Câu 12b

def xuat_so_am(ds):
    for dong in ds:
        am = [x for x in dong if x < 0]
        print(am)
