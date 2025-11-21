# Câu 7

def ghi_so_1_10(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(1, 11):
            f.write(str(i) + "\n")
