a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
ch = input("Nhập ký tự ch: ")
if( ch == '+'):
    print("Kết quả là: ", a + b)
elif( ch == '_'):
    print("Kết quả là: ", a - b)
elif(ch == '*'):
    print("Kết quả là: ", a * b)
elif(ch == '/'):
    print("Kết quả là: ", a / b)
else:
    print("Ký tự ch không phải là một toán tử!")