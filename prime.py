def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def print_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=' ')
            count += 1
        num += 1

#my name is gopal 
try:
    n=int(input("Enter the number of prime numbers to print: "))
    if n>0:
        print_n_primes(n)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter an integer.")

#this is v3


#now this is v4