# Key Programming Activities Program

# Function to calculate the factorial of a number
def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

# Function to check if a number is prime
def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Main program
if __name__ == "__main__":
    # Take user input
    number = int(input("Enter a positive integer: "))

    # Calculate and display the factorial of the number
    factorial = calculate_factorial(number)
    print("Factorial of", number, "is", factorial)

    # Check if the number is prime and display the result
    is_prime = check_prime(number)
    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")
