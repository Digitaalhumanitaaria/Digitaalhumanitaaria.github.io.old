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
with open('whatis_et.txt','r') as myfile:
    whatis_et=myfile.read().replace('\n', '')
with open('liikmed_et.txt','r') as myfile:
    members_et=myfile.read().replace('\n', '')
with open('docs_et.txt','r') as myfile:
    docs_et=myfile.read().replace('\n', '')
with open('activities_et.txt','r') as myfile:
    activities_et=myfile.read().replace('\n', '')

with open('head_en.txt','r') as myfile:
    head_en=myfile.read().replace('\n', '')
with open('leftcol_en.txt','r') as myfile:
    leftcol_en=myfile.read().replace('\n', '')
with open('home_en.txt','r') as myfile:
    home_en=myfile.read().replace('\n', '')
with open('rightcol_en.txt','r') as myfile:
    rightcol_en=myfile.read().replace('\n', '')
with open('whatis_en.txt','r') as myfile:
    whatis_en=myfile.read().replace('\n', '')
with open('liikmed_en.txt','r') as myfile:
    members_en=myfile.read().replace('\n', '')
with open('docs_en.txt','r') as myfile:
    docs_en=myfile.read().replace('\n', '')
with open('activities_en.txt','r') as myfile:
    activities_en=myfile.read().replace('\n', '')

f = open('index_et.html','w')
sisu = head_et + leftcol_et + home_et + rightcol_et
f.write(sisu)
f.close()
f = open('index_en.html','w')
sisu = head_en + leftcol_en + home_en + rightcol_en
f.write(sisu)
f.close()
f = open('mison_et.html','w')
sisu = head_et + leftcol_et + whatis_et + rightcol_et
f.write(sisu)
f.close()
f = open('whatis_en.html','w')
sisu = head_en + leftcol_en + whatis_en + rightcol_en
f.write(sisu)
f.close()
f = open('liikmed_et.html','w')
sisu = head_et + leftcol_et + members_et + rightcol_et
f.write(sisu)
f.close()
f = open('members_en.html','w')
sisu = head_en + leftcol_en + members_en + rightcol_en
f.write(sisu)
f.close()
f = open('dok_et.html','w')
sisu = head_et + leftcol_et + docs_et + rightcol_et
f.write(sisu)
f.close()
f = open('docs_en.html','w')
sisu = head_en + leftcol_en + docs_en + rightcol_en
f.write(sisu)
f.close()
f = open('tegevused_et.html','w')
sisu = head_et + leftcol_et + activities_et + rightcol_et
f.write(sisu)
f.close()
f = open('activities_en.html','w')
sisu = head_en + leftcol_en + activities_en + rightcol_en
f.write(sisu)
f.close()
