import random

row = 2
col = 2
win = 3


chess = [[ 0 for i in range(col)] for i in range(row)]
for i in range(row):
    for j in range(col):
        chess[i][j] = i*row + j+1

chess_flat = []
for i in chess:
    chess_flat.extend(i)

path = []
all_state = {'first_win': [[]], 'second_win': [[]], 'draw': [[]]};

def __iter_fun(chess_flat:list,path:list):
    for sing in chess_flat:
        # 如果当前路径(path)中已包含该位置，则跳过
        if sing in path:
            continue

        #调用接口判断结果，若分出胜负, 保存结果并继续下一分支遍历
        path.append(sing)
        result = get_result(path)
        if result == 1 or result == -1 or result == 0:
            res = {1: 'first_win', -1: 'second_win', 0: 'draw'}
            all_state[res[result]].append( path.copy() )

        # 未结束继续下一层遍历
        __iter_fun(chess_flat,path)

        # 该分支遍历结束继续遍历该层次下一分支
        path.remove(sing)
        continue





me_win = 2
def feedback(player_posion:tuple = 0,who_win:int = me_win):
    if not player_posion:
        me_win = 1
        first_ai_posiion = random.randint(1,row*col + 1)
        shrink(first_ai_posiion)

        x = (first_ai_posiion-1)//col + 1
        y = (first_ai_posiion-1)%col + 1
        return (x,y)

    ai_position = (player_posion[0]-1)*col + player_posion[1]
    shrink(ai_position)
    next = calculate(who_win)

    x = (next - 1) // col + 1
    y = (next - 1) % col + 1
    return (x,y)


def shrink(ai_position:int):
    for key,values in all_state.items():
        len = values.__len__()
        for reverse_index in range(len-1,-1,-1):
            if values[reverse_index][0] != ai_position:
                values.pop(reverse_index)

def calculate(who_win , regula:list = [1,-1,0]):
    refer = {}
    res = { 'first_win':regula[0],  'second_win':regula[-1],  'draw':regula[0]}
    for key, values in all_state.items():
        for value in values:
            if value[0] not in refer:
                refer[value[0]] = res[key]
            else:
                refer[value[0]] += res[key]

    if me_win == 2:
        return max(refer, key = dict.get)
    return min(refer, key = dict.get)



