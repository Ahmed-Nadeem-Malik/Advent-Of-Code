with open("input.txt", "r") as f:
    data = f.readline().rstrip()
    ranges = data.split(",")


total = 0
for r in ranges:
    start, end = r.split("-")

    for i in range(int(start), int(end) + 1):
        string: str = str(i)

        if len(string) % 2 != 0:
            continue

        firstPart, secondPart = string[: len(string) // 2], string[len(string) // 2 :]

        if firstPart == secondPart:
            total += i

print(total)
