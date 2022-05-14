s = open("7.txt").read()

length = 275

for i in range(len(s)):
    sb = s[i : i + length]
    if sb.count("E") == 0 and s.count("A") >= 3:
        print(len(sb), sb)
