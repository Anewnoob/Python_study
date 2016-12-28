#!/usr/bin/python
#-*- coding:utf-8 -*-
#get http://www.xinhuanet.com/health/ infomation

import re
import urllib
import os

def get_data(url):
	page = urllib.urlopen(url)
	html = page.read()
	reg1 = r'<ul id="showData0[\w\W]*?.*?<ul id="showData1'
	infore1 = re.compile(reg1)
	infolist1 = re.findall(infore1,html)
	data1=''.join(infolist1)
	reg2 = r'<ul id="showData3[\w\W]*?.*?<ul id="showData4'
	infore2 = re.compile(reg2)
	infolist2 = re.findall(infore2,html)
	data2=''.join(infolist2)
	data=data1+data2	
	return data


def get_url(data):
	reg1 = r'<h3><a href="[\w\W]*?.*?target'
	infore1 = re.compile(reg1)
	infolist1 = re.findall(infore1,data)
	temp=''.join(infolist1)
	reg2 = r'http.*?htm'
	infore2 = re.compile(reg2)
	infolist2 = re.findall(infore2,temp)
	return infolist2

def get_title(data):
	reg1 = r'<h3><a href="[\w\W]*?.*?</a>'
	infore1 = re.compile(reg1)
	infolist1 = re.findall(infore1,data)
	temp=''.join(infolist1)
	reg2 = r'">[\w\W]*?.*?<'
	infore2 = re.compile(reg2)
	infolist2 = re.findall(infore2,temp)
	
	#handle title
	j=0
	for i in infolist2:
		title = list(i)
		for k in range(2):
			del title[0]
		title.pop()
		infolist2[j]=''.join(title)
		j+=1
	return infolist2

def get_time(data):
	reg1 = r'<span class="time"[\w\W]*?.*?<'
	infore1 = re.compile(reg1)
	infolist1 = re.findall(infore1,data)
	temp = ''.join(infolist1)
	reg2 = r'>[\w\W]*?.*?<'
	infore2 = re.compile(reg2)
	infolist2 = re.findall(infore2,temp)
	
	#handle time
	j=0
	for i in infolist2:
		time = list(i)
		del time[0]
		time.pop()
		infolist2[j]=''.join(time)
		j+=1
	return infolist2

def get_info(url):
	data=get_data(url)
	url=get_url(data)
	title=get_title(data)
	time=get_time(data)
	f=open("get_xinhua_health_info.csv","wb+")
	j=0
	f.write("url,title,time\n")
	for i in range(len(url)):
		f.write(url[j]+',')
		f.write(title[j]+',')
		f.write(time[j]+'\n')
		j+=1
	f.close()
	
url="http://www.xinhuanet.com/health/"
get_info(url)
