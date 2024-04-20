# 简易 Python 中式日期时间库

### 简介

一个简单的小巧的轻量级中式日期时间库，支持农历公历互相转换，支持时辰刻数的时间表达转换。

### 参标

1. 本库的农历日期计算方法参照[《中华人民共和国国家标准 GB/T 33661—2017〈农历的编算和颁行〉》](https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296)
2. 本库的时刻表达方法参照[时辰\_百度百科](https://baike.baidu.com/item/%E6%97%B6%E8%BE%B0/524274)中，唐以后的“十二时辰制”，此制是目前最为广为人知的时辰表示方法；对于宋以后的“二十四时辰”制，本库虽有提供相关内容，但并不实际采用
3. 本库中的拼音参照[《中华人民共和国国家标准 GB/T 16159-2012〈汉语拼音正词法基本规则〉》](https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=5645BD8DB9D8D73053AD3A2397E15E74)
4. 本库中的汉字大数表示方法，参照[徐岳．数术记遗．](https://ctext.org/wiki.pl?if=gb&res=249044&remap=gb)<font color=gray size=0.5>《周髀算经》，汉</font>
5. 本库中的汉字数字表示方法参照[读数法\_百度百科](https://baike.baidu.com/item/%E8%AF%BB%E6%95%B0%E6%B3%95/22670728)中，十进制读数法的相关内容
6. 本库的汉字数字用法参照[《中华人民共和国国家标准 GB/T 15835-2011〈出版物上数字用法的规定〉》](https://xb.sasu.edu.cn/__local/9/03/2D/4990C7C8DFC8D015AC7CD1FA1F9_237F574B_5DAA5.pdf)

### 致谢

1. 感谢[香港天文台](https://www.hko.gov.hk/tc/index.html)的[公历与农历日期对照表](https://www.hko.gov.hk/tc/gts/time/conversion1_text.htm)提供的自公历 1901 年至公历 2100 年的农历日期对照数据
2. 感谢[zhdate](https://github.com/CutePandaSh/zhdate)项目启发，以至于作者决定开发此项目，作者曾去那贡献过代码（awa）
3. 感谢[cnlunar 相关代码](https://github.com/OPN48/cnlunar/blob/master/cnlunar/config.py)为存储日期的方式样式提供启发
4. 感谢[中国哲学书电子化计划](https://ctext.org/zhs)为古代文献的查考提供便捷实用的途径
