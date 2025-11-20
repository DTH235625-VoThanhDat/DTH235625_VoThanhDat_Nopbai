def process_array(arr):
    odd = [x for x in arr if x % 2 == 1]
    even = [x for x in arr if x % 2 == 0]
    
    def is_prime(n):
        if n < 2: 
            return False
        for i in range(2, int(n**0**5)+1):
            if n % i == 0:
                return False
        return True
    
    primes = [x for x in arr if is_prime(x)]

    print("Dòng 1:", odd, "- Tổng số lẻ:", len(odd))
    print("Dòng 2:", even, "- Tổng số chẵn:", len(even))
    print("Dòng 3:", primes)
