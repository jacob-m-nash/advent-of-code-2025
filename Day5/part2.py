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
        input_range = line.rstrip().split("-")
        ranges.append(Range(int(input_range[0]),int(input_range[1])))


sorted_ranges = sorted(ranges, key=lambda r: r.lower)

merged_ranges = [sorted_ranges[0]]
for i in range(1,len(sorted_ranges)):
    prev_range = merged_ranges[-1]
    range = sorted_ranges[i]
    if(range.lower > prev_range.upper):
        merged_ranges.append(range)
        continue
    if(range.upper > prev_range.upper):
        prev_range.upper = range.upper

fresh_ids_total = 0
for range in merged_ranges:
    fresh_ids_total += (range.upper - range.lower) + 1

print(fresh_ids_total)