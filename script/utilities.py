# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:51:06 2020

@author: e144483
"""
from datetime import date

def weekly_update_on_thursday(todays_file):
    if date.today().weekday() == 3:
        todays_file.write('Weekly update to Lin by 5pm')