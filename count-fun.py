# /usr/bin/python
# coding=utf-8
import re

__author__ = 'mengfan'
class CountFun:
   # def __init__(self, x, y):
       # self.x = x
        #self.y = y

    #@classmethod
    #直接调用方法名方法名

    def jia(self, x, y):
        print x + y

    def jian(self, x, y):
        print x - y

    def cheng(self, x, y):
        print x * y

    def chu(self, x, y):
        print x / y

#CountFun.jia(3,5)
f = CountFun()
countswitch = {'+': f.jia, '-': f.jian, '*': f.cheng, '/': f.chu}

def f(x, o, y):
    countswitch.get(o)(x,y)

#f(3,'+',1)

input_count = raw_input('请输入你要执行的运算:\n')
reinput = re.split('(\D+)',input_count)
print reinput[0],reinput[1],reinput[2]

f(int(reinput[0]),reinput[1],int(reinput[2]))
# >>> re.split('(\D+)','424234+2344')
# ['424234', '+', '2344']




