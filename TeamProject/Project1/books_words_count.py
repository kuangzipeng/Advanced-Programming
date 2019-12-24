import re
import jieba
import nltk
from nltk.tokenize import word_tokenize
from snownlp import SnowNLP
import pandas as pd
from pathlib import Path

def extract_word(filename):
    with open(filename, "r") as f:
        text = f.read()
    unen = re.compile(r'[\u4e00-\u9fa5]')
    zh = "".join(unen.findall(text))
    uncn = re.compile(r'[\u0061-\u007a,\u0020]')
    en = "".join(uncn.findall(text.lower()))  # 匹配英文文本(包括英文单引号)
    return zh, en  #return text

def count_zh(zh):
    dic_zh = {}
    zh_list = jieba.cut(zh, cut_all=False)
    freq_dist = nltk.FreqDist(zh_list)  # nltk统计词频
    for key in freq_dist:
        dic = {key: freq_dist[key]}
        dic_zh.update(dic_zh, **dic)
    dic_zh = sorted(dic_zh.items(), key=lambda dic_zh: dic_zh[1], reverse=True)
    return dic_zh

def count_en(en):
    dic_en = {}
    en_list = word_tokenize(en)
    freq_dist = nltk.FreqDist(en_list)  # nltk统计词频
    for key in freq_dist:
        dic = {key: freq_dist[key]}
        dic_en.update(dic_en, **dic)
    dic_en = sorted(dic_en.items(), key=lambda dic_en:dic_en[1], reverse=True)
    return dic_en

def to_csv(filename,dic_zh,dic_en):
    result_list = list()
    file_columns = ["单词", "次数"]
    i = 0
    for each in dic_zh:
        word = dic_zh[i][0]
        count = dic_zh[i][1]
        i = i + 1
        line = [word, count]
        result_list.append(line)
    i = 0
    for each in dic_en:
        word = dic_en[i][0]
        count = dic_en[i][1]
        i = i + 1
        line = [word, count]
        result_list.append(line)
    df = pd.DataFrame(result_list, columns=file_columns)
    df.to_csv(filename + "_count.csv", encoding="utf_8_sig", index=0)
    return 0

Books = Path(r"books")
for file in Books.glob(r"*.txt"):
    zh, en = extract_word(file)
    dic_zh = count_zh(zh)
    dic_en = count_en(en)
    to_csv(file.stem, dic_zh, dic_en)
