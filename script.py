def generate_fibonacci_sequence(limit):
    sequence = [0, 1]

    while sequence[-1] + sequence[-2] <= limit:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

# Main program
if __name__ == "__main__":
    limit = int(input("Enter the limit for the Fibonacci sequence: "))

    fibonacci_sequence = generate_fibonacci_sequence(limit)

    print("Fibonacci sequence up to", limit, ":")
    print(fibonacci_sequence)
