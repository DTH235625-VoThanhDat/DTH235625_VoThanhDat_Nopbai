# Câu 6: Tần suất từ

from collections import Counter

def tan_suat_tu(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        words = f.read().split()

    freq = Counter(words)
    for w, c in freq.items():
        print(w, ":", c)
