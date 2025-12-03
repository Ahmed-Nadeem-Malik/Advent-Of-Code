count: int = 0
cur: int = 50

with open("input.txt", "r") as f:
    for l in f:
        line: str = l.rstrip()

        direction: str = line[0]
        rotation: int = int(line[1:])
        movement: int = rotation % 100

        if direction == "L":
            cur = (cur - movement) % 100

        else:
            cur = (cur + movement) % 100

        if cur == 0:
            count += 1

print(count)
