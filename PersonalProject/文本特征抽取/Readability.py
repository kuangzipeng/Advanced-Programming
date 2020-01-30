from pathlib import Path
import re
from nltk.tokenize import sent_tokenize
import textstat
from pyecharts.charts import Bar
from pyecharts import options as opts

def READFILE(filename): # 读取文件内容
    with open(filename,encoding="utf-8") as f:
        content = f.read()
    return content


def DESWC(content): #英文单词数
    en = re.compile(r'[\u0061-\u007a\u0020]')
    content = "".join(en.findall(content.lower()))
    content = content.split()
    en_text = " ".join(content)  # 纯字母文本
    word_count = 0
    for each in content:
        word_count = word_count + 1
    return en_text,word_count


def DESSC(content):    # 句子数
    sents = sent_tokenize(content)
    sen_count = 0
    for i in sents:
        sen_count = sen_count + 1
    return sen_count


def DESSL(sen_count,word_count):    #句子平均长度
    ASL = word_count/sen_count
    return ASL

# 参考链接：https://blog.csdn.net/weixin_38008864/article/details/102855031
def DESWLsy(en_text,word_count):    # 单词平均音节数
    SW_count = textstat.syllable_count(en_text)
    ASW = SW_count/word_count
    return ASW


def RDFRE(ASL,ASW): # Flesch Reading Ease
    RDFRE = 206.835 - (1.015*ASL) - (84.6*ASW)
    return RDFRE


def RDFKGL(ASL,ASW):    # Flesch_Kincaid Grade Level
    RDFKGL = (.39*ASL)+(11.8*ASW)-15.59
    return RDFKGL


#main
en_book= Path(r"en_book")
for each in en_book.rglob("*.txt"):
    content = READFILE(each)
    en_text,word_count= DESWC(content)
    sen_count = DESSC(content)
    ASL = DESSL(sen_count,word_count)
    ASW = DESWLsy(en_text,word_count)
    Flesch_Reading_Ease = RDFRE(ASL,ASW)
    Flesch_Kincaid_Grade_Level = RDFKGL(ASL,ASW)
    print("英文文章",each.name,"信息统计如下：")
    print("DESWC:",word_count)
    print("DESSC:", sen_count)
    print("DESSL:", '%.3f' % ASL)
    print("DESWLsy:",'%.3f' % ASW)
    print("Flesch Reading Ease:", '%.3f'%Flesch_Reading_Ease)
    print("Flesch_Kincaid Grade Level:", '%.3f'%Flesch_Kincaid_Grade_Level)
    bar = (
        Bar()
            .add_xaxis(["DESWC","DESSC","DESSL","DESWLsy","RDFRE","RDFKGL"])
            .add_yaxis("Readability", [word_count, sen_count,'%.3f'%ASL, '%.3f'%ASW, '%.3f'%Flesch_Reading_Ease, '%.3f'%Flesch_Kincaid_Grade_Level])
            .set_global_opts(title_opts=opts.TitleOpts(title=each.stem))
    )
    bar.render(each.stem + "_Readability.html")