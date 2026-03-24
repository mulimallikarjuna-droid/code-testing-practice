def divide(a, b):
    return a / b
def divide_fixed(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def is_even(n):
    if n % 2 == 1:
        return True
    return False

def is_even_fixed(n):
    return n % 2 == 0

print(divide_fixed(10, 0))
print(is_even_fixed(4))
