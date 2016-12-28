#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
import urllib
import os

def get_html(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def get_baseInfo(data):
	reg1 = r'<div class="fl">[\w\W]*?.*?<div class="fr">'
	infore1 = re.compile(reg1)
	infolist1 = re.findall(infore1,data)
	temp=''.join(infolist1)
	reg2 = r'http://.*?]'
	infore2 = re.compile(reg2)
	infolist2 = re.findall(infore2,temp)
	target=''.join(infolist2)
	return target
	
	
def get_target_info(url):
	html=get_html(url)
	temp=html.decode('gb2312','ignore')
	data=temp.encode('utf-8','ignore')
	
	target=get_baseInfo(data)

	f=open("./web_info.txt","wb+")
	f.write(target)
	f.close()
	
	f = open("web_info.txt","rb+")
	info=f.read()
	f.close()
	
	reg1 = r"http://.*?'"
	reg2 = r'>[\w\W]*?</a>'
	reg3 = r'\[.*?\]'
	
	infore1 = re.compile(reg1)
	infore2 = re.compile(reg2)
	infore3 = re.compile(reg3)
	
	#handle url
	infolist1 = re.findall(infore1,info)
	j=0
	for i in infolist1:
		url=list(i)
		url.pop()
		url=''.join(url)
		infolist1[j]=url
		j+=1

	#handle title
	infolist2 = re.findall(infore2,info)
	j=0
	for i in infolist2:
		title=list(i)
		del title[0]
		for k in range(4):
			title.pop()
		title=''.join(title)
		infolist2[j]=title
		j+=1

	#handle time
	infolist3 = re.findall(infore3,info)
	j=0
	for i in infolist3:
		time=list(i)
		del time[0]
		time.pop()
		time=''.join(time)
		infolist3[j]=time
		j+=1
	

	#write info to .csv
	f_new = open("get_medicine.people_info.csv","ab+")
	j=0
	for i in range(len(infolist1)):
		f_new.write(infolist1[j]+',')
		f_new.write(infolist2[j]+',')
		f_new.write(infolist3[j]+'\n')
		j+=1
	f_new.close()
	return

f=open("get_medicine.people_info.csv","wb+")
f.write("url,title,time\n")
url="http://medicine.people.com.cn/GB/132555/"
get_target_info(url+"index.html")
for page in range(1,21):
	page=str(page)
	get_target_info(url+"index"+page+".html")
os.remove("./web_info.txt")
