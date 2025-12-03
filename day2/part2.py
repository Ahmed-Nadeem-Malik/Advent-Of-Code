with open("input.txt", "r") as f:
    data = f.readline().rstrip()
    ranges = data.split(",")


total = 0
for r in ranges:
    start, end = r.split("-")

    for i in range(int(start), int(end) + 1):
        string: str = str(i)
        res = string in (string + string)[1:-1]
        if res:
            total += i

print(total)
