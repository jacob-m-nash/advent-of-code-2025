from dataclasses import dataclass
@dataclass(slots=True)
class Number:
    value: int
    index: int

with open("Day3/input.txt") as f:
    batteries = f.readlines()
sum = 0

for battery in batteries:
    battery = battery.rstrip()

    numbers = [
    Number(value = -1, index = x)
    for x in range(len(battery) - 12, len(battery))
    ]

    for i in range(numbers[0].index, -1, -1):
        if(int(battery[i]) >= numbers[0].value):
            numbers[0].value = int(battery[i])
            numbers[0].index = i

    for j in range(1,len(numbers)):
        for i in range(numbers[j].index, numbers[j-1].index, -1):
            if(int(battery[i]) >= numbers[j].value):
                numbers[j].value = int(battery[i])
                numbers[j].index = i
    
    s = "".join(str(n.value) for n in numbers)
    sum += int(s)
print(sum)