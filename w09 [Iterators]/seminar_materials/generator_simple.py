def even():
    curr = 0
    while curr < 10:
        yield curr
        curr += 2


gen = even()
# next(gen)
for i in range(10):
    print(next(gen))
# for i in gen:
#     print(i)

