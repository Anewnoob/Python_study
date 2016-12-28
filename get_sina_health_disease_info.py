#!/usr/bin/python
# -*- coding: utf-8 -*-
#get infomation from http://health.sina.com.cn/disease/

import re
import urllib
import os

def get_html(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def get_url(data):
	reg1 = r'<h2><a href="[\w\W]*?.*?target'
	infore1 = re.compile(reg1)
	infolist1 = re.findall(infore1,data)
	temp = ''.join(infolist1)
	reg2 = r'http[\w\W]*?.*?html'
	infore2 = re.compile(reg2)
	infolist2 = re.findall(infore2,temp)
	print infolist2

def get_eachpage_info(url):
	data=get_html(url)
	url=get_url(data)

url="http://health.sina.com.cn/disease/"
get_eachpage_info(url)
