
# def some(x):
#     yield x - 2
#     yield x - 3
#     yield x - 4
#
# tmp = some(10)
# print(list(tmp))
# for itm in tmp:
#     print(itm)

def some2(x,y):
    for n in range(y):
        print("Pre Yield")
        yield (n+x)**y
        print("Post Yield")
    print("Cycle end")

tmp=some2(2,5)

print(next(tmp))
print(next(tmp))
print(next(tmp))
print(next(tmp))
print(next(tmp))
