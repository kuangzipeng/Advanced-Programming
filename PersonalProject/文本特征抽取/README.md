
项目介绍
=================

**项目名称：** **文本特征抽取**

**项目要求：** 

+ 参考[Coh-Metrix version3.0 indices](http://141.225.41.245/cohmetrixhome/documentation_indices.html)，编写自己的mini版Coh-Metrix（中文或英文）
+ 实现 Descriptive、Lexical Diversity 和Readability 中的指标 
+ 输入：文章

**项目说明：**<br/>

+ 3个文件，共实现中英文共12个指标

| 文件      | 实现指标 |
|:-------:    |:-------:|
| Descriptive | DESPC（段落数）DESSC（句子数中文版）DESWC（词数中文版）DESSL（句子平均长度中文版） |
| <u>Lexical Diversity^1</u> | LDTTRa（所有单词形符比）                 LDTTRc（实词形符比） |
| <u>Readability^2</u> | DESSC（英文版） DESWC（英文版）        DESSL（英文版） DESWLsy（英文版）    RDFRE (Flesch Reading Ease)  RDFKGL(Flesch_Kincaid Grade Level) |

- ^1.形符比概念理解：https://lexically.net/downloads/version7/HTML/type_token_ratio_proc.html

- ^2.原计划按要求只做针对中文的Mini Coh-Metrix。但因为Readability中的指标所需的ASL和<u>ASW^3</u>只找到了针对英语文本的方法，故将其他指标的英文版也一并做了。

  （^3.ASW单词平均音节数的计算方法参考CSDN：https://blog.csdn.net/weixin_38008864/article/details/102855031）

  

- 输出形式：因为网站无法进行测试，所以不能参照输出。我使用**<u>文本及可视化^4的形式</u>**进行输出。

（使用pyecharts进行可视化，输出html网页如下：）

![image-20200130185648670](C:\Users\kzxzc\AppData\Local\GitHubDesktop\Advanced-Programming\PersonalProject\文本特征抽取\image-sample.png)