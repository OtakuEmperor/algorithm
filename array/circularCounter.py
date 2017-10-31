a = ['1','2','3','4','5','6','7','8','9']

def circular(list,offset):
    index = 0
    offset = offset - 1
    while len(list) > 0:
        index = (offset + index) % len(list)
        print(list.pop(index))


circular(a,3)
