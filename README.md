# 简易 Python 中式日期时间库

### 简介

一个简单小巧的轻量级中式日期时间库，支持农历公历互相转换，支持时辰刻数的时间表达转换，支持整数汉字化。

**敬告：该库自 2.0.0 版本开始与之前的所有版本接口不再兼容**

### 用法

1.  农历与公历

```python
# 导入模块中的类
from zhDateTime import DateTime, zhDateTime

# 利用 DateTime 类创建公历日期
western_date = DateTime(2020, 5, 20)
# 利用 chinesize 属性转换为农历日期
chinese_date = western_date.chinesize

# 利用 zhDateTime 类创建农历日期
date_lunar = zhDateTime(2024, 3, False, 13)  # 此处之False示意是否为闰月
# 利用 westernize 函数转换为公历日期
date_solar = date_lunar.westernize


# 也可以通过各自的类函数进行自主创建
a_western_date = DateTime.from_chinese_format(2024, 3, False, 13)
a_chinese_date = zhDateTime.from_western_format(2020, 5, 20)

# DateTime 类是增强型的 datetime.datetime 类，因此可以用相同的方式使用后者的函数
b_western_datetime = DateTime.now()
b_chinese_datetime = b_western_datetime.chinesize

# zhDateTime类可以进行汉字化输出
print(b_chinese_datetime.chinese_text)
# 输出应类似
# 公元二〇二五 农历乙巳蛇年 正月初三 丑时一刻 又十二分五十一秒八五 余五十一微六十二纤
# 公元二〇二五 农历乙巳蛇年 正月初三 丑时 零四分廿五秒八四 余四微六十四纤
# 公元二〇二五 农历乙巳蛇年 正月初三 子时四刻整

# 也可以分日期和时间输出不同部分（参照国家标准，此处公元2024年是农历年首所在年份）
print(b_chinese_datetime.date_hanzify())
# 类似
# 公元二〇二四 农历甲辰龙年 三月十二
print(b_chinese_datetime.time_hanzify())
# 类似
# 午时三刻 又一分三十秒三九 余五十五微六十纤
# 子时四刻整
# 丑时 零四分廿五秒八四
# 寅时二刻 又一分廿八秒
# 卯时一刻 又四分整
# 午时 零三十二秒 余四微三十六纤

# 汉字化的日期和时间函数是支持自定义格式的
print(b_chinese_datetime.date_hanzify("{干支年}{生肖}年{月份}月"))
# 类似 甲辰龙年三月
print(b_chinese_datetime.time_hanzify("{地支时}时{刻} {分}{秒}{忽}"))
# 类似 午时三刻 又一分三十秒三九
# 具体可用的格式参数请详见函数文档


# 此二类者，皆可各自加减
print(
    (zhDateTime(2024, 3, False, 12) + (DateTime.now() - DateTime(2024, 3, 1)))
    - (DateTime.now().chinesize - zhDateTime(2023, 2, False, 1))
)
# 输出应为zhDateTime类，类似
# 公元2023年 农历3月22日 0时4刻0分0秒0
```

2.  汉字数字表示法

```python
# 对整数进行汉字分组

# 分离各个单位，不进行其他处理
from zhDateTime import int_group
print(int_group(1010045760500200000000026410400044640400000002))
# 应为 [10, '载', 1004, '正', 5760, '涧', 5002, '沟', 0, '穰', 0, '秭', 264, '垓', 1040, '京', 44, '兆', 6404, ' 亿', 0, '万', 2]

# 分离单位的同时，包括中间的“零”
from zhDateTime import int_group_seperated
print(int_group_seperated(1010045760500200000000026410400044640400000002))
# 应为 [10, '载', 1004, '正', 5760, '涧', 5002, '沟', '零', 264, '垓', 1040, '京', '零', 44, '兆', 6404, '亿', ' 零', 2]

# 输出分离后的字符串，包括中间的“零”
from zhDateTime import int_2_grouped_han_str
print(int_2_grouped_han_str(1010045760500200000000026410400044640400000002))
# 应为 10载1004正5760涧5002沟零264垓1040京零44兆6404亿零2


# 四位以内整数的汉字化读法
from zhDateTime import lkint_hanzify
lkint_hanzify(1534)
# 一千五百三十四
lkint_hanzify(1020)
# 一千零二十
lkint_hanzify(29)
# 廿九

# 常规整数汉字化读法
from zhDateTime import int_hanzify
int_hanzify(1010045760500200000000026410400044640400000002)
# 十载一千零四正五千七百六十涧五千零二沟零二百六十四垓一千零四十京零四十四兆六千四百零四亿零二
```

3.  日期相关数据

```python
# 就这四个函数，，，自己看一下函数文档吧
from zhDateTime import (
    shichen_ke_2_hour_minute,  # 给出时辰和刻数，返回小时和分钟
    hour_minute_2_shichen_ke,  # 给出小时和分钟，返回时辰和刻数
    get_chinese_calendar_month_list,  # 依据提供的公历年份，给出当年每月天数列表及闰月月份
    get_chinese_new_year,  # 依据提供的公历年份，返回当年的农历新年所在的公历日期
    verify_chinese_calendar_date,  # 检查所给出之农历日期是否符合本库之可用性
)
```

### 授权

zhDateTime 库源代码之授权采用 **木兰宽松许可证，第2版** 进行授权。

> 版权所有 © 2025 金羿ELS  
> Copyright (C) 2025 Eilles(EillesWan@outlook.com)
>
> zhDateTime is licensed under Mulan PSL v2.  
> You can use this software according to the terms and conditions of the Mulan PSL v2.  
> You may obtain a copy of Mulan PSL v2 at:  
>         http://license.coscl.org.cn/MulanPSL2  
> THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,  
> EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,  
> MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.  
> See the Mulan PSL v2 for more details.

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
