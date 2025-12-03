with open("Day3/input.txt") as f:
    batteries = f.readlines()
sum = 0
for battery in batteries:
    battery = battery.rstrip()
    p1 = 0
    p2 = 1
    tens = int(battery[p1])
    units = int(battery[p2])
    while(p2 < len(battery)):
        if(int(battery[p2]) > tens and p2 < len(battery) - 1 ):
            p1 = p2
            tens = int(battery[p1])
            p2+= 1
            units = int(battery[p2])
            continue
        if(int(battery[p2]) > units ):
            units = int(battery[p2])

        p2 +=1
    
    sum += tens * 10 + units

print(sum)
