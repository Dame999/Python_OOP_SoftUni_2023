def read_next(*items):
    for el in items:
        for sub_el in el:
            yield sub_el


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

