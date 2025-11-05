s = input("Nhập vào một chuỗi: ")
chuhoa = 0
chuthuong = 0
chuso = 0
kytu = 0
khoangtrang = 0
nguyenam = 0
phuam = 0
arr = list(s)
for i in arr:
    if i >= 'A' and i <= 'Z':
        chuhoa += 1
    elif i >= 'a' and i  <='z':
        chuthuong += 1
    elif i >= '0' and i <= '9':
        chuso += 1
    elif i.isalnum():
        kytu += 1 
    elif i.isspace():
        khoangtrang += 1
    
    if (i >= 'A' and i <= 'Z') or (i >= 'a' and i  <='z'):
        if i == 'A' or i=='E' or i=='I' or i=="O" or i=="U" or i == 'a' or i=='e' or i=='i' or i=="o" or i=="u":
            nguyenam += 1
        else:
            phuam += 1

print("Tổng chữ hoa:", chuhoa)
print("Tổng chũ thường:", chuthuong)
print("Tổng chữ số:", chuso)
print("Tổng ký tự đặc biệt:", kytu)
print("Tổng khoảng trắng:", khoangtrang)
print("Tổng nguyên âm:", nguyenam)
print("Tổng phụ âm:", phuam)