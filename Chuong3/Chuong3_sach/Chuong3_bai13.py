# Câu 13
def NegativeNumberInStrings(s):
    result = []
    i = 0
    while i < len(s):
        if s[i] == '-' and i+1 < len(s) and s[i+1].isdigit():
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            result.append(int(s[i:j]))
            i = j
        else:
            i += 1
    return result

s = input("Nhập chuỗi: ")
print("Các số âm trong chuỗi:", *NegativeNumberInStrings(s))
