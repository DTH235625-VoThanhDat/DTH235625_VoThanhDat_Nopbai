nam = int(input("Nhập vòa một năm: "))
if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
    print(f"{nam} là năm nhuần")
else:
    print(f"{nam} không phải là năm nhuần")