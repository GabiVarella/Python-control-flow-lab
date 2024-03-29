# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

n1 = 0
n2 = 1
count = 0
termCount = 51
if termCount <= 0:
    print("Please enter a positive number!")
elif termCount == 1:
    print(f'Fibonacci sequence up to {termCount} is {n1}')
else: 
    print(f'Fibonacci sequence up to {termCount} is: ')
    while termCount > count:
        fib = n1 + n2
        print(f"term: {count} / number: {fib}")
        n1 = n2
        n2 = fib
        count += 1