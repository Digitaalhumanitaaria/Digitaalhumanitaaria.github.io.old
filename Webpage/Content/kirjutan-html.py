#!/usr/bin/env python
# -*- coding: utf-8 -*-
# kirjutan-html.py


with open('head_et.txt','r') as myfile:
    head_et=myfile.read().replace('\n', '')
with open('leftcol_et.txt','r') as myfile:
    leftcol_et=myfile.read().replace('\n', '')
with open('home_et.txt','r') as myfile:
    home_et=myfile.read().replace('\n', '')
with open('rightcol_et.txt','r') as myfile:
    rightcol_et=myfile.read().replace('\n', '')
#with open('whatis_et.txt','r') as myfile:
#    rightcol_et=myfile.read().replace('\n', '')


with open('head_en.txt','r') as myfile:
    head_en=myfile.read().replace('\n', '')
with open('leftcol_en.txt','r') as myfile:
    leftcol_en=myfile.read().replace('\n', '')
with open('home_en.txt','r') as myfile:
    home_en=myfile.read().replace('\n', '')
with open('rightcol_en.txt','r') as myfile:
    rightcol_en=myfile.read().replace('\n', '')
#with open('whatis_et.txt','r') as myfile:
#    rightcol_et=myfile.read().replace('\n', '')


f = open('index_et.html','w')
sisu = head_et + leftcol_et + home_et + rightcol_et
f.write(sisu)
f.close()

f = open('index_en.html','w')
sisu = head_en + leftcol_en + home_en + rightcol_en
f.write(sisu)
f.close()


