def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    result = f"A : {a}\nB : {b}"
    return result

if __name__ == "__main__":
    print(swap_numbers(5, 10))
