# encoding=utf8  
import os
import shutil
import zipfile
import re
import time
import sys  
from os.path import join, getsize

filename = sys.argv[1]

#解压函数
def unzip_file(zip_src, dst_dir):
	r = zipfile.is_zipfile(zip_src)
	if r:
		fz = zipfile.ZipFile(zip_src, 'r')
		for file in fz.namelist():
			fz.extract(file, dst_dir)
		return True
	else:
		print('This is not zip')
		return False

zsrc = "D:/hexo/source/others/%s.zip" % filename
dsrc = "D:/hexo/source/others/test"

flag = unzip_file(zsrc,dsrc)
if flag:
	for f in os.listdir(dsrc):
		if 'md' in f:
			filename = f
			path = "D:/hexo/source/others/test/%s" % filename
else:
	path = "D:/hexo/source/others/"+filename+'.md'


#markdown文档处理
title_pattern = re.compile(r'##.(.*)')
cat_pattern = re.compile(r'@\((.*)\)')
tag_pattern = re.compile(r'\[(.*?)\]')
img_pattren = re.compile(r'!\[Alt text\]\(./')
img_pattren2 = re.compile(r'!\[.*\]\(\.\/(.*)\)')
with open(path,'r',encoding='UTF-8') as fp:
	s = fp.read()
	title = re.findall(title_pattern,s.split('\n')[0])[0]
	time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	cat = re.findall(cat_pattern,s.split('\n')[1])
	tag = re.findall(tag_pattern,s.split('\n')[1])
	imgs = re.findall(img_pattren2,s)
	s = re.sub(img_pattren,'![](/img/',s)
	tags=""
	for t in tag:
		tags += '- %s\n' % t
	if tags == "":
		tags = '- other'
	else:
		tags = tags[:-1]
	desc = '''---
title: %s
date: %s
categories:
- %s
tags:
%s
---''' % (title,time,cat[0],tags)

	result = desc + '\n'+'\n'.join(s.split('\n')[2:]).replace('###','##')
	# print(result)
	with open("D:/hexo/source/_posts/%s.md" % title,'w',encoding="UTF-8") as f:
		f.write(result)

## 图片处理

# print(imgs)
if flag:
	for i in imgs:
		try:
			shutil.move(dsrc+'/'+i,'D:/hexo/source/img')
		except:
			pass
	shutil.rmtree(dsrc)
	os.remove("D:/hexo/source/others/"+filename+'.zip')

os.remove("D:/hexo/source/others/"+filename+'.md')
print('Markdown create in hexo successfuly :)')