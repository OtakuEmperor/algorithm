def garage(init, final):
    step = 0
    while init != final:
        zero = init.index(0)
        if zero != final.index(0):
            finalZero = final.index(0)
            index[zero], index[finalZero] = index





init = [1,2,3,0,4]
final = [0,3,1,2,4]
print(garage(init, final))
