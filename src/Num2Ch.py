#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
阿拉伯数字转人民币大写
'''
import math
from decimal import Decimal

DIGIT_TABLE = {0:'零',1:'壹',2:'贰',3:'叁',4:'肆',5:'伍',6:'陆',7:'柒',8:'捌',9:'玖'}
DIGIT_UNIT = {1:'',10:'拾',100:'佰',1000:'仟',10000:'万'}

def _handle_int_part(num,cny_str,zero_before,is_head=False):
    assert num > 0 and num < 10000
    
    num_of_place = int(math.log10(num)) + 1
    if num_of_place < 4 and not is_head:
        zero_before += 1
    for i in xrange(num_of_place,0,-1):
        number = num/(10**(i-1))%10
        if number != 0:
            if zero_before > 0:
                cny_str += '零'
                zero_before = 0
            cny_str += DIGIT_TABLE[number] + DIGIT_UNIT[10**(i-1)]
        elif number == 0:
            zero_before += 1
    
    return cny_str,zero_before
            

def _handle_dec_part(decimal,integer,cny_str,zero_before=False):
    assert decimal > 0 and decimal < 100
    
    if zero_before > 0 and decimal > 0 and integer > 0:
        cny_str += '零'
    for i in xrange(2,0,-1):
        number = decimal/(10**(i-1))%10
        if i == 2 and number == 0 and zero_before == 0 and integer > 0:
            cny_str += '零'
        elif i == 2 and number != 0:
            cny_str += DIGIT_TABLE[number] + '角'
        elif i == 1 and number == 0:
            cny_str += '整'
        elif i == 1:
            cny_str += DIGIT_TABLE[number] + '分'
    
    return cny_str


def transform(price):
    price_cn = ''
    price = Decimal('{:.2f}'.format(Decimal(price)))
    
    integer = int(price)
    decimal = int(price * 100 % 100)
    
    wanyi = integer / 1000000000000
    yi = integer / 100000000 % 10000
    wan = integer / 10000 % 10000
    ge = integer % 10000
    
    zero_before = 0
    if wanyi > 0:
        price_cn, zero_before = _handle_int_part(wanyi,price_cn,zero_before,True)
        if yi > 0:
            price_cn += '万'
        else:
            price_cn += '万亿'
    
    if yi > 0:
        is_head = integer >= 100000000 and integer < 1000000000000
        price_cn, zero_before = _handle_int_part(yi,price_cn,zero_before,is_head)
        price_cn += '亿'
        
    if wan > 0:
        is_head = integer >= 10000 and integer < 100000000
        price_cn, zero_before = _handle_int_part(wan,price_cn,zero_before,is_head)
        price_cn += '万'
    
    if ge > 0:
        is_head = integer >= 0 and integer < 10000
        price_cn, zero_before = _handle_int_part(ge,price_cn,zero_before,is_head)
    
    if integer > 0:
        price_cn += '元'
    
    if decimal > 0:
        price_cn = _handle_dec_part(decimal,integer,price_cn,zero_before)
    elif decimal == 0 and integer > 0:
        price_cn += '整'
    else:
        price_cn += '零元整'
    
    return price_cn
    
if __name__ == '__main__':
    price = '101232304000034.99'
#    price = 34.99
    print transform(price)
#    for i in xrange(1000000):
#        price = 101232304000034.202434
#        transform(price)
#    print 'mine',time.time() - start

