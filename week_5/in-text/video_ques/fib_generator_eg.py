def fibGen():
    fibn_1 = 1  # (n-1) term
    fibn_2 = 0  # (n-2) term
    while True:
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

f = fibGen()
for i in range (5):
    print(f.__next__())




