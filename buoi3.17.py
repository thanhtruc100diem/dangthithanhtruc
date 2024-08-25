# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:53:58 2024

@author: Student
"""
a = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
a1 = a.split(",") 
for i in a1:
    print(i)
a2 = a.replace('P. ', '').replace('.', '').replace('Tp. ', '').split(",")
for u in a2:
    print(u)