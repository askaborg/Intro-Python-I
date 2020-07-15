def prime(num):
    if (num <= 1):
        return False
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True
print(prime(23))
print(prime(16))