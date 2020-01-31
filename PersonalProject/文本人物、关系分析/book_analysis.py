from pathlib import Path
import jieba.posseg as pseg


def READFILE(filename): # 读取文件内容
	content = ""
	with open(filename,"r",encoding="utf-8") as f:
		for line in f.readlines():
			if line != "\n":
				content += line	#content去除原文件中的空行
	return content


def	Content_analysis(content,name):
	names = {}  # 人名字典，key为名字，value为出现次数
	relation = {}  # 关系词典，key为人名A，value为一个字典，该字典key为人名B，value为AB两人在500词内的共存次数。
	name_list = []	# 每500词中出现的人物为list中的元素
	n = 0
	while n < len(content):
		para = content[n:n+1000]	# 每次读取1000词为一段，统计人物出现次数，分析其中的人物关系
		n += 1000
		pos = pseg.cut(para)	# 使用jieba分词
		name_list.append([])	# 为这1000词建立一个列表，列表内是所有出现的人物
		for each in pos:
			if each.flag != "nr" :	# 找出词性为nr的词语，即为人物
				continue
			if each.word not in name:
				continue
			name_list[-1].append(each.word)

			if(each.word in names.keys()):	#判断人名字典中是否已出现该人物，没出现则新增，出现过则次数加1
				names[each.word] += 1
			else:
				relation[each.word] = {}	#为该人物添加字典，key为人名，value为与之有关系的人物和共存次数
				names[each.word] = 1
	return names,name_list,relation

def Relation_analysis(name_list,relation):
	for each in name_list:	#取出每一段（1000词）中的人名列表
		for nameA in each:
			for nameB in each:
				if nameA == nameB:
					continue
				if nameB in relation[nameA].keys():	#判断A的关系列表是否有B，若无则新建，有则次数加1
					relation[nameA][nameB] += 1
				else:
					relation[nameA][nameB] = 1
	return relation





