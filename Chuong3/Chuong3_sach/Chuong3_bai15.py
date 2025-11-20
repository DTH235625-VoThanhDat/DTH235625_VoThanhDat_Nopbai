# Câu 15
def is_valid_password(pw):
    if not (6 <= len(pw) <= 12):
        return False
    has_lower = any(c.islower() for c in pw)
    has_upper = any(c.isupper() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_special = any(c in "#$@" for c in pw)

    return has_lower and has_upper and has_digit and has_special

s = input("Nhập các mật khẩu, cách nhau bởi dấu phẩy: ")

passwords = [x.strip() for x in s.split(",")]
valid = [pw for pw in passwords if is_valid_password(pw)]

print("Mật khẩu hợp lệ:")
print(",".join(valid))
