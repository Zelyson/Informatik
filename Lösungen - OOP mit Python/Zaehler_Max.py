# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:49:15 2021

@author: Mueller.Max
"""

class Zaehler(object):
        def __init__(self):
            self.zahlenSumme=0
        def weiterZaehlen(self):
            self.zahlenSumme=self.zahlenSumme+1
        def nullSetzen(self):
            self.zahlenSumme=0