n = int(input("Nhập n: "))

for i in range(2 ** n):
    print(format(i, "0{}b".format(n)))
