#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
阿拉伯数字转英文
'''
from decimal import Decimal

DIGIT_TABLE = {0:' ZERO',1:' ONE',2:' TWO',3:' THREE',4:' FOUR',5:' FIVE',6:' SIX',7:' SEVEN',
               8:' EIGHT',9:' NINE',10:' TEN',11:' ELEVEN',12:' TWELVE',13:' THIRTEEN',14:' FOURTEEN',
               15:' FIFTEEN',16:' SIXTEEN',17:' SEVENTEEN',18:' EIGHTEEN',19:' NINETEEN'}
TENS_TABLE = {20:' TWENTY',30:' THIRTY',40:' FOURTY',50:' FIFTY',60:' SIXTY',70:' SEVENTY',80:' EIGHTY',90:' NINETY'}
CARDINAL_NUMBER = {100:' HUNDRED',1000:' THOUSAND',1000000:' MILLION',1000000000:' BILLION',1000000000000:' TRILLION'}
CONJUNCTION = ' AND'


def _handle_int_part(num,eng_str):
    assert num > 0 and num < 1000
    
    baiwei = num / 100
    shiwei = num / 10 % 10
    gewei = num % 10
    
    if baiwei != 0:
        eng_str += DIGIT_TABLE[baiwei] + CARDINAL_NUMBER[100]
        if shiwei > 0 or gewei > 0:
            eng_str += CONJUNCTION
    if shiwei == 0:
        eng_str += DIGIT_TABLE[gewei]
    elif shiwei == 1:
        eng_str += DIGIT_TABLE[shiwei*10+gewei]
    else:
        if gewei != 0:
            eng_str += TENS_TABLE[shiwei*10] + DIGIT_TABLE[gewei]
        else:
            eng_str += TENS_TABLE[shiwei*10]
    
    return eng_str

def _handle_dec_part(num,eng_str):
    assert num > 0 and num < 100
    
    shiwei = num / 10
    gewei = num % 10
    
    if shiwei == 0:
        eng_str += DIGIT_TABLE[gewei]
    elif shiwei == 1:
        eng_str += DIGIT_TABLE[shiwei*10+gewei]
    else:
        if gewei != 0:
            eng_str += TENS_TABLE[shiwei*10] + DIGIT_TABLE[gewei]
        else:
            eng_str += TENS_TABLE[shiwei*10]
    
    return eng_str
    

def transform(price):
    eng_str = ''
    price = Decimal('{:.2f}'.format(Decimal(price)))
    
    integer = int(price)
    decimal = int(price * 100 % 100)
    
    wanyi = integer / 1000000000000
    shiyi = integer / 1000000000 % 1000
    baiwan = integer / 1000000 % 1000
    qian = integer / 1000 % 1000
    ge = integer % 1000

    if wanyi > 0 and wanyi < 1000:
        eng_str = _handle_int_part(wanyi,eng_str)
        eng_str += ' TRILLION'
    elif wanyi >= 1000 and wanyi < 10000:
        qianwanyi = wanyi / 1000
        eng_str += DIGIT_TABLE[qianwanyi] + ' THOUSAND'
        eng_str = _handle_int_part(wanyi%1000,eng_str)
        eng_str += ' TRILLION'
    
    if shiyi > 0:
        eng_str = _handle_int_part(shiyi,eng_str)
        eng_str += ' BILLION'
    
    if baiwan > 0:
        eng_str = _handle_int_part(baiwan,eng_str)
        eng_str += ' MILLION'
    
    if qian > 0:
        eng_str = _handle_int_part(qian,eng_str)
        eng_str += ' THOUSAND'
    
    if ge > 0:
        eng_str = _handle_int_part(ge,eng_str)
    
    if decimal > 0:
        eng_str += CONJUNCTION + ' CENTS'
        eng_str = _handle_dec_part(decimal,eng_str)
    
    eng_str += ' ONLY'
    
    return eng_str[1:]


if __name__ == '__main__':
    price = '1204680004567.15'
    eng_str = transform(price)
    print eng_str