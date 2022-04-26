lines = open("6.txt").read().splitlines()[1:]
lists = [[int(v) for v in line.split()] for line in lines]

# lists = []
#
# for line in lines:
#     nums = [int(v) for v in line.split()]
#     lists.append(nums)
