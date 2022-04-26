lines = open("4.txt").read().splitlines()
numbers = [int(line) for line in lines]
count = numbers.pop(0)

# count, *numbers = map(int, open("4.txt").readlines())

print(count)
print(numbers[0] + numbers[1])
