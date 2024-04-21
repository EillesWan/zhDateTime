# -*- coding: utf-8 -*-

"""
版权所有 © 2024 金羿ELS
Copyright (R) 2024 Eilles Wan

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

汉字数字 = HÀNNUM = HANNUM = "〇一二三四五六七八九"
"""
汉字数字
"""

十倍汉字数字单位 = HÀNUNIT10P = "初十廿卅"
"""
仅出现在十倍的数字单位
Numeric Units for Multiples of Ten
"""

万内汉字计数单位 = HÀNUNITLK = "十百千"
"""
万以内的汉字计数单位
"""

千外汉字数字单位 = HÀNUNITRW = (
    "万亿兆京垓秭穰沟涧正载 "  # 请保留此处空格，参见 main.py的int_hàn_grouping函数
)
"""
千以上的汉字计数单位
"""

月份数字 = YUÈFÈN = MONTHNUM = " 正二三四五六七八九十⑾腊"
"""
月份数字
"""

生肖 = SHĒNGXIÀO = SHENGXIAO = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
"""
十二生肖
"""

天干 = TIĀNGĀN = TIANGAN = "甲乙丙丁戊己庚辛壬癸"
"""
天干
"""

地支 = DÌZHĪ = DIZHI = "子丑寅卯辰巳午未申酉戌亥"
"""
地支
"""

二十四时辰 = XXIVSHÍCHEN = XXIVSHICHEN = [
    "子初",
    "子正",
    "丑初",
    "丑正",
    "寅初",
    "寅正",
    "卯初",
    "卯正",
    "辰初",
    "辰正",
    "巳初",
    "巳正",
    "午初",
    "午正",
    "未初",
    "未正",
    "申初",
    "申正",
    "酉初",
    "酉正",
    "戌初",
    "戌正",
    "亥初",
    "亥正",
]
"""
宋以后的二十四时辰表示法所用之时辰
"""

LUNAR_NEW_YEAR_DATE = b"\x83\xdb\xd0\x81\xd8\xcc}\xd5\xcaz\xd2\x82\xda\xce~\xd6\xcb{\xd3\xc9\xdc\xd0\x80\xd8\xcd|\xd5\xca{\xd2\x82\xd9\xce~\xd6\xcc|\xd3\x83\xdb\xd0\x7f\xd7\xcd}\xd5\xcaz\xd2\x81\xd9\xce\x7f\xd6\xcb|\xd4\x83\xda\xd0\x80\xd7\xcd}\xd5\xcay\xd1\x82\xd9\xce\x7f\xd7\xcb{\xd3\x83\xda\xcf\x80\xd8\xcd}\xd5\xca\xdc\xd1\x81\xd9\xce\x7f\xd7\xcc{\xd2\x83\xdb\xcf\x80\xd8\xcd|\xd4\xc9z\xd1\x81\xda\xcf~\xd6\xcb{\xd2\x83\xdb\xd0\x80\xd8\xcd}\xd4\xc9z\xd2\x81\xd9\xce~\xd5\xcb{\xd3\x83\xdb\xd0\x80\xd7\xcc|\xd4\xc9z\xd2\x82\xd9\xce~\xd6\xca{\xd3\xc9\xdb\xd0\x80\xd7\xcc|\xd4\xcay\xd1\x81\xd9\xcd~\xd6\xcb{\xd3\x83\xdb\xcf\x7f\xd7\xcd|\xd4\xcaz\xd1\x81\xd9\xce~\xd6\xcb|\xd2\x82\xda\xcf\x7f\xd7\xcd}\xd4\xc9y\xd1"
"""
自1900年至2100年（首尾皆含）的农历新年所在的公历日期表（从首至尾）
每一位字节均表示一个日期，例如第一个字节 \x83 数字为 131 即表示 1900 年的农历新年是1月31日
"""

LUNAR_MONTH_PER_YEAR = b"\x84\xbd\x04\xae\nWUM\r&\r\x95FU\x05j\t\xad%]\x04\xaej[\nM\r%]%\x0bT\rj*\xda\t[t\x97\x04\x97\nK[K\x06\xa5\x06\xd4J\xb5\x02\xb6\tW%/\x04\x97fV\rJ\x0e\xa5V\xa9\x05\xad\x02\xb68n\t.|\x8d\x0c\x95\rJm\x8a\x0bU\x05jJ[\x02]\t--+\n\x95{U\x06\xca\x0bUU5\x04\xda\n[4W\x05+\x8a\x9a\x0e\x95\x06\xaaj\xea\n\xb5\x04\xb6J\xae\nW\x05&?&\r\x95u\xb5\x05j\tmT\xdd\x04\xad\nMMM\r%\x8dU\x0bT\x0bjiZ\t[\x04\x9bJ\x97\nK\xab'\x06\xa5\x06\xd4j\xf4\n\xb6\tWT\xaf\x04\x97\x06K7J\x0e\xa5\x86\xb5\x05\xac\n\xb6Ym\t.\x0c\x96M\x95\rJ\r\xa5'U\x05jz\xbb\x02]\t-\\\xab\n\x95\x0bJK\xaa\n\xd5\x95]\x04\xba\n[e\x17\x05+\n\x93G\x95\x06\xaa\n\xd5%\xb5\x04\xb6jn\nN\r&^\xa6\rS\x05\xaa7j\tm\xb4\xaf\x04\xad\nMm\x0b\r%\rR]\xd4\x0bZ\x05m%[\x04\x9bzW\nK\n\xa5[%\x06\xd2\n\xda4\xb6\t7\x84\x9f\x04\x97\x06Kf\x8a\x0e\xa5\x06\xaaJl\n\xae\t.=.\x0c\x96}U\rJ\r\xa5U\xd5\x05j\nmE]\x05-\x8a\x9b\n\x95\x0bJkj\n\xd5\x05ZJ\xba\n[\x05+;'\x06\x93w3\x06\xaa\n\xd5T\xb5\x04\xb6\nWEN\r\x16\x8e\x96\rR\r\xaaf\xaa\x05m\x04\xaeJ\x9d\n-\r\x15/%\rR"
"""
自1900年至2100年（首尾皆含）的每年的农历月份（从首至尾）
对于每个数据：
占有两个字节，共16位
首四位规定为闰的是哪一月，如 0101 为 5 即在当年5月之后闰一月
后十二位表示该年的大小月分布情况，如 010101010101 表示当年月份情况位 小大小大小大小大小大小大 月
"""

# LEAP_SIZE = 0b000000010000000100000000000000000000000000100100001001000000000010000000000000000001000000000000000000000000000000000000010000000000000000000000010010000000100100101001000000010000010000100000001000000
LEAP_SIZE = 12603243328493723047405108687154840022568558660414467489856
"""
分别是自1900年至2100年（首尾皆含）的农历闰月大小月（从尾至首）
1 为大月 30 日
0 为小月 29 日
"""
