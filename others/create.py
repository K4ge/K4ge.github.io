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
	else:
		print('This is not zip')

zsrc = "D:/hexo/source/others/%s.zip" % filename
dsrc = "D:/hexo/source/others/test"

unzip_file(zsrc,dsrc)
for f in os.listdir(dsrc):
	if 'md' in f:
		filename = f

#markdown文档处理
cat_pattern = re.compile(r'@\((.*)\)')
tag_pattern = re.compile(r'\[(.*?)\]')
img_pattren = re.compile(r'!\[Alt text\]\(./')
img_pattren2 = re.compile(r'!\[.*\]\(\.\/(.*)\)')

with open("D:/hexo/source/others/test/%s" % filename,'r',encoding='UTF-8') as fp:
	s = fp.read()
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
---''' % (filename[:-3],time,cat[0],tags)

	result = desc + '\n'+'\n'.join(s.split('\n')[2:]).replace('##','#')
	# print(result)
	with open("D:/hexo/source/_posts/%s" % filename,'w',encoding="UTF-8") as f:
		f.write(result)

## 图片处理

# print(imgs)
for i in imgs:
	try:
		shutil.move(dsrc+'/'+i,'D:/hexo/source/img')
	except:
		pass
shutil.rmtree(dsrc)

print('Markdown create in hexo successfuly :)')