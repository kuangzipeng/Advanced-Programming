from pathlib import Path
import jieba
import re
from pyecharts.charts import Bar
from pyecharts import options as opts
def READFILE(filename): # 读取文件内容
    with open(filename,encoding="utf-8") as f:
        content = f.read()
    return content


def DESPC(content):    # 段落数
    para_count = 0
    content = content.split('\n')
    for each in content:
        if (each != ''):
            para_count = para_count + 1
        else:
            continue
    return para_count


def DESSC(content):    # 句子数
    sen_list = re.split("[\n]|[\?\!\.\'。''。”''!''?']",content)  #【。”】这种情况为在句末的“XXXXX。”
    sen_count = 0
    for each in sen_list:
        if ( each != ""):
            sen_count = sen_count + 1
        else:
            continue
    return sen_count


def DESWC(content):    # 词数
    content = re.sub("[\f\r\t\v+\.\!\/_,$%^*(+\"\')]+|[+——()?《》【】“”！，。？、~@#￥%……&*（）]+", "", content) #去掉除换行符以外字符。换行符保留，避免段尾与下一段段首结合而成的词语
    word_list = jieba.cut(content)  #使用jieba进行分词。英文单词也能被正确分开
    word_list = list(word_list)
    word_count = 0
    for each in word_list:
        if ( each != "\n" and each != " "):   # " "存在于英文单词间
            word_count = word_count + 1
        else:
            continue
    return word_count


def zh_count(content):  #字数
    content = re.sub("[\W]+","",content)
    count = len(content)
    return count


def DESSL(sen_count,count): #句子平均长度
    ASL = count/sen_count
    return ASL


#main
zh_book= Path(r"zh_book")
for each in zh_book.rglob("*.txt"):
    content = READFILE(each)
    para_count = DESPC(content)
    sen_count = DESSC(content)
    word_count = DESWC(content)
    count = zh_count(content)
    ASL = DESSL(sen_count,count)
    print("中文文章",each.name,"信息统计如下：")
    print("字数：", count)  # 不在指标列表内
    print("DESPC:",para_count)
    print("DESSC:",sen_count)
    print("DESWC:",word_count)
    print("DESSL:",'%.3f'%ASL)
    bar = (
        Bar()
            .add_xaxis(["DESPC", "DESSC", "DESWC", "DESSL"])
            .add_yaxis("Descriptive", [para_count, sen_count, word_count, ASL])
            .set_global_opts(title_opts=opts.TitleOpts(title=each.stem))
    )
    bar.render(each.stem+"_Descriptive.html")




