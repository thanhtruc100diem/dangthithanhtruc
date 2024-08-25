# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:28:06 2024

@author: Student
"""
a=int(input(" Nhập hệ số a :"))
b=int(input(" Nhập hệ số b :"))
S = (a**(1/2)-b**(1/2))/(a**(1/4)-b**(1/4))-(a**(1/2)+(a*b)**(1/4))/(a**(1/4)+b**(1/4))
print(S)