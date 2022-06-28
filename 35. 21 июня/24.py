s = "BABOCAODODAOCACOBABODOABABO"

s = s.replace("BA", "+")
s = s.replace("CA", "+")
s = s.replace("DA", "+")
s = s.replace("BO", "+")
s = s.replace("CO", "+")
s = s.replace("DO", "+")
# for x in "AO":
#     for y in "BCD":
#         s = s.replace(y + x, "+")

for x in "ABCDO":
    s = s.replace(x, " ")

groups = s.split()

for g in groups:
    if len(g) > 3:
        print(g, len(g))