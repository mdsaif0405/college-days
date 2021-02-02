def _data(a, **b):
    print(a, b)
    # print(type(b))
    for x, y in b.items():
        print(x, "=", y)


_data(7, x=4, y=6, f=0, e=6, q=7)
