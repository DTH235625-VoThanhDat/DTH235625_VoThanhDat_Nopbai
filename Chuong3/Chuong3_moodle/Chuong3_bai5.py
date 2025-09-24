cases = {
    "a": (3, 5, 7),
    "b": (3, 7, 5),
    "c": (5, 3, 7),
    "d": (5, 7, 3),
    "e": (7, 3, 5),
    "f": (7, 5, 3),
}

for name, (i, j, k) in cases.items():
    # thuật toán trong đề
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print(f"({name}) i = {i}, j = {j}, k = {k}")

    #Kết quả xuất ra màn hình
    #(a) i = 5, j = 5, k = 7
    #(b) i = 3, j = 5, k = 5
    #(c) i = 7, j = 3, k = 7
    #(d) i = 5, j = 3, k = 3
    #(e) i = 5, j = 3, k = 5
    #(f) i = 7, j = 7, k = 3