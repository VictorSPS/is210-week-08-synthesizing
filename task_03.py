#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Docstring. """

import decimal

NAME = raw_input('What is your name? ')
PRINCIPAL = raw_input('What is amount of your Principal? $ ')
PRINCIPAL = int(PRINCIPAL)
PRP1 = PRINCIPAL <= 199999
PRP2 = (200000 <= PRINCIPAL <= 999999)
PRP3 = (PRINCIPAL >= 1000000)
DURATION = raw_input('for how many years is this loan being borrowed? ')
DURATION = int(DURATION)
DUR1 = (1 <= DURATION <= 15)
DUR2 = (16 <= DURATION <= 20)
DUR3 = (21 <= DURATION <= 30)
PRE_QUALIFIED = raw_input('Are you pre-qualified for this loan? ')
TOTAL = int()
RATE = 0

if PRP1 and DUR1:
    if (PRE_QUALIFIED == 'Yes') or (PRE_QUALIFIED == 'y'):
        RATE = decimal.Decimal('0.0363')
    elif PRE_QUALIFIED == 'No' or 'n':
        RATE = decimal.Decimal('0.0465')
    else:
        RATE = None

if PRP1 and DUR2:
    if (PRE_QUALIFIED == 'Yes') or (PRE_QUALIFIED == 'y'):
        RATE = decimal.Decimal('0.0404')
    elif PRE_QUALIFIED == 'No' or 'n':
        RATE = decimal.Decimal('0.0498')
    else:
        RATE = None

if PRP1 and DUR3:
    if (PRE_QUALIFIED == 'Yes') or (PRE_QUALIFIED == 'y'):
        RATE = decimal.Decimal('0.0577')
    elif PRE_QUALIFIED == 'No' or 'n':
        RATE = decimal.Decimal('0.0639')
    else:
        RATE = None

if PRP2 and DUR1:
    if (PRE_QUALIFIED == 'Yes') or (PRE_QUALIFIED == 'y'):
        RATE = decimal.Decimal('0.0302')
    elif PRE_QUALIFIED == 'No' or 'n':
        RATE = decimal.Decimal('0.0398')
    else:
        RATE = None

if PRP2 and DUR2:
    if (PRE_QUALIFIED == 'Yes') or (PRE_QUALIFIED == 'y'):
        RATE = decimal.Decimal('0.0327')
    elif PRE_QUALIFIED == 'No' or 'n':
        RATE = decimal.Decimal('0.0408')
    else:
        RATE = None


if PRP2 and DUR3 and (PRE_QUALIFIED == 'Yes') or (PRE_QUALIFIED == 'y'):
    RATE = decimal.Decimal('0.0466')
else:
    RATE = None        
if PRP3 and DUR1 and (PRE_QUALIFIED == 'Yes') or (PRE_QUALIFIED == 'y'):
    RATE = decimal.Decimal('.0205')
else:
    RATE = None
if PRP3 and DUR2 and (PRE_QUALIFIED == 'Yes') or (PRE_QUALIFIED == 'y'):
    RATE = decimal.Decimal(' .0262')
else:
    RATE is None
if RATE :
    ratedec = decimal.Decimal(RATE) / 100
    TOTAL = int(round(PRINCIPAL * ((1 + (ratedec / 12)) ** (12 * DURATION))))
else:
    TOTAL = None    
REPORT = 'Loan Report for:  {}\n'.format(NAME)
REPORT += '----------------------------------------\n'
REPORT += 'Principal:$ {}\n'.format(PRINCIPAL)
REPORT += 'Duration:  {}\n'.format(DURATION)
REPORT += 'Pre-qualified ? : {}\n'.format(PRE_QUALIFIED)
REPORT += 'TOTAL:  {}'.format(TOTAL)

print REPORT
