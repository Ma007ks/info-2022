numbers = [int(v) for v in open("27-a.txt").read().splitlines()][1:]

max_sum = 0

for s in range(len(numbers)):
    for f in range(s, len(numbers)):
        fragment = numbers[s : f + 1]
        fragment_sum = sum(fragment)
        if fragment_sum % 43 == 0 and fragment_sum >= max_sum:
            max_sum = fragment_sum
            print(fragment_sum, len(fragment))
