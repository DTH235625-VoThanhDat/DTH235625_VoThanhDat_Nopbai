# Câu 2: Đọc n dòng đầu tiên

def doc_n_dong(ten_file, n):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            for i in range(n):
                dong = f.readline()
                if not dong:     # Nếu hết file thì dừng
                    break
                print(dong, end="")
    except FileNotFoundError:
        print("❌ Không tìm thấy tập tin!")
    except Exception as e:
        print("❌ Lỗi khác:", e)


