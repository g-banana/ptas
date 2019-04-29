# 手动十 - 十六机制转换

def dic_to_ox(num,grad):
    rep = []
    round = num//grad
    decim = num/grad - round
    while(round):
        newpla = decim*grad
        rep.append(newpla)
        decim = round / grad - round//grad
        round = round//grad
    newpla = decim * grad
    rep.append(newpla)

    rep.reverse()
    print(rep)


dic_to_ox(20013,16)