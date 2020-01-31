import book_analysis
from pathlib import Path


#main
zh_book= Path(r"zh_book")
with open("name.txt", "r", encoding = "utf-8") as f:
	name = f.read().splitlines()

for each in zh_book.rglob("*.txt"):
	content = book_analysis.READFILE(each)
	names_dic,name_list,relation_dic = book_analysis.Content_analysis(content,name)	#返回人物字典、段落共存列表和人物关系字典
	relation = book_analysis.Relation_analysis(name_list,relation_dic)		#返回人物关系词典


	with open(each.stem + "_人物及出场次数.txt", "w", encoding="utf-8") as f:	#生成人物txt
		wordcloud = []
		for name, count in names_dic.items():
			if count > 10:
				f.write(name + " " + str(count) + "次\r\n")
				tuple = (name,count)
				wordcloud.append(tuple)

	book_analysis.wordcloud_diamond(wordcloud,each.stem)	#生成词云

	with open(each.stem + "_人物关系.txt", "w", encoding="utf-8") as f:	#生成人物关系txt
		for nameA, relation in relation.items():
			for nameB, count in relation.items():
				if count > 5:
					f.write(nameA + " " + nameB + " " + str(count) + "次\r\n")

