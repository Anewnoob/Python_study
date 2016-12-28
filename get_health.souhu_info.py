#!/usr/bin/python
#-*- coding: utf-8 -*-
#get http://health.sohu.com/shipin/ infomation

import re
import urllib
import os

def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def get_id(data):
	reg1 = r'<a class="per-name"[\w\W]*?.*?</a>'
	infore1 = re.compile(reg1)
	infolist1 = re.findall(infore1,data)
	temp = ''.join(infolist1)
	reg2 = r'>.*?</a>'
	infore2 = re.compile(reg2)
	infolist2 = re.findall(infore2,temp)

	#handle ID
	j=0
 	for i in infolist2:
		id=list(i)
		del id[0]
		for k in range(4):
			id.pop()
		id=''.join(id)
		infolist2[j]=id
		j+=1
	return infolist2

def get_url(data):
	reg1 = r'<span class="content-title">[\w\W]*?.*?target'
	infore1 = re.compile(reg1)
	infolist1 = re.findall(infore1,data)
	temp = ''.join(infolist1)
	reg2 = r'http.*?"'
	infore2 = re.compile(reg2)
	infolist2 = re.findall(infore2,temp)

	#handle url
	j=0
	for i in infolist2:
		url=list(i)
		url.pop()
		url=''.join(url)
		infolist2[j]=url
		j+=1
	return infolist2

def get_title(data):
	reg1 = r'<span class="content-title">[\w\W]*?.*?</a>'
	infore1 = re.compile(reg1)
	infolist1 = re.findall(infore1,data)
	temp = ''.join(infolist1)
	reg2 = r'blank">[/w/W]*?.*?</a>'
	infore2 = re.compile(reg2)
	infolist2 = re.findall(infore2,temp)
	
	#handle title
	j=0
	for i in infolist2:
		title=list(i)
		for k in range(7):
			del title[0]
		for k in range(4):
			title.pop()
		infolist2[j]=''.join(title)
		j+=1
	return infolist2

def get_time(data):
	reg1 = r'<span class="time">[\w\W]*?.*?</span>'
	infore1 = re.compile(reg1)
	infolist1 = re.findall(infore1,data)
	temp = ''.join(infolist1)
	reg2 = r'">[/w/W]*?.*?</'
	infore2 = re.compile(reg2)
	infolist2 = re.findall(infore2,temp)

	#handle time
	j=0
   	for i in infolist2:
		time =list(i)
		for k in range(2):
			del time[0]
		for k in range(2):
			time.pop()
		infolist2[j]=''.join(time)
		j+=1
	return infolist2

def	get_eachpage_info(url):	
	data=get_html(url)
	temp=data.decode('gb2312','ignore')
	data=temp.encode('utf-8','ignore')
	url = get_url(data)
	id = get_id(data)
	title = get_title(data)
	time = get_time(data)
	f=open("get_health.souhu_info.csv","ab+")
	j=0
	for i in range(len(url)):
		f.write(url[j]+',')
		f.write(id[j]+',')
		f.write(title[j]+',')
		f.write(time[j]+'\n')
		j+=1
	f.close()
	return

def get_page(url):
	data=get_html(url)
	temp=data.decode('gb2312','ignore')
	data=temp.encode('utf-8','ignore')
	reg1= r'var maxPage = .*?;'
	infore1 = re.compile(reg1)
	infolist1 = re.findall(infore1,data)

	#handle page
	temp=infolist1[0]
	page=list(temp)
	for i in range(14):
		del page[0]
	page.pop()
	page=''.join(page)
	return page

f=open("get_health.souhu_info.csv","wb+")
f.write("url,id,title,time\n")
pre_url="http://health.sohu.com/shipin/"
get_eachpage_info(pre_url+"index.shtml")
start=get_page(pre_url+"index.shtml")
start=int(start)-1
end=start-100+1
for page in range(start,end,-1):
	page=str(page)
	get_eachpage_info(pre_url+"index_"+page+".shtml")
