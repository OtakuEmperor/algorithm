# cant't print array

def NotRepet(string):
    temp = []
    length = 0
    for i in string:
        if i in temp:
            temp = []
        temp.append(i)
        length = max(length,len(temp))
    return str(length) + " " +  " ".join(temp)


a = "abcccdfadfagda"
print(NotRepet(a))
