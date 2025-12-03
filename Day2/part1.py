invalid_total = 0
with open("Day2/input.txt") as f:
    ranges = f.readlines()
for id_range in ranges[0].split(","):
    lower,upper = id_range.split("-")
    for i in range(int(lower),int(upper)):
        number_string = str(i)
        word_length = len(number_string)
        half = int(word_length/2)
        if(word_length %2 != 0):
            continue
        a = number_string[:half]
        b = number_string[half:]
        if(a == b):
            invalid_total += i

print(invalid_total)


