#In bảng cửu chương từ 2 đến 9
for i in range(1, 11, 1):
    for j in range(2, 10, 1):
        print(f"{j} x {i} = {i * j}", end="\t")
    print()