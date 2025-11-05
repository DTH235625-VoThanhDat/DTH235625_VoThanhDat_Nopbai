# Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python.
# SyntaxError: sai cú pháp
# NameError: dùng biến chưa khai báo
# TypeError: sai kiểu dữ liệu
# ValueError: giá trị không hợp lệ
# ZeroDivisionError: chia cho 0
# Có thể bắt lỗi bằng try-except

try:
    a = int("abc")  # gây ValueError
except ValueError:
    print("Lỗi: không thể chuyển đổi chuỗi thành số nguyên")