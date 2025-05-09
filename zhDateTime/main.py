# -*- coding: utf-8 -*-

"""
版权所有 © 2025 金羿ELS
Copyright (C) 2025 Eilles(EillesWan@outlook.com)

zhDateTime is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""

import datetime
from dataclasses import dataclass

from .constants import (
    CELESTIAL_STEMS,
    CHINESE_CALENDAR_MONTH_PER_YEAR,
    CHINESE_NEW_YEAR_DATE,
    CHINESE_ZODIACS,
    HÀNUNIT10P,
    HÀNUNITLK,
    HÀNUNITRW,
    LEAP_SIZE,
    MONTHS_IN_HANZI,
    NUM_IN_HANZI,
    TERRESTRIAL_BRANCHES,
    XXIVSHÍCHEN,
)
from .types import (
    Callable,
    HànziNumericUnitsString,
    List,
    Optional,
    ShíchenString,
    Tuple,
    Union,
    XXIVShíChenString,
)

"""
    警告
本软件之源码中包含大量简体汉语，不懂的话请自行离开。

    注意
此軟體源碼内含大量簡化字，若存不解勿觀之。

    WARNING
This source code contains plenty of simplified Han characters.

    诫曰
此软件源码所含多俗字。
"""


def get_chinese_new_year(western_year: int) -> Tuple[int, int]:
    """
    依据提供的公历年份（年首所在的公历年），返回当年的农历新年所在的公历日期

    参数
    ----
        western_year: int 公历年份

    返回值
    ------
        Tuple(int公历月, int公历日, )农历新年日期
    """
    new_year_code = CHINESE_NEW_YEAR_DATE[western_year - 1900]
    return new_year_code // 100, new_year_code % 100


month_days_bos: Callable[[Union[bool, int]], int] = lambda big_or_small: (
    30 if big_or_small else 29
)
"""
依据提供的是否为大小月之布尔值，返回当月的天数

参数
----
    big_or_small: int|bool 大月为真，小月为假

返回值
------
    int 当月天数，大月为30，小月为29
"""

month_days_pusher: Callable[[int, int], int] = (
    lambda month_code, push_i: month_days_bos((month_code >> push_i) & 0x1)
)
"""
依据提供的农历月份信息，求取所需的月份之天数

参数
----
    month_code: int 当月月份信息，为16位整数数据，其末12位当为一年的大小月排布信息
    push_i: int 需求的月份

返回值
------
    int 当月天数，大月为30，小月为29
"""


def decode_month_code(month_code: int, leap_days: int = 0) -> Tuple[List[int], int]:
    """
    依据提供的农历月份信息码，求取当年每月天数之列表及闰月月份

    参数
    ----
        month_code: int 当月月份信息，为16位整数数据，其末12位当为一年的大小月排布信息，前四位为闰月月份
        leap_days: int 当年闰月之天数

    返回值
    ------
        Tuple(List[int当月天数, ]当年每月天数, int闰月之月份（为0则无闰月）, )当年每月天数列表及闰月月份
    """
    leap_month = (month_code & 0b1111000000000000) >> 12
    return (
        [month_days_pusher(month_code, i) for i in range(11, 11 - leap_month, -1)]
        + [
            leap_days,
        ]
        + [month_days_pusher(month_code, i) for i in range(11 - leap_month, -1, -1)]
        if leap_month
        else [month_days_pusher(month_code, i) for i in range(12)][::-1]
    ), leap_month


get_month_code: Callable[[int], int] = lambda western_year: int.from_bytes(
    CHINESE_CALENDAR_MONTH_PER_YEAR[
        (western_year - 1900) * 2 : (western_year - 1899) * 2
    ],
    "big",
)
"""
依据提供的公历年份（年首所在的公历年），返回当年的农历月份信息码

参数
----
    western_year: int 公历年份

返回值
------
    int 农历月份信息码
"""

get_leap_size: Callable[[int], int] = lambda western_year: month_days_bos(
    (LEAP_SIZE >> (western_year - 1900)) & 0x1
)
"""
依据提供的公历年份（年首所在的公历年），通过判断当年的农历中是否有大闰月，给出其闰月应为几天

注意，倘若本年无闰月，也会给出闰月天数为29天

参数
----
    western_year: int 公历年份

