from dataclasses import dataclass
@dataclass(slots=True)
class Range:
    lower: int
    upper: int

ranges = []
ids = []
with open("Day5/input.txt") as f:
    while True:
        line = f.readline()
        if(line == "\n"):
            break
        range = line.rstrip().split("-")
        ranges.append(Range(int(range[0]),int(range[1])))

    for id in f:
        ids.append(int(id.rstrip()))

sorted_ranges = sorted(ranges, key=lambda r: r.lower)


fresh = 0
for id in ids:
    for range in sorted_ranges:
        if(id >= range.lower and id <= range.upper):
            fresh += 1
            break
        
print(fresh)
