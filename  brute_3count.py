hh = int(input())
count = 0
for h in range(hh+1):
    for min in range(60):
        for sec in range(60):
            if "3" in str(h)+str(min)+str(sec):
                count += 1
print(count)
