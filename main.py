#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: rouwanzi
"""
import sys
from workflow import Workflow

log = None


def main(wf):
    a = wf.args
    a = '{query}'
    wf.add_item(u'123',subtitle=u'456')
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger()
    
    sys.exit(wf.run(main))
    