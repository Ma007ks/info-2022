lines = open("7.txt").read().splitlines()

for line in lines:
    a, b, c = map(float, line.split())
    # a, b, c = line.split()
    # a = float(a)
    # b = float(b)
    # c = float(c)
    print(a + b + c)

triples = [sum(float(v) for v in line.split()) for line in lines]

print(triples)
