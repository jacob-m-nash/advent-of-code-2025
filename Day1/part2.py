from dial import Dial

dial = Dial(50)
zero_count = 0
past_zero = 0
with open("Day1/input.txt") as f:
    instructions = f.readlines()

for rotation in instructions:
    past_zero += dial.turn(rotation)
    if(dial.location == 0):
        zero_count += 1

print(past_zero)
