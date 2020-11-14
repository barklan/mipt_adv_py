a = {1, 2, 3, 4, 5}
a1 = a.copy()
b = {3, 4, 5, 6, 7}
a1.symmetric_difference_update(b)
print(a1)
all = set(list(a) + list(b))
print(all)
a_l = list(a)
out = []
for i in list(a):
    if i in b:
        out.append(i)
print(set(out))