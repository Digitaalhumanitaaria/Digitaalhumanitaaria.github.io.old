#!/usr/bin/env python
# -*- coding: utf-8 -*-
# kirjutan-html.py




with open('header_en.txt','r') as myfile:
    header_en=myfile.read()
with open('mainstart.txt','r') as myfile:
    mainstart=myfile.read()
with open('leftmain_en.txt','r') as myfile:
    leftmain_en=myfile.read()
with open('centermain_en.txt','r') as myfile:
    centermain_en=myfile.read()
with open('rightmain_en.txt','r') as myfile:
    rightmain_en=myfile.read()
with open('mainend.txt','r') as myfile:
    mainend=myfile.read()
with open('footer.txt','r') as myfile:
    footer=myfile.read()
#with open('whatis_et.txt','r') as myfile:
#    rightcol_et=myfile.read().replace('\n', '')


f = open('test6.html','w')
sisu = header_en + mainstart + leftmain_en + centermain_en + rightmain_en + mainend + footer
f.write(sisu)
f.close()


