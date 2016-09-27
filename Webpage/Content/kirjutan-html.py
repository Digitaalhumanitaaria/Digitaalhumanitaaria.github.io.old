#!/usr/bin/env python
# -*- coding: utf-8 -*-
# kirjutan-html.py

f = open('Teremaalim.html','w')

with open('head_et.txt','r') as myfile:
    head_et=myfile.read().replace('\n', '')
with open('leftcol_et.txt','r') as myfile:
    leftcol_et=myfile.read().replace('\n', '')
with open('home_et.txt','r') as myfile:
    home_et=myfile.read().replace('\n', '')
with open('rightcol_et.txt','r') as myfile:
    rightcol_et=myfile.read().replace('\n', '')

sonumalgus = """<html>
<head></head>
"""
sonumlopp = """<body><p>Tere maalim!</p></body>
</html>"""

sonum = head_et + leftcol_et + home_et + rightcol_et

f.write(sonum)
f.close()


