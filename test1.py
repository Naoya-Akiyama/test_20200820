no = int(input())
sox = []
type_s = []
for i in range(no):
    x = list(input().split())
    type_s.append(x[0])
    sox.append(x)
type_s = list(set(type_s))

new_type = []
for l in type_s:
    new_type.append(l + 'R')
    new_type.append(l + 'L')

no_type = [0]*len(new_type)
new_type = dict(zip(new_type, no_type))

x = 0
for j in type_s:
    for k in range(no):
        if sox[k][0] == j and sox[k][1] == 'R':
            new_type[j+'R'] += 1
        elif sox[k][0] == j and sox[k][1] == 'L':
            new_type[j+'L'] += 1
        else:
            x += 1

total = 0
for k in type_s:
    total += min(new_type[k+'R'], new_type[k+'L'])

print(total)
            