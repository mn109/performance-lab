import sys

input_file = sys.argv[1]

with open(input_file, 'r') as file:
    numbers = [int(line.strip()) for line in file.readlines()]

numbers.sort()

median = numbers[len(numbers) // 2]

moves = sum(abs(number - median) for number in numbers)

print(moves)
