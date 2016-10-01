#!/usr/bin/env python
# -*- coding: utf-8 -*-
# kirjutan-html.py




with open('header_en.txt','r') as myfile:
    header_en=myfile.read()
with open('leftcol_en.txt','r') as myfile:
    leftcol_en=myfile.read()
with open('main_en.txt','r') as myfile:
    main_en=myfile.read()
with open('rightcol_en.txt','r') as myfile:
    rightcol_en=myfile.read()
with open('footer_en.txt','r') as myfile:
    footer_en=myfile.read()
#with open('whatis_et.txt','r') as myfile:
#    rightcol_et=myfile.read().replace('\n', '')


f = open('test5.html','w')
sisu = header_en + leftcol_en + main_en + rightcol_en + footer_en
f.write(sisu)
f.close()


