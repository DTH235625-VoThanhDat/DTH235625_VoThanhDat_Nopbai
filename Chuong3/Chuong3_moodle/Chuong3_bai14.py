a = 0
while a < 100:
    b = 0
    while b < 40:
        if(a + b) % 2 == 0:
            print('*', end='')
        b += 1
    print()
    a += 1

#Giải thích:
#Vòng lặp ngoài: a chạy từ 0 đến 99 (100 lần)
#Vòng lặp trong: b chạy từ 0 đến 39 (40 lần)
#Điều kiện (a + b) % 2 == 0 đúng với 20 giá trị của b trên mỗi dòng (vì cứ 2 số thì có 1 số chẵn)
#Tổng số dấu *: 100 x 20 = 2000
#Kết luận:
#Có 2000 dấu * được in ra trong toàn bộ quá trình chạy chương trình.