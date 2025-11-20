lst1 = [x for x in range(100) if x % 3 == 0]
print(lst1)

lst2 = [i*i for i in range(1, 21)]
print(lst2)

lst3 = ["1" + "0"*i for i in range(10)]
print(lst3)

lst4 = [("0"*i) + "1" + ("0"*(9-i)) for i in range(10)]
print(lst4)
