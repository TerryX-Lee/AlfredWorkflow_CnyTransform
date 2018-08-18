#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: rouwanzi
"""
import sys
import Ch2Num,Num2Ch,Eng2Num,Num2Eng
from workflow import Workflow3
reload(sys)
sys.setdefaultencoding('utf8')

log = None
#judge a character is a Chinese Character
def is_Chinese(uchar):
	if len(uchar) != 1:
		raise TypeError,'expected a character, but a string found!'
 
	if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
		return True
	else:
		return False
 
#Judge a ustr is all Chinese
def is_all_Chinese(ustr): 
	for uchar in ustr:
		if not is_Chinese(uchar):
			return False
 
	return True
 
#Judge a char is a number
def is_digit(uchar):
	if len(uchar) != 1:
		raise TypeError,'expected a character, but a string found!'
 
	if uchar >= u'\u0030' and uchar<=u'\u0039':
		return True
	else:
		return False
 
#Judge a str is all num
def is_all_digit(ustr):
	for uchar in ustr:
		if not is_digit(uchar) and uchar != u'\u002e':
			return False
	
	return True
 
#Judge a char is a alphabet
def is_alpha(uchar):
	if len(uchar) != 1:
		raise TypeError,'expected a character, but a string found!'
 
	if (uchar >= u'\u0041' and uchar<=u'\u005a') or \
	   (uchar >= u'\u0061' and uchar<=u'\u007a'):
		return True
	else:
		return False
 
 
#Judge a str is all alphabet
def is_all_alpha(ustr):
	for uchar in ustr:
		if uchar != u'\u0020' and not is_alpha(uchar):
			return False
	
	return True


def main(wf):
    query = wf.args[0]
    subtitle = "Press 'Enter' and copy to clipboard"

    if is_all_Chinese(query):
    	item1 = Ch2Num.transform(query)
    	item2 = Num2Eng.transform(item1)
    	wf.add_item(item1,subtitle=subtitle,arg=item1,valid=True)
    	wf.add_item(item2,subtitle=subtitle,arg=item2,valid=True)
    elif is_all_digit(query):
    	item1 = Num2Ch.transform(query)
    	item2 = Num2Eng.transform(query)
    	wf.add_item(item1,subtitle=subtitle,arg=item1,valid=True)
    	wf.add_item(item2,subtitle=subtitle,arg=item2,valid=True)
    elif is_all_alpha(query):
    	item1 = Eng2Num.transform(query)
    	item2 = Num2Ch.transform(item1)
    	wf.add_item(item1,subtitle=subtitle,arg=item1,valid=True)
    	wf.add_item(item2,subtitle=subtitle,arg=item2,valid=True)
    else:
    	item = u'Invalid input'
    	wf.add_item(item,subtitle=subtitle,arg=item,valid=True)

    
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()

    log = wf.logger
    sys.exit(wf.run(main))
    