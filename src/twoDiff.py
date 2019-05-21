# Kash: Find unique numbers from a list that have a given difference

pairs =set()

target = 1
list = [1,2,3,4,2]

for i in range(len(list)-1):
    for j in range(1,len(list)):
        tuple = (list[i],list[j])
        if list[j] - list[i] == target:
            if not tuple in pairs:
                pairs.add(tuple)

print(tuple)
        