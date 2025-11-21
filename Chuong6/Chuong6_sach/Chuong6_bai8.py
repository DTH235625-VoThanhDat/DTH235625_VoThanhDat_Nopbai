# Câu 8

def doc_data71(filename="data71.txt"):
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
