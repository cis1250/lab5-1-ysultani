def get_positive_integer():
    while True:
        try:
            num = int(input("Enter the number of terms: "))
            if num > 0:
                return num
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def print_fibonacci(seq):
    print("Fibonacci sequence:", seq)

def main():
    n = get_positive_integer()
    seq = generate_fibonacci(n)
    print_fibonacci(seq)

main()
