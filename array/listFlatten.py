import time
def listFlatten(l, a=None):
    a = list(a) if isinstance(a, (list, tuple)) else []
    for i in l:
        if isinstance(i, (list, tuple)):
            a = listFlatten(i, a)
        else:
            a.append(i)
    return a

def main():
    list = [2, 1, [3, [4, 5], 6], 7, [8]]
    print(listFlatten(list))


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
