#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: rouwanzi
"""
'''
人民币大写转阿拉伯数字
'''
CNY_TABLE = {u'零':0,u'壹':1,u'贰':2,u'叁':3,u'肆':4,u'伍':5,u'陆':6,u'柒':7,u'捌':8,u'玖':9}
CNY_UNIT = {u'拾':10,u'佰':100,u'仟':1000,u'角':0.1,u'分':0.01}
CARDINAL_NUMBER = {u'万':10000,u'亿':100000000}

def transform(cny_str):
    if not isinstance(cny_str,unicode):
        cny_str = cny_str.decode('utf8')
    
    price = 0.0
    temp = 0
    num = 0
    for i in cny_str:
        if i == u'零':
            continue
        if i in CNY_TABLE:
            num = CNY_TABLE[i]
        elif i in CNY_UNIT:
            temp += num * CNY_UNIT[i]
            num = 0
        elif i == u'万':
            temp += num
            price += temp * 10000
            temp = 0
            num = 0
        elif i == u'亿':
            temp += num
            price += temp
            price *= 100000000
            temp = 0
            num = 0
        elif i in {u'元',u'圆'}:
            temp += num
            price += temp
            temp = 0
            num = 0
    
    price += temp
    
    return price

if __name__ == '__main__':
    cny_str = '壹佰贰拾亿零叁拾肆万零陆佰壹拾叁圆零柒分'
    cny_str1 = u'壹佰贰拾伍亿'
    cny_str2 = u'壹佰贰拾伍亿零叁拾肆万'
    cny_str3 = u'陆佰壹拾叁圆'
    
    cny_str4 = u'壹佰零壹万贰仟叁佰贰拾叁亿零肆佰万零叁拾肆元贰角整'
    cny_str5 = u'贰仟叁佰贰拾叁亿零肆佰万零叁拾肆元贰角整'
    cny_str6 = u'贰佰伍拾肆亿肆仟叁佰万零陆仟伍佰零壹圆肆角捌分'
    cny_str7 = u'贰亿柒仟叁佰贰拾壹万零叁仟零伍亿壹佰贰拾叁万伍仟玖佰零壹元肆角捌分'
    price = transform(cny_str7)
    print price
#    import time
#    start = time.time()
#    for i in xrange(10000000):
#        cny_str7 = u'叁佰贰拾壹万零叁仟零伍亿壹佰贰拾叁万伍仟玖佰零壹元肆角捌分'
#        price = transform(cny_str7)
#        print price
#
#    print 'ch2num',time.time() - start
     
     

