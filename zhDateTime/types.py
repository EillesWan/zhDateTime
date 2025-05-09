from typing import Callable, List, Literal, Optional, Tuple, Union

TiāngānString = CelestialStem = Literal[
    "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"
]
"""
天干字符串
"""

DìzhīString = TerrestrialBranch = Literal[
    "子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"
]
"""
地支字符串
"""

ShíchenString = Literal[
    "子时",
    "丑时",
    "寅时",
    "卯时",
    "辰时",
    "巳时",
    "午时",
    "未时",
    "申时",
    "酉时",
    "戌时",
    "亥时",
]
"""
时辰字符串
"""

XXIVShíChenString = Literal[
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
二十四时辰表达法字符串
"""

YuèfènString = ChineseCalendarMonth = Literal[
    "正月",
    "二月",
    "三月",
    "四月",
    "五月",
    "六月",
    "七月",
    "八月",
    "九月",
    "十月",
    "十一月",
    "腊月",
]
"""
月份字符串
"""

ShēngxiàoString = ChineseZodiac = Literal[
    "鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"
]
"""
生肖字符串
"""

HànziNumericUnitsString = Literal[
    "零",
    "十",
    "百",
    "千",
    "万",
    "亿",
    "兆",
    "京",
    "垓",
    "秭",
    "穰",
    "沟",
    "涧",
    "正",
    "载",
]
"""
汉字数字单位
"""
