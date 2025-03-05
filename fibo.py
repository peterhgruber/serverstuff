# short fibonacci
# peter.gruber@usi.ch, 2024-03-04

import sys

# Check if command line arguments are provided
if len(sys.argv) < 2:
    print("Please provide the number of elements to be calculated as an argument.")
    sys.exit(1)

# Get the number from command line arguments
n = int(sys.argv[1])

# Initialize the Fibonacci sequence with the first two numbers
fib = [1, 1]

# Generate the Fibonacci sequence up to the nth number
for k in range(2, n):  # Adjusting the range because Python indexing starts at 0
    fib.append(fib[k-1] + fib[k-2])

# Print the Fibonacci sequence
print(fib)
