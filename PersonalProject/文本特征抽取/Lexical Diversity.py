from pathlib import Path
import jieba.posseg as pseg
import re
from pyecharts.charts import Bar
from pyecharts import options as opts

def READFILE(filename): # 读取文件内容
    with open(filename,encoding="utf-8") as f:
        content = f.read()
    return content


def word_tag(content):    # 分词并标注词性
    content = re.sub("[\f\r\t\v+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、《》~@#￥%……&*（）]+", "", content) #去掉除换行符和空格以外字符。换行符保留，避免段尾与下一段段首结合而成的词语。空格保留，避免两个英文单词变成一个。
    words = pseg.cut(content)
    word_list = []
    flag_list = []
    for word,flag in words:
        if (word != "\n" and word != " "):  #略高换行符和英文间的空格符
            word_list.append(word)
            flag_list.append(flag)
        else:
            continue
    word_count = len(word_list)
    return word_count,word_list,flag_list #返回词数,单词列表，词性列表。此时还不能合并成字典，否则相同项会合并


def LDTTRa(word_count,word_list,flag_list): #Type token ratio for all words
    types = dict(zip(word_list,flag_list))  # 合并成字典后也合并了重复项
    TTRa = len(types) / word_count
    return TTRa


def LDTTRc(word_list,flag_list): #Type token ratio for content words
    content_word = []   #实词列表
    content_flag = []   #实词词性列表
    empty_word = ["d","p","c","u","e","o","y"]   # 根据网上资料，中文常见的虚词有：d副词、p介词、c连词、u助词、e叹词、o拟声词、y语气词
    for i in range(0,len(word_list)):
        if (flag_list[i] not in empty_word):
            content_word.append(word_list[i])
            content_flag.append(flag_list[i])
        else:
            continue
    content_dic = dict(zip(content_word,content_flag))  # 合并成字典后也合并了重复项
    types = len(content_dic)  #类符
    values = len(content_word)#形符
    TTrc = types/values
    return TTrc


#main
zh_book= Path(r"zh_book")
for each in zh_book.rglob("*.txt"):
    content = READFILE(each)
    word_count,word_list,flag_list= word_tag(content)
    TTra = LDTTRa(word_count,word_list,flag_list)
    TTrc = LDTTRc(word_list,flag_list)
    print("中文文章",each.name,"信息统计如下：")
    print("Type token ratio for all words:",'%.3f'%TTra)
    print("Type token ratio for content words:",'%.3f'%TTrc)
    bar = (
        Bar()
            .add_xaxis(["Type token ratio for all words", "Type token ratio for content words"])
            .add_yaxis("Lexical Diversity", ['%.3f'%TTra,'%.3f'%TTrc])
            .set_global_opts(title_opts=opts.TitleOpts(title=each.stem))
    )
    bar.render(each.stem + "_Lexical Diversity.html")
