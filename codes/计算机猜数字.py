
class tryNum:
    '''
    作用：根据取得信息猜测数字总类：
    规则：四位数字各位非0且相互不重复；每猜测一次用户输入数字正确个数、数字正确且位置正确个数
    实现原理：列出所有组合集合，根据条件每轮进行筛选，最后剩下一个正确答案
    '''

    def __init__(self,value = 1234):
        '''
        构造猜数对象，调用自身函数初始化包含所有可能结果的集合；可指定首次猜测的数值
        :param value: 首次猜测数值
        '''
        self.firstValue = value
        self.__numbs = set(self.__getSet())
        pass

    def res(self):
        '''
        重置集合
        :return:None
        '''
        self.__numbs = set(self.__getSet())

    def __getSet(self):
        '''
        供调用获取初始参数
        :return:包含所有可能结果的迭代器
        '''
        return filter(lambda x:str(x)[0] != str(x)[1] != str(x)[2] != str(x)[3] \
                               and str(x)[0] != str(x)[3] != str(x)[1] and str(x)[0] != str(x)[2] \
                               and str(x)[0] != '0' and str(x)[1] != '0' and str(x)[2] != '0' and str(x)[3] != '0',
                      {x for x in range(1234,9877)})

    def shrink(self,lastValue,numb_correct,posi_correct = -1):
        '''
        核心函数，根据传入值缩减可能的答案范围，更新初始迭代器为可变集合
        ：param lastValue: 上一猜测数值
        :param numb_correct: 正确数字个数
        :param posi_correct: 正确数字和位置个数
        :return: 返回列表第一个数值，判定无答案则或者参数错误抛出相应错误类
        '''
        numbat = set()
        for numb in self.__numbs:
            a,b = 0,0
            nubstr = str(numb)
            lastValueStr =str(lastValue)
            for i in range(4):
                if nubstr[i] in lastValueStr:
                    a += 1
                if nubstr[i] is lastValueStr[i]:
                    b += 1
            if a is numb_correct and (b is posi_correct or posi_correct < 0):
                numbat.add(numb)
        # print(numbat,self.__numbs,a,b,lastValueStr,numb_correct,posi_correct)
        if not numbat:
            raise UserDataError('用户输入数据前后矛盾，该失误不可回溯。')
        self.__numbs = numbat
        return self.__numbs.pop()


class BusiError(Exception):
    '''程序异常错误信息总类'''
    pass

class UserInputError(BusiError):
    '''用户输入格式错误
    err_input: 用户错误的输入
    err_info: 记录提示信息
    '''
    def __init__(self,err_input,out_info):
        self.err_input = err_input
        self.out_info = out_info


class UserDataError(BusiError):
    '''用户输入数据失误错误
    err_info: 记录提示信息
    '''
    def __init__(self,info = None):
        self.err_info = info




import re
import win32com.client

# help(tryNum)
fac = tryNum()
speaker = win32com.client.Dispatch("SAPI.SpVoice")

#以下为业务逻辑部分：
speaker.speak("准备好了吗晓丽小仙女")
while True:
    print('计算机：准备猜数？\t(开始:yes，猜对:ok，\
    没猜对请输入数字猜对个数+半角逗号+位置猜对个数，如：2,1)')
    # speaker.speak('准备猜数？\t(开始:yes，猜对:ok，\
    # 没猜对请输入数字猜对个数+半角逗号+位置猜对个数，如：2,1)')
    reply = input('人：')
    if reply == 'yes':
        value = fac.firstValue
        flag = True
        while True:
            print('计算机：', value)
            speaker.speak(value)
            get_in = input("人：")
            if get_in == 'ok':
                break
            while not re.match('[0-9],[0-9]', get_in) and get_in is not 'ok':
               get_in = input('命令格式错误，请重新输入：')
            get_in = get_in.split(',')
            if not(int(get_in[0]) in range(5) and int(get_in[0]) >= int(get_in[1])):
                print('数据明显错误，此次判定跳过')
                continue

            try:
                value = fac.shrink(value, int(get_in[0]), int(get_in[1]))
            except userdataerror as err:
                print(err.err_info,'\t请开始新一轮。')
                flag = False
                break;
        fac.res()
        if flag:
            speaker.speak('太棒啦，我已猜对数字：{}\t\t本轮已完成，可继续进入下一轮。')
            print('已猜对数字：{}\t\t本轮已完成，可继续进入下一轮。'.format(value))
        print()
    else:
        break
print('计算机：程序结束。')


# print(len(fac._tryNum__numbs),6*7*8*9)

