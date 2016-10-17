#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02"""

DAY = raw_input('What day is it? ').lower()[:3]
TIME = int(raw_input('What time is it? '))

SNOOZE = True if (DAY == 'Sat' or DAY == 'Sun') or TIME < 600 else False
if SNOOZE == False:
    print 'Beep!'*5
