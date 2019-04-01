# row = 8
# column = 8
#
# NUM = 0
#
# def setTable(table,x,y):
#     for i in range(row):
#         for j in range(column):
#             if x == i or y == j or x+y == i+j or x-y == i-j:
#                 table[i][j] += 1
#
# def eraseTable(table,x,y):
#     for i in range(row):
#         for j in range(column):
#             if x == i or y == j or x+y == i+j or x-y == i-j:
#                 table[i][j] -= 1
#
# # 判断该行是否至少存在一个安全位置
# def judge(table,x):
#     for y in range(column):
#         if table[x][y] == 0:
#             return 1
#     return 0
#
# def prResult(result):
#     table = [[0 for x in range(row)] for x in range(column)]
#     for posion in result:
#         table[posion[0]][posion[1]] = 1
#     for line in table:
#         print(line)
#
#     global NUM
#     NUM += 1
#
# def tryNext(table,x,result):
#     if x == row:
#         prResult(result)
#         print('-------------------------')
#         return
#     else:
#         if judge(table,x) == 0:
#             return
#         else:
#             for y in range(column):
#                 if table[x][y] == 0:
#                     setTable(table,x,y)
#                     result.append((x,y))
#                     tryNext(table,x+1,result)
#                     eraseTable(table,x,y)
#                     result.pop()
#         return
#
#
#
# danger = [[0 for x in range(row)] for x in range(column)]
# result = []
#
# tryNext(danger,0,result)
#
# print('total:',NUM)
#


NUM = 0

def getTab(row,col):
    return [[0 for x in range(col)] for x in range(row)]

def printResultAsTab(result,row,col):
    tab = getTab(row,col)
    for position in result:
        tab[position[0]][position[1]] = 1
    for line in tab:
        print(line)

def setTab(tab,x,y,z=1):
    # if z==1:
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                if i==x or j==y or i+j==x+y or i-j==x-y:
                    # tab[i][j] += 1
                    tab[i][j] += z
    # if z==-1:
    #     for i in range(len(tab)):
    #         for j in range(len(tab[0])):
    #             if i==x or j==y or i+j==x+y or i-j==x-y:
    #                 tab[i][j] -= 1

# def ifNotHit(tab,x):
#     for i in range(len(tab[0])):
#         if tab[x][i] < 1:
#             return 1

def serch(tab,row=0,result=[]):
    if row < len(tab):
        # if ifNotHit(tab, row):
            for i in range(len(tab[0])):
                if tab[row][i] < 1:
                    result.append((row,i))
                    setTab(tab,row,i)
                    serch(tab,row+1,result)

                    setTab(tab,row,i,-1)
                    result.pop()
    else:
        printResultAsTab(result,len(tab),len(tab[0]))
        print('-' * 20)
        global NUM
        NUM += 1



tab = getTab(8,8)
serch(tab)
print('total: ',NUM)

# setTab(tab,1,1)
# # setTab(tab,1,1,-1)
# for line in tab:
#     print(line)
# print(len(tab))
# print(len(tab[0]))
#
# if ifNotHit(tab,0):
#     print(ifNotHit(tab,1))