#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: rouwanzi
"""
'''
货币英文转阿拉伯数字
'''
DIGIT_TALBE = {u'ZERO':0,u'ONE':1,u'TWO':2,u'THREE':3,u'FOUR':4,u'FIVE':5,u'SIX':6,u'SEVEN':7,
               u'EIGHT':8,u'NINE':9,u'TEN':10,u'ELEVEN':11,u'TWELVE':12,u'THIRTEEN':13,
               u'FOURTEEN':14,u'FIFTEEN':15,u'SIXTEEN':16,u'SEVENTEEN':17,u'EIGHTEEN':18,
               u'NINETEEN':19,u'TWENTY':20,u'THIRTY':30,u'FOURTY':40,u'FIFTY':50,
               u'SIXTY':60,u'SEVENTY':70,u'EIGHTY':80,u'NINETY':90}
CARDINAL_NUMBER = {u'THOUSAND':1000,u'MILLION':1000000,u'BILLION':1000000000,u'TRILLION':1000000000000}

def transform(eng_str):
    if not isinstance(eng_str,unicode):
        eng_str = eng_str.decode('utf8')
    
    eng_str = eng_str.upper()
    values = eng_str.split(u' ')
    
    price = 0.0
    temp = 0
    is_int = True
    for i in values:
        if i == u'AND':
            continue
        if i == u'HUNDRED':
            temp = temp * 100
        elif i in DIGIT_TALBE:
            if is_int:
                temp += DIGIT_TALBE[i]
            else:
                temp += DIGIT_TALBE[i] * 0.01
        elif i in CARDINAL_NUMBER:
            price += temp * CARDINAL_NUMBER[i]
            temp = 0
        elif i == u'CENTS':
            is_int = False
            price += temp
            temp = 0
        elif i == u'ONLY':
            price += temp
            temp = 0
    if temp != 0:
        price += temp
        temp = 0

    return price


if __name__ == '__main__':
#    import time
#    start = time.time()
#    for i in xrange(10000000):
#        eng_str = 'ONE hundred and one TRILLION TWO HUNDRED AND FOUR BILLION SIX HUNDRED AND EIGHTY \
#MILLION FOUR THOUSAND FIVE HUNDRED AND SIXTY SEVEN AND CENTS fourty eight ONLY'
#        eng_str1 = 'twenty one'
#        price = transform(eng_str)
#    print 'eng2num',time.time()-start
    eng_str = 'three hundred and twenty one trillion FOUR BILLION SIX HUNDRED AND EIGHTY \
MILLION FOUR THOUSAND FIVE HUNDRED AND SIXTY SEVEN AND CENTS fourty eight ONLY'
    price = transform(eng_str)
    print price
