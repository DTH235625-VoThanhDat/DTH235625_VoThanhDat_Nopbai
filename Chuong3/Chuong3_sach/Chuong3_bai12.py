# Câu 12
s = input("Nhập chuỗi: ")

so_inhoa = sum(1 for c in s if c.isupper())
so_inthuong = sum(1 for c in s if c.islower())
so_chuso = sum(1 for c in s if c.isdigit())
so_kytudacbiet = sum(1 for c in s if not c.isalnum() and not c.isspace())
so_khoangtrang = sum(1 for c in s if c.isspace())

nguyen_am = "aeiouAEIOU"
so_nguyenam = sum(1 for c in s if c in nguyen_am)
so_phuam = sum(1 for c in s if c.isalpha() and c not in nguyen_am)

print("Số chữ IN HOA:", so_inhoa)
print("Số chữ thường:", so_inthuong)
print("Số chữ số:", so_chuso)
print("Số ký tự đặc biệt:", so_kytudacbiet)
print("Số khoảng trắng:", so_khoangtrang)
print("Số nguyên âm:", so_nguyenam)
print("Số phụ âm:", so_phuam)
