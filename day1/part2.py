cur = 50
count = 0

with open("input.txt", "r") as f:
    for line in f:
        direction = line[0]
        rotation = int(line[1:].strip())

        movement = rotation % 100
        full = rotation // 100
        count += full

        for _ in range(movement):
            if direction == "L":
                cur = (cur - 1) % 100
            else:
                cur = (cur + 1) % 100

            if cur == 0:
                count += 1

print(count)

