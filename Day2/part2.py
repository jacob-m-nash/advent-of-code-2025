from functools import reduce

def factors_list(n) :
    return sorted(set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))), reverse=True)


invalid_total = 0
with open("Day2/input.txt") as f:
    ranges = f.readlines()
for id_range in ranges[0].split(","):
    lower,upper = id_range.split("-")
    factors = {i: factors_list(i) for i in range(len(lower),len(upper)+1)}
    for i in range(int(lower),int(upper)+1):
        valid = True
        number = str(i)
        number_len = len(number)
        if(number_len < 2):
            continue
        for factor in factors[number_len]:
            if(factor == number_len):
                continue
            a = number[:factor]
            for j in range(factor,number_len,factor):
                b = number[j:j+factor]
                if(a == b):
                    valid = False
                else:
                    valid = True
                    break
            if(not valid):
                break

        if(not valid):
            invalid_total += i
            
print(invalid_total)
    