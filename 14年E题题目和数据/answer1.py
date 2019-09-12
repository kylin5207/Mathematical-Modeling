# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 20:06:33 2019
建模比赛——乘用车运输第一题：
运输I型乘用车100辆，II型乘用车68辆
对于1-1型轿运车只用考虑长度是否满足，而1-2型轿运车需要考虑长度和宽度
@author: Kylin
"""
import numpy as np

def onlytunk1():
    """
    如果只用1-1型轿运车来运输车辆，只用考虑轿运车的长度是否够用\
    返回值：
        classifylist:单层存放方案
        carnumlist：双层存放方案
        carnum:去重后的车辆存放总数
    """
    print("-------全用1-1型轿运车来运输车辆------")
    tunk_length = 19
    car1_length = 4.61+0.1 #这里加上0.1是因为每辆车之间有0.1m间距
    car2_length = 3.615+0.1
    k = 0 #记录可行方案数
    classifylist = [] #存放方案数据
    
    print("单层存放方案：")
    #如果全放1型车，可以放四辆
    for i in range(5):
        #记录剩余容量
        surplus = tunk_length - i * car1_length
    
        #如果全放II，可以放5辆
        for j in range(6):
            surplus2 = surplus - j * car2_length
            if surplus2 < car2_length:
                #这里只记录放满的情况，其他情况不予考虑
                print("car1:", i, "car2:", j, end=" ")
                print("surplus:", surplus2+0.1) #n辆车之间的间隔为0.1*(n-1)，这里多剪掉了一个0.1m，加回去
                k += 1
                classifylist.append([i,j,surplus2+0.1]) #将信息存入list中，后期便于操作
                break
    
    print("单层存放乘用车共{}种方案\n".format(k))
    
    
    #计算每种方案存放的Ⅰ型车和Ⅱ型车总车辆数
    carnumlist = []
    
    print("双层存放方案：")
    for i in range(len(classifylist)):
        for j in range(i, len(classifylist)):
            car1num = int(classifylist[i][0]) + int(classifylist[j][0])
            car2num = int(classifylist[i][1]) + int(classifylist[j][1])
            print("(方案{},方案{}) car1:{}, car2:{}".format(i, j, car1num, car2num))
            carnumlist.append([car1num,car2num])
    print("双层总方案有{}种".format(len(carnumlist)))
    
    print("统计总共存放的车辆数：")
    carnum = np.array(carnumlist)
    
    carnum = np.array(list(set([tuple(t) for t in carnumlist])))
    print(carnum)
    print("(去重后)存放车辆总数，共有：{}种".format(len(carnum)))
    
    return classifylist, carnumlist, carnum

def onlytunk2():
    """
    如果只用1-2型轿运车来运输车辆，不仅考虑轿运车的长度是否够用，还要考虑上层的宽是否够用
    """
    
    print("-------全用1-2型轿运车来运输车辆------")
    
    #考虑上层的计算方法
    tunk_length = 24.3
    tunk_width2 = 3.5
    
    car1_length = 4.61 + 0.1 #这里加上0.1是因为每辆车之间有0.1m间距
    car1_width = 1.7 + 0.1
    car2_length = 3.615 + 0.1
    car2_width = 1.605 + 0.1 
    
    k = 0 #记录可行方案数
    downclassifylist = [] #存放下层方案数据
    upclassifylist = [] #存放上层方案数据
    
    print("单层存放方案：")
    #如果全放1型车，可以放5辆
    for i in range(6):
        #记录剩余容量
        surplus = tunk_length - i * car1_length
    
        #如果全放II，可以放6辆
        for j in range(7):
            surplus2 = surplus - j * car2_length
            if surplus2 < car2_length:
                #这里只记录放满的情况，其他情况不予考虑
                print("car1:", i, "car2:", j, end=" ")
                print("surplus:", surplus2+0.1) #n辆车之间的间隔为0.1*(n-1)，这里多剪掉了一个0.1m，加回去
                k += 1
                downclassifylist.append([i,j,surplus2+0.1]) #将信息存入list中，后期便于操作
                break
    
    print("单层存放乘用车共{}种方案\n".format(k))
    print(downclassifylist)
    
    #上层两列力求对称，表明两列选择的车辆是一样的，还要排放一致。
    for i in range(len(downclassifylist)):
        car1num, car2num = downclassifylist[i][0], downclassifylist[i][1]
        print(car1num, car2num)
        
        if car1num == 0:
            surplus = tunk_width2 - 2 * car2_width + 0.1
            
        else:
            surplus = tunk_width2 - car1_width - car2_width + 0.1
        
        if surplus > 0:
            upclassifylist.append([i,i,car1num*2, car2num*2, surplus])
    print(upclassifylist)
    
#    #如果全放1型车，可以放四辆
#    for i in range(5):
#        #记录剩余容量
#        surplus = tunk_length - i * car1_length
#    
#        #如果全放II，可以放5辆
#        for j in range(6):
#            surplus2 = surplus - j * car2_length
#            if surplus2 < car2_length:
#                #这里只记录放满的情况，其他情况不予考虑
#                print("car1:", i, "car2:", j, end=" ")
#                print("surplus:", surplus2+0.1) #n辆车之间的间隔为0.1*(n-1)，这里多剪掉了一个0.1m，加回去
#                k += 1
#                classifylist.append([i,j,surplus2+0.1]) #将信息存入list中，后期便于操作
#                break
#    
#    
#    print(classifylist)
#    print("单层存放乘用车共{}种方案".format(k))
#    
#    #计算每种方案存放的Ⅰ型车和Ⅱ型车总车辆数
#    carnumlist = []
#    for i in range(len(classifylist)):
#        for j in range(i, len(classifylist)):
#            car1num = int(classifylist[i][0]) + int(classifylist[j][0])
#            car2num = int(classifylist[i][1]) + int(classifylist[j][1])
#            carnumlist.append([car1num,car2num])
#    
#    carnum = np.array(carnumlist)
#    #去除重复的项，最开始想用unique，但是unique无法实现对二维数据的去重
#    carnum = np.array(list(set([tuple(t) for t in carnumlist])))
#    print(carnum)
#    
#    print("存放车辆总数，共有：{}种".format(len(carnum)))
#    
#    return classifylist

if __name__ == "__main__":
    
#    tunk1classify, car1numlist, car1num = onlytunk1()
    onlytunk2()