s = open("6.txt").read()

# z_indexes = [i for i in range(len(s)) if s[i] == "Z"]

# z[i] и z[i + 3]
# print(max(z_indexes[i + 3] - z_indexes[i] - 1 for i in range(len(z_indexes) - 3)))

length = 51

for i in range(len(s) - length + 1):
    if s[i : i + length].count("Z") <= 2:
        print(s[i : i + length])
