#Tính giờ phút giây
t = int(input("Nhập số giây: "))
gio = (t//3600) % 24
phut = (t % 3600) // 60
giay = t % 60
print(gio, "giờ", phut, "phút", giay, "giây")