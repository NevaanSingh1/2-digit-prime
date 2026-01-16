def is_two_digits(n):
    if n >= 10 and n <= 99:
        return True
    else:
        print("The number is not 2 digits.")
        return False

def is_prime(n):
    if n <= 1:
        print("This number is not prime.")
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("This number is not prime.")
            return False
    print("This number is prime.")
    return True


n = int(input("Enter a number: "))
if is_two_digits(n):
    is_prime(n)