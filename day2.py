horizontal = 0
vertical = 0

with open("data_day2.txt") as f:
    for l in f:
        [direction, amount] = l.split(" ")
        amount = int(amount)

        if direction == "forward":
            horizontal += amount
        elif direction == "down":
            vertical += amount
        elif direction == "up":
            vertical -= amount

print(horizontal * vertical)

horizontal = 0
vertical = 0
aim = 0

with open("data_day2.txt") as f:
    for l in f:
        [direction, amount] = l.split(" ")
        amount = int(amount)

        if direction == "forward":
            horizontal += amount
            vertical += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount

print(horizontal * vertical)
