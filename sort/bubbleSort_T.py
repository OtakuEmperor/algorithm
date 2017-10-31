import time
def bubble_sort(list):
    change = True
    while change:
        change = False
        for i in range(1,len(list)):
            if list[i] < list[i-1]:
                tmp = list[i-1]
                list[i-1] = list[i]
                list[i] = tmp
                change = True

def main():
    array = [1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100,
             4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999]
    print(array)
    bubble_sort(array)
    print(array)


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
