# 简易Python中式日期时间库

### 简介
一个简单的小巧的中式日期时间库，支持农历公历互相转换，支持时辰刻数的时间表达转换。

### 参标

1.  本库的农历日期计算方法参照[《中华人民共和国国家标准GB/T 33661—2017〈农历的编算和颁行〉》](https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296)
2.  本库的时刻表达方法参照[时辰_百度百科](https://baike.baidu.com/item/%E6%97%B6%E8%BE%B0/524274)中，唐以后的“十二时辰制”，此制是目前最为广为人知的时辰表示方法；对于宋以后的“二十四时辰”制，本库虽有提供相关内容，但并不实际采用
2.  本库中的拼音参照[《中华人民共和国国家标准GB/T 16159-2012〈汉语拼音正词法基本规则〉》](https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=5645BD8DB9D8D73053AD3A2397E15E74)

### 致谢

1.  感谢[香港天文台](https://www.hko.gov.hk/tc/index.html)的[公历与农历日期对照表](https://www.hko.gov.hk/tc/gts/time/conversion1_text.htm)提供的自公历1901年至公历2100年的农历日期对照数据
2.  感谢[zhdate](https://github.com/CutePandaSh/zhdate)项目启发，以至于作者决定开发此项目，作者曾去那贡献过代码（awa）
3.  感谢[cnlunar相关代码](https://github.com/OPN48/cnlunar/blob/master/cnlunar/config.py)为存储日期的方式样式提供启发