返回值
------
    int 闰月天数
"""


get_chinese_calendar_month_list: Callable[[int], Tuple[List[int], int]] = (
    lambda western_year: decode_month_code(
        get_month_code(western_year),
        get_leap_size(western_year),
    )
)
"""
依据提供的公历年份（年首所在的公历年），给出当年每月天数之列表及闰月月份

参数
----
    western_year: int 公历年份

返回值
------
    Tuple(List[int当月天数, ]当年每月天数, int闰月之月份（为0则无闰月）, )当年每月天数列表及闰月月份
"""


def verify_chinese_calendar_date(
    western_year: int,
    chinese_calendar_month: int,
    is_leap: bool,
    chinese_calendar_day: int,
) -> Tuple[
    int,
    List[int],
    int,
]:
    """
    检查所给出之农历日期是否符合本库之可用性

    参数
    ----
        western_year: int 公历年份（年首所在的公历年）
        chinese_calendar_month: int 农历月份
        is_leap: bool 当月是否为闰月
        chinese_calendar_day: int 当月天数

    返回值
    ------
        Tuple(int该日期的可用情况, List[int]每月天数, int闰月月份（为0则无闰月）)

        注：返回的第一个值 verify_result 是一个整数，占 4 位。从左至右，这四位的二进制值分别表示：
            1: 年份范围
            2: 月份范围
            3: 日数范围
            4: 闰月判断
        的正误情况。
            例如，返回为 11 即 `0b1011` ，则表示所给的月份是错误的。
            完全正确应该返回为 15 即 `0b1111`

    """
    _month_data = get_chinese_calendar_month_list(western_year)

    verify_result = (
        (
            ((1900 <= western_year <= 2100) << 1)  # 确认年份范围
            + (1 <= chinese_calendar_month <= 12)
        )
        << 2
    ) + (  # 确认月份范围
        (  # 当为闰月时
            (
                (
                    1 <= chinese_calendar_day <= get_leap_size(western_year)
                )  # 确认闰月日数
                << 1
            )
            + (chinese_calendar_month == _month_data[1])  # 确认此月闰月与否
        )
        if is_leap
        else (
            (
                (
                    1
                    <= chinese_calendar_day
                    <= _month_data[0][chinese_calendar_month - 1]
                )  # 当非闰月时，确认日数范围
                << 1
            )
            + 1  # 由于无闰可判断，故默认为正确
        )
    )
    return (
        verify_result,
        *_month_data,
    )


def analyze_verify_result(
    verify_result: int,
) -> Tuple[bool, str]:
    """
    反馈农历日期的检验结果

    参数
    ----
        verify_result: int 该日期的可用情况

    返回
    ----
        Tuple[bool, str] 是否可用，错误信息
    """

    # 参数校验（仅为 4 位时有效，即范围检查 0 <= verify_result <= 15）
    if verify_result >> 4:
        raise ValueError("无效验证结果值：{}".format(bin(verify_result)))
    # print(bin(verify_result))
    error_map = [
        (0b1000, "年份范围"),
        (0b0100, "月份范围"),
        (0b0010, "日数范围"),
        (0b0001, "闰月判断"),
    ]

    return (
        verify_result == 0b1111,
        "、".join(error for mask, error in error_map if not verify_result & mask),
    )


def shíchen2int(dìzhī: Union[ShíchenString, XXIVShíChenString], xxiv: bool = False):
    """
    将给出的地支时辰字符串转为时辰数

    参数
    ----
        dìzhī: str 地支时辰字串
        xxiv: bool 是否使用二十四时辰表示法

    返回值
    ------
        int 时辰之数字
    """
    return (
        (XXIVSHÍCHEN.index(dìzhī[:2]) if dìzhī[:2] in XXIVSHÍCHEN else -1)
        if xxiv
        else TERRESTRIAL_BRANCHES.find(dìzhī[0])
    )
    # 其实，二十四时辰完全可以算的出来，而不用index这样丑陋
    # 但是，平衡一下我们所需要的时间和空间
    # 不难发现，如果利用计算来转，虽然对空间需求确实减少了
    # 但是消耗的计算量是得不偿失的，更何况计算还占一部分内存
    # 有人曾经对我说，在这种着实细微之处的优化无论是相较于用户还是开发者，都等于没有
    # 也许在现在这个时代实实在在是这样的
    # 从来如此，还会错吗？
    # if xxiv:
    #     return DÌZHĪ.find(dìzhī[0])*2+(0 if dìzhī[1] == '初' else (1 if dìzhī[1] == "正" else -1))


def shíchen_kè_2_hour_minute(
    shichen: int, quarter: int, xxiv: bool = False
) -> Tuple[int, int]:
    """
    给出时辰和刻数，返回小时和分钟

    参数
    ----
        shichen: int 时辰
        quarter: int 刻
        xxiv: bool 是否使用二十四时辰表示法

    返回值
    ------
        Tuple(int小时, int分钟, )时间
    """
    return (
        ((shichen - 1) % 24, quarter * 15)
        if xxiv
        else (
            (23 + (shichen * 2) + (quarter // 4)) % 24,
            (quarter * 15) % 60,
        )
    )


def hour_minute_2_shíchen_kè(
    hours: int, minutes: int, xxiv: bool = False
) -> Tuple[int, int]:
    """
    给出小时和分钟，返回时辰和刻数

    参数
    ----
        hours: int 小时数
        minutes: int 分钟
        xxiv: bool 是否使用二十四时辰表示法

    返回值
    ------
        Tuple(int时辰, int刻数, )古法时间
    """
    return (
        ((hours + 1) % 24, minutes // 15)
        if xxiv
        else (
            (shichen := (((hours := hours + (minutes // 60)) + 1) // 2) % 12),
            (((hours - ((shichen * 2 - 1) % 24)) % 24) * 60 + (minutes % 60)) // 15,
        )
    )


def int_group(integer: int) -> List[Union[int, HànziNumericUnitsString]]:
    """
    整数分组，依据汉字标准

    参数
    ----
        integer: int 整数

    返回值
    ------
        List[Union[int, HànziNumericUnitsString]] 汉字分组后的列表
    """
    # 应该没有大于 999999999999999999999999999999999999999999999999
    # 即 9999载9999正9999涧9999沟9999穰9999秭9999垓9999京9999兆9999亿9999万9999
    # 的数吧，有也不支持就好了；我是不希望佛经里那一套可以放进这完美的计数法
    # 凑单个汉字也好听
    if integer:
        final_result = []
        unit = 0
        while integer:
            final_result.insert(
                0,
                integer % 10000,
            )
            final_result.insert(
                0,
                HÀNUNITRW[unit],
            )
            integer //= 10000
            unit += 1
        return final_result[1:]
    else:
        return [0]


def int_group_seperated(integer: int) -> List[Union[int, HànziNumericUnitsString]]:
    """
    整数汉字分组读法

    参数
    ----
        integer: int 整数

    返回值
    ------
        List[Union[int, HànziNumericUnitsString]] 汉字分组后的列表，包括读出的零
    """
    result: List[Union[int, HànziNumericUnitsString]] = ["零"]
    skip = False
    for ppc in int_group(integer):
        if skip:
            skip = False
            continue
        elif ppc == 0:
            if result[-1] != "零":
                result.append("零")
            skip = True
            continue
        elif isinstance(ppc, int):
            if ppc < 1000:
                if result[-1] != "零":
                    result.append("零")
        result.append(ppc)
    return result[1:]


def int_2_grouped_hàn_str(integer: int) -> str:
    """
    整数汉字分组

    参数
    ----
        integer: int 整数

    返回值
    ------
        str 汉字分组后的字符串
    """
    return "".join([str(i) for i in int_group_seperated(integer)])


def lkint_hànzìfy(integer: int) -> str:
    """
    万以内的数字汉字化

    参数
    ----
        integer: int 千以内的整数

    返回值
    ------
        str 汉字表达的整数
    """
    # 妈耶
    # 我写的真丑
    # 有没有更好的写法？？？
    if integer == 0:
        return "零"
    elif integer == 10:
        return "十"
    elif integer < 100:
        if integer % 10 == 0:
            return NUM_IN_HANZI[integer // 10] + "十"
        elif integer < 30:
            if integer > 20:
                return "廿" + NUM_IN_HANZI[integer % 10]
            elif integer > 10:
                return "十" + NUM_IN_HANZI[integer % 10]
            else:
                return NUM_IN_HANZI[integer % 10]
        else:
            return NUM_IN_HANZI[integer // 10] + "十" + NUM_IN_HANZI[integer % 10]
    elif integer < 1000:
        if integer % 100 == 0:
            return NUM_IN_HANZI[integer // 100] + "百"
        elif (integer // 10) % 10 == 0:
            return NUM_IN_HANZI[integer // 100] + "百零" + NUM_IN_HANZI[integer % 10]
        else:
            return (
                NUM_IN_HANZI[integer // 100]
                + "百"
                + NUM_IN_HANZI[(integer // 10) % 10]
                + "十"
                + (NUM_IN_HANZI[integer % 10] if integer % 10 else "")
            )
    else:
        if integer % 1000 == 0:
            return NUM_IN_HANZI[integer // 1000] + "千"
        elif (integer // 100) % 10 == 0:
            if (integer // 10) % 10 == 0:
                return (
                    NUM_IN_HANZI[integer // 1000] + "千零" + NUM_IN_HANZI[integer % 10]
                )
            else:
                return (
                    NUM_IN_HANZI[integer // 1000]
                    + "千零"
                    + NUM_IN_HANZI[(integer // 10) % 10]
                    + "十"
                    + (NUM_IN_HANZI[integer % 10] if integer % 10 else "")
                )
        else:
            return NUM_IN_HANZI[integer // 1000] + "千" + lkint_hànzìfy(integer % 1000)


def int_hànzìfy(integer: int) -> str:
    """
    整数的汉字化

    参数
    ----
        integer: int 整数

    返回值
    ------
        str 汉字表达的整数
    """
    return "".join(
        [
            lkint_hànzìfy(i) if isinstance(i, int) else i
            for i in int_group_seperated(integer)
        ]
    )


@dataclass(init=False)
class zhDateTime:
    """
    中式传统日期时间
    """

    western_year: int
    """
    农历年首所处的公历年份
    """
    chinese_calendar_month: int
    """
    农历月
    """
    is_leap_month: bool
    """
    当月是否为闰月
    """
    chinese_calendar_day: int
    """
    农历日
    """
    shichen: int
    """
    时辰
    """
    quarters: int
    """
    刻数
    """
    minutes: int
    """
    分钟
    """
    seconds: int
    """
    秒数
    """
    microseconds: int
    """
    微秒
    """

    def __init__(
        self,
        western_year_: int,
        chinese_calendar_month_: int,
        is_leap_: Optional[bool],
        chinese_calendar_day_: int,
        shichen_: Union[int, ShíchenString] = 0,
        quarters_: int = 4,
        minutes_: int = 0,
        seconds_: int = 0,
        microseconds_: int = 0,
    ) -> None:
        """
        构建一个中式传统日期时间类

        参数
        ----
            western_year_: int 农历年份（农历新年所在的公历年份）
            chinese_calendar_month_: int 农历月
            is_leap_: bool 是否闰月
            chinese_calendar_day_: int 农历日
            shichen_: Union[int, ShíchenString] 时辰
            quarters_: int 刻
            minutes_: int 分
            seconds_: int 秒
            microseconds_: int 微秒

        """
        is_leap_ = bool(is_leap_)
        # 确认所输入 年份、月份、闰否、日期 的正误情况
        if (
            check_result := analyze_verify_result(
                verify_chinese_calendar_date(
                    western_year_,
                    chinese_calendar_month_,
                    is_leap_,
                    chinese_calendar_day_,
                )[0]
            )
        )[0]:
            self.western_year = western_year_
            self.chinese_calendar_month = chinese_calendar_month_
            self.chinese_calendar_day = chinese_calendar_day_
            self.is_leap_month = is_leap_
            self.shichen = (
                shichen_ if isinstance(shichen_, int) else shíchen2int(shichen_)
            ) + (quarters_ // 8)
            self.quarters = (quarters_ % 8) + (minutes_ // 15)
            self.minutes = (minutes_ % 15) + (seconds_ // 60)
            self.seconds = (seconds_ % 60) + (microseconds_ // 1000000)
            self.microseconds = microseconds_ % 1000000
        else:
            raise ValueError(
                "农历日期错误：不支持形如 公历{}年 农历{}{}月{}日 的日期表示\n\t可能是{}错误".format(
                    western_year_,
                    "闰" if is_leap_ else "",
                    chinese_calendar_month_,
                    chinese_calendar_day_,
                    check_result[1],
                )
            )

    @classmethod
    def from_western_format(
        cls,
        western_calendar_year: int,
        western_calendar_month: int,
        western_calendar_day: int,
        hour: int = 0,
        minute: int = 0,
        second: int = 0,
        microsecond: int = 0,
    ):
        """
        从公历格式创建一个中式传统日期时间类

        参数
        ----
            western_calendar_year: int 公历年份
            western_calendar_month: int 公历月份
            western_calendar_day: int 公历日
            hour: int 小时
            minute: int 分钟
            second: int 秒
            microsecond: int 微秒
        """
        # 若未至农历新年，则农历年份为公历之去年；而后求得距农历当年之新年所差值值
        passed_days = (
            datetime.date(
                western_calendar_year, western_calendar_month, western_calendar_day
            )
            - datetime.date(
                (
                    chinese_calendar_year := western_calendar_year
                    - (lambda a, c, d: ((a[0] > c) or (a[0] == c and a[1] > d)))(
                        get_chinese_new_year(western_calendar_year),
                        western_calendar_month,
                        western_calendar_day,
                    )
                ),
                *get_chinese_new_year(chinese_calendar_year),
            )
        ).days
        # 取得本农历年之月份表
        month_info, leap_month = get_chinese_calendar_month_list(chinese_calendar_year)
        calculate_days = 0
        # 临时计算用的月份
        temp_month = (
            len(
                months := [
                    days_per_mon
                    for days_per_mon in month_info
                    if (
                        (calculate_days := calculate_days + days_per_mon) <= passed_days
                    )
                ]
            )
            + 1
        )
        # print(hour_minute2shíchen_kè(hour, minute + (second // 60)))
        return cls(
            chinese_calendar_year,
            temp_month - ((leap_month > 0) and (temp_month > leap_month)),
            (leap_month > 0) and (temp_month == leap_month + 1),
            passed_days - sum(months) + 1,
            *hour_minute_2_shíchen_kè(hour, (minute := (minute + (second // 60)))),
            minute % 15,
            (second % 60) + (microsecond // 1000000),
            microsecond % 1000000,
        )

    def __str__(self) -> str:
        """
        返回一个中式传统日期时间类的字符串表示，以数字代替其中所有量
        """
        return "公元{}年 农历{}{}月{}日 {}时{}刻{}分{}秒{}".format(
            self.western_year,
            "闰" if self.is_leap_month else "",
            self.chinese_calendar_month,
            self.chinese_calendar_day,
            self.shichen,
            self.quarters,
            self.minutes,
            self.seconds,
            self.microseconds,
        )

    def __add__(self, time_delta: datetime.timedelta):
        return (self.to_western_format() + time_delta).to_chinese_format()

    def __sub__(self, datetime_delta):
        if isinstance(datetime_delta, datetime.timedelta):
            return (self.to_western_format() - datetime_delta).to_chinese_format()
        elif isinstance(datetime_delta, DateTime):
            return self.to_western_format() - datetime_delta
        elif isinstance(datetime_delta, zhDateTime):
            return self.to_western_format() - datetime_delta.to_western_format()
        else:
            raise TypeError(
                "运算单位错误：{}与{}不支持相减".format(
                    type(self), type(datetime_delta)
                )
            )

    @property
    def western_calender_year_in_hànzì(self) -> str:
        """
        西历年份，如：二〇二四
        """
        return "".join(
            [
                NUM_IN_HANZI[(self.western_year // (10**i)) % 10]
                for i in range(3, -1, -1)
            ]
        )

    @property
    def gānzhī_year(self):
        """
        干支年份，如：甲辰
        """
        return (
            CELESTIAL_STEMS[(yc := (self.western_year - 1984) % 60) % 10]
            + TERRESTRIAL_BRANCHES[yc % 12]
        )

    @property
    def zodiac_year(self):
        """
        当前生肖，如：龙
        """
        return CHINESE_ZODIACS[(self.western_year - 1984) % 12]

    @property
    def month_in_hànzì(self):
        """
        汉字月份，如：八
        """
        return MONTHS_IN_HANZI[
            self.chinese_calendar_month
        ]  # .replace("冬", "十一") 冬月就十一月，不替换了

    @property
    def numeric_day_in_hànzì(self):
        """
        数序纪日，如：廿六
        """
        return (
            "初十"
            if self.chinese_calendar_day == 10
            else (
                NUM_IN_HANZI[self.chinese_calendar_day // 10] + "十"
                if (self.chinese_calendar_day % 10 == 0)
                else (
                    HÀNUNIT10P[self.chinese_calendar_day // 10]
                    + NUM_IN_HANZI[self.chinese_calendar_day % 10]
                )
            )
        )

    @property
    def gānzhī_day(self):
        """
        干支纪日，如：丁亥
        """
        return (
            CELESTIAL_STEMS[dz := (self.chinese_calendar_day - 1) % 10]
            + TERRESTRIAL_BRANCHES[dz % 12]
        )

    def date_in_hànzì(
        self, 格式文本: str = "公元{西历年} 农历{干支年}{生肖}年 {月份}月{数序日}"
    ) -> str:
        return 格式文本.format(
            西历年=self.western_calender_year_in_hànzì,
            干支年=self.gānzhī_year,
            生肖=self.zodiac_year,
            月份=self.month_in_hànzì,
            数序日=self.numeric_day_in_hànzì,
            干支日=self.gānzhī_day,
        )

    def date_hanzify(
        self, formatter: str = "公元{西历年} 农历{干支年}{生肖}年 {月份}月{数序日}"
    ) -> str:
        """
        返回以汉语表示的日期

        参数
        ----
            formatter: 格式文本，需要生成的汉语日期格式化样式。
                可用参数为：西历年、干支年、生肖、月份、数序日、干支日；
                分别对应值：western_calender_year_in_hànzì、gānzhī_year、zodiac_year、month_in_hànzì、numeric_day_in_hànzì、gānzhī_day
                所有参数皆不带单位

        返回值
        ----
            str日期字符串
        """
        return self.date_in_hànzì(格式文本=formatter)

    @property
    def dìzhī_hour(self):
        """
        地支时，如：午
        """
        return TERRESTRIAL_BRANCHES[self.shichen]

    @property
    def quarters_hànzì(self):
        """
        汉字刻数，如：七
        """
        return NUM_IN_HANZI[self.quarters]

    @property
    def minutes_hànzì(self):
        """
        汉字分钟，如：三
        """
        return lkint_hànzìfy(self.minutes)

    @property
    def seconds_hànzì(self):
        """
        汉字秒数，如：十
        """
        return lkint_hànzìfy(self.seconds)

    @property
    def cent_seconds_hànzì(self):
        """
        汉字忽秒，如：六七
        """
        return (
            NUM_IN_HANZI[(self.microseconds // 100000) % 10]
            + NUM_IN_HANZI[(self.microseconds // 10000) % 10]
        ).replace("〇", "零")

    def time_in_hànzì(
        self, 格式文本: str = "{地支时}时{刻} {分}{秒}{忽} {微}{纤}"
    ) -> str:
        return 格式文本.format(
            地支时=self.dìzhī_hour
            + (
                ""
                if (self.quarters or self.minutes or self.seconds or self.microseconds)
                else "整"
            ),
            刻=(
                (
                    self.quarters_hànzì
                    + "刻"
                    + (
                        ""
                        if (self.minutes or self.seconds or self.microseconds)
                        else "整"
                    )
                )
                if self.quarters
                else ""
            ),
            分=(
                ("又" if self.quarters else "零")
                if (self.minutes or self.seconds or self.microseconds)
                else ""
            )
            + (
                (
                    self.minutes_hànzì
                    + "分"
                    + ("" if (self.seconds or self.microseconds) else "整")
                )
                if self.minutes
                else ""
            ),
            秒=(
                (self.seconds_hànzì + "秒" + ("" if self.microseconds else "整"))
                if (self.seconds or self.microseconds)
                else ""
            ),
            忽=(self.cent_seconds_hànzì if (self.microseconds // 10000) else ""),
            微=(
                (
                    "余"
                    + (
                        (
                            lkint_hànzìfy(wēi)
                            + "微"
                            + ("" if (self.microseconds % 100) else "整")
                        )
                        if wēi
                        else ""
                    )
                )
                if (wēi := ((self.microseconds // 100) % 100))
                or (self.microseconds % 100)
                else ""
            ),
            纤=(
                (lkint_hànzìfy(xiān) + "纤")
                if (xiān := (self.microseconds % 100))
                else ""
            ),
        ).strip()

    def time_hanzify(
        self, formatter: str = "{地支时}时{刻} {分}{秒}{忽} {微}{纤}"
    ) -> str:
        """
        返回以汉语表示的时间

        参数
        ----
            formatter: 格式文本，需要生成的汉语时间格式化样式。
                可用参数为：地支时、刻、分、秒、忽、微、纤
                当 `刻` 为 `0` 时， `分` 会在其数字之前增加一个“零”字，否则增加的是“又”
                当 `微`、`纤` 任意一个有值时，会在 `微` 的数字前增加一个“余”字
                对于任意计量大小大于 `秒` 的单位，若小于其计量大小的所有单位之值皆为 `0` 时，其后会增加一个“整”字
                除 `地支时` 外，其余参数皆自带单位

        返回值
        ----
            str时间字符串
        """
        return self.time_in_hànzì(格式文本=formatter)

    def hànzì(self) -> str:
        return " ".join(
            (
                self.date_in_hànzì(),
                self.time_in_hànzì(),
            )
        )

    def hanzify(self) -> str:
        """
        返回以汉语表示的完整日期和时间
        """
        return self.hànzì()

    @property
    def chinese_text(self) -> str:
        """
        以汉语表示的传统日期时间字符串
        """
        return self.hanzify()

    def to_western_format(self) -> "DateTime":
        return DateTime.from_chinese_format(
            self.western_year,
            self.chinese_calendar_month,
            self.is_leap_month,
            self.chinese_calendar_day,
            self.shichen,
            self.quarters,
            self.minutes,
            self.seconds,
            self.microseconds,
        )

    @property
    def westernize(self) -> "DateTime":
        return self.to_western_format()


class DateTime(datetime.datetime):

    @classmethod
    def from_chinese_format(
        cls,
        western_year_: int,
        chinese_calendar_month_: int,
        is_leap_: Optional[bool],
        chinese_calendar_day_: int,
        shichen: Union[int, ShíchenString] = 0,
        quarters: int = 4,
        minutes: int = 0,
        seconds: int = 0,
        microseconds: int = 0,
    ):
        is_leap_ = bool(is_leap_)
        # 确认支持年份、月份数字正误、日期数字正误
        if (
            check_result := analyze_verify_result(
                (
                    lunar_mon_info := verify_chinese_calendar_date(
                        western_year_,
                        chinese_calendar_month_,
                        is_leap_,
                        chinese_calendar_day_,
                    )
                )[0]
            )
        )[0]:
            _hours, _minutes = shíchen_kè_2_hour_minute(
                shichen if isinstance(shichen, int) else shíchen2int(shichen), quarters
            )
            return cls(
                western_year_,
                *get_chinese_new_year(western_year_),
                hour=_hours,
                minute=_minutes + minutes,
                second=seconds,
                microsecond=microseconds,
            ) + datetime.timedelta(
                days=(
                    sum(
                        (lunar_mon_info[1])[
                            : chinese_calendar_month_
                            - (
                                not (
                                    (
                                        is_leap_
                                        and (
                                            chinese_calendar_month_ > lunar_mon_info[2]
                                        )
                                    )
                                    and lunar_mon_info[2]
                                )
                            )
                        ]
                    )
                    - 1
                    + chinese_calendar_day_
                )
            )
        else:
            raise ValueError(
                "农历日期错误：不支持形如 公历{}年 农历{}{}月{}日 的日期表示\n\t可能是{}错误".format(
                    western_year_,
                    "闰" if is_leap_ else "",
                    chinese_calendar_month_,
                    chinese_calendar_day_,
                    check_result[1],
                )
            )

    def to_chinese_format(self) -> "zhDateTime":

        return zhDateTime.from_western_format(
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.second,
            self.microsecond,
        )

    @property
    def chinesize(self) -> "zhDateTime":
        return self.to_chinese_format()
