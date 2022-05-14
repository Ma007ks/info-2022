s = open("1.txt").read()

print(s[:100])
s = s.replace("%!", "% !")
s = s.replace("%?", "% ?")
s = s.replace("?!", "? !")
s = s.replace("?%", "? %")
s = s.replace("!?", "! ?")
s = s.replace("!%", "! %")

print(s[:100])

for w in s.split():
    if len(w) >= 16:
        print(len(w), w)
