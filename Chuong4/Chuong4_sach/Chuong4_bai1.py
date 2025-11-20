def gen_even(n):
    """Sinh n số chẵn đầu tiên từ 0: 0, 2, 4, ..."""
    for i in range(n):
        yield i * 2

def gen_squares(n):
    """Sinh n số chính phương đầu tiên: 0, 1, 4, 9, ..."""
    for i in range(n):
        yield i * i
