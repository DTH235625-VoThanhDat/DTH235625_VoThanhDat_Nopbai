# Câu 1: Đọc toàn bộ tập tin và hiển thị nội dung

def doc_toan_bo_file(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
        print("=== Nội dung tập tin ===")
        print(noi_dung)
    except FileNotFoundError:
        print("❌ Không tìm thấy tập tin!")
    except Exception as e:
        print("❌ Lỗi khác:", e)


