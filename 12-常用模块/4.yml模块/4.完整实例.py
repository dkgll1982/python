#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
' a YAML module '
 
__author__ = 'Chua Tony'
 
import ruamel.yaml,os
 
curpath = os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(curpath, "人资.yaml")
copypath = os.path.join(curpath, "人资1.yaml")

#开档
with open(yamlpath, "r",encoding="utf-8") as docs:
	try:
		alldata = ruamel.yaml.safe_load(docs)
	except ruamel.yaml.YAMLError as exc:
		print(exc)
 
#印出
for data in alldata:
	print(alldata[data]['联络'])
 
#修改
alldata['Tom']['联络']['公司']='963852741'
alldata['Tom']['附件']='《工作守则》'
 
#写档
with open(copypath, 'w+', encoding='utf8') as outfile:
	ruamel.yaml.dump(alldata, outfile, default_flow_style=False, allow_unicode=True)