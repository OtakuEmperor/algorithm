def garage(init, final):
    step = 0
    while init != final:
        zero = init.index(0)
        if zero != final.index(0):
            carMove = final[zero]
            carTo = init.index(carMove)
            init[zero], init[carTo] = init[carTo], init[zero]
        else :
            for i in range(len(init)):
                if init[i] != final[i]:
                    init[zero], init[i] = init[i], init[zero]
                    break
        step += 1
    return step





init = [1,2,3,0,4]
final = [0,3,2,1,4]
print(garage(init, final))
