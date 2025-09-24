#Hình 1
print("Hình 1")
for i in range(0, 4, 1):
    for j in range(0, 4, 1):
        if i == 0 or i ==3 or j == 0 or j == 3:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("Hình 2")
#Hinh 2
for i in range(1, 4 + 1):
    for j in range(4 - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()

print("Hình 3")
#Hinh 3
hinh3 ="""
*
* *
*   *
* * * * * * *
        *   *
          * *
            *
"""
print(hinh3)