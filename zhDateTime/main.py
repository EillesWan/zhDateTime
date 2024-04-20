# -*- coding: utf-8 -*-

"""
版权所有 © 2024 金羿ELS
Copyright (R) 2024 Eilles Wan

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

import datetime
from dataclasses import dataclass

from .types import (
    Tuple,
    List,
    Optional,
    Union,
    Callable,
    ShíchenString,
    XXIVShíChenString,
    HànziNumericUnitsString,
)
from .constants import (
    LUNAR_NEW_YEAR_DATE,
    LUNAR_MONTH_PER_YEAR,
    LEAP_SIZE,
    TIĀNGĀN,
    DÌZHĪ,
    HANNUM,
    SHĒNGXIÀO,
    YUÈFÈN,
    HÀNUNIT10P,
    XXIVSHÍCHEN,
    HÀNUNITLK,
    HÀNUNITRW,
)

"""
    警告
本软件之源码中包含大量简体汉语，不懂的话请自行离开。

    注意
此軟體源碼内含大量簡化字，如有不解請勿觀看。

    WARNING
This source code contains plenty of simplified Han characters.

    诫曰
众汉语字含于此软件源码，非通勿入。
"""


def get_lunar_new_year(solar_year: int) -> Tuple[int, int]:
    """
    依据提供的公历年份，返回当年的农历新年所在的公历日期

    参数
    ----
        solar_year: int 公历年份

    返回值
    ------
        Tuple(int公历月, int公历日, )农历新年日期
    """
    new_year_code = LUNAR_NEW_YEAR_DATE[solar_year - 1900]
    return new_year_code // 100, new_year_code % 100


month_days_bs: Callable[[Union[bool, int]], int] = lambda big_or_small: (
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

month_days_pusher: Callable[[int, int], int] = lambda month_code, push_i: month_days_bs(
    (month_code >> push_i) & 0x1
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


def decode_lunar_month_code(
    month_code: int, leap_days: int = 0
) -> Tuple[List[int], int]:
    """
    依据提供的农历月份信息码，求取当年每月天数之列表及闰月月份

    参数
    ----
        month_code: int 当月月份信息，为16位整数数据，其末12位当为一年的大小月排布信息
        leap_days: int 当年闰月之天数，若为0则无闰

    返回值
    ------
        Tuple(List[int当月天数, ]当年每月天数, int闰月之月份, )当年每月天数列表及闰月月份
    """
    leap_month = month_code & 0b1111000000000000
    return (
        [month_days_pusher(month_code, i) for i in range(leap_month)][::-1]
        + [
            leap_days,
        ]
        + [month_days_pusher(month_code, i) for i in range(leap_month, 12)][::-1]
        if leap_month
        else [month_days_pusher(month_code, i) for i in range(12)][::-1]
    ), leap_month


get_lunar_month_code: Callable[[int], int] = lambda solar_year: int.from_bytes(
    LUNAR_MONTH_PER_YEAR[(solar_year - 1900) * 2 : (solar_year - 1899) * 2],
    "big",
)
"""
依据提供的公历年份，返回当年的农历月份信息码

参数
----
    solar_year: int 公历年份

返回值
------
    int 农历月份信息码
"""

get_lunar_leap_size: Callable[[int], int] = lambda solar_year: month_days_bs(
    (LEAP_SIZE >> (solar_year - 1900)) & 0x1
)
"""
依据提供的公历年份，通过判断当年的农历中是否有大闰月，给出其闰月应为几天

注意，倘若本年无闰月，也会给出闰月天数为29天

参数
----
    solar_year: int 公历年份

返回值
------
    int 闰月天数
"""


get_lunar_month_list: Callable[[int], Tuple[List[int], int]] = (
    lambda solar_year: decode_lunar_month_code(
        get_lunar_month_code(solar_year),
        get_lunar_leap_size(solar_year),
    )
)
"""
依据提供的公历年份，给出当年每月天数之列表及闰月月份

参数
----
    solar_year: int 公历年份

返回值
------
    Tuple(List[int当月天数, ]当年每月天数, int闰月之月份, )当年每月天数列表及闰月月份
"""


verify_lunar_date: Callable[[int, int, bool, int], Tuple[bool, int, int]] = (
    lambda lunar_year, lunar_month, is_leap, lunar_day: (
        (
            (1900 <= lunar_year <= 2100)  # 确认年份范围
            and (1 <= lunar_month <= 12)  # 确认月份范围
            and (
                (  # 当为闰月时
                    1
                    <= lunar_day
                    <= (leap_days := get_lunar_leap_size(lunar_year))  # 获取闰月日数
                    and (
                        lunar_month
                        == (lunar_month_code := get_lunar_month_code(lunar_year))
                    )  # 确认此月闰月与否
                )
                if is_leap
                else (  # 当非闰月时，确认日期范围
                    (leap_days := 0)  # 非闰月的闰月日期数位0
                    < lunar_day
                    <= (  # 获取当月日数
                        month_days_pusher(
                            (lunar_month_code := get_lunar_month_code(lunar_year)),
                            lunar_month,
                        )
                    )
                )
            )
        ),
        lunar_month_code,
        leap_days,
    )
)
"""
校验所给出之农历日期是否符合本库之可用性

参数
----
    lunar_year: int 农历年份
    lunar_month: int 农历月份
    is_leap: bool 当月是否为闰月
    lunar_day: int 当月天数

返回值
------
    Tuple(bool该日期是否可用, int当年农历月份信息码, int当年闰月天数)
"""


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
        else DÌZHĪ.find(dìzhī[0])
    )
    # 其实，二十四时辰完全可以算的出来，而不用index这样丑陋
    # 但是，平衡一下我们所需要的时间和空间
    # 不难发现，如果利用计算来转，虽然对空间需求确实减少了
    # 但是消耗的计算量是得不偿失的，更何况计算还占一部分内存
    # 有人曾经对我说，小于一千字节的内存优化都等于没有
    # 我也坚信在现在这个时代实实在在是这样的
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


def int_grouping(integer: int) -> List[Union[int, HànziNumericUnitsString]]:
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
    # 的数吧
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


def int_2_grouped_hàn(integer: int) -> List[Union[int, HànziNumericUnitsString]]:
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
    for ppc in int_grouping(integer):
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
    return "".join([str(i) for i in int_2_grouped_hàn(integer)])


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
    if integer == 0:
        return "零"
    elif integer == 10:
        return "十"
    elif integer < 100:
        if integer % 10 == 0:
            return HANNUM[integer // 10] + "十"
        elif integer < 30:
            if integer > 20:
                return "廿" + HANNUM[integer % 10]
            elif integer > 10:
                return "十" + HANNUM[integer % 10]
            else:
                return HANNUM[integer % 10]
        else:
            return HANNUM[integer // 10] + "十" + HANNUM[integer % 10]
    elif integer < 1000:
        if integer % 100 == 0:
            return HANNUM[integer // 100] + "百"
        elif (integer // 10) % 10 == 0:
            return HANNUM[integer // 100] + "百零" + HANNUM[integer % 10]
        else:
            return (
                HANNUM[integer // 100]
                + "百"
                + HANNUM[(integer // 10) % 10]
                + "十"
                + (HANNUM[integer % 10] if integer % 10 else "")
            )
    else:
        if integer % 1000 == 0:
            return HANNUM[integer // 1000] + "千"
        elif (integer // 100) % 10 == 0:
            if (integer // 10) % 10 == 0:
                return HANNUM[integer // 1000] + "千零" + HANNUM[integer % 10]
            else:
                return (
                    HANNUM[integer // 1000]
                    + "千零"
                    + HANNUM[(integer // 10) % 10]
                    + "十"
                    + (HANNUM[integer % 10] if integer % 10 else "")
                )
        else:
            return HANNUM[integer // 1000] + "千" + lkint_hànzìfy(integer % 1000)


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
            for i in int_2_grouped_hàn(integer)
        ]
    )


@dataclass(init=False)
class zhDateTime:
    """
    中式传统日期时间
    """

    lunar_year: int
    lunar_month: int
    is_leap_month: bool
    lunar_day: int
    shichen: int
    quarters: int
    minutes: int
    seconds: int
    microseconds: int

    def __init__(
        self,
        lunar_year_: int,
        lunar_month_: int,
        is_leap_: Optional[bool],
        lunar_day_: int,
        shichen_: Union[int, ShíchenString] = 0,
        quarters_: int = 4,
        minutes_: int = 0,
        seconds_: int = 0,
        microseconds_: int = 0,
    ) -> None:
        is_leap_ = bool(is_leap_)
        # 确认支持年份、月份数字正误、日期数字正误
        if verify_lunar_date(lunar_year_, lunar_month_, is_leap_, lunar_day_)[0]:
            self.lunar_year = lunar_year_
            self.lunar_month = lunar_month_
            self.lunar_day = lunar_day_
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
                "农历日期错误：不支持形如 {}年{}{}月{}日 的日期表示".format(
                    lunar_year_, "闰" if is_leap_ else "", lunar_month_, lunar_day_
                )
            )

    @classmethod
    def from_solar(
        cls,
        solar_year: int,
        solar_month: int,
        solar_day: int,
        hour: int = 0,
        minute: int = 0,
        second: int = 0,
        microsecond: int = 0,
    ):
        # 若未至农历新年，则农历年份为公历之去年；而后求得距农历当年之新年所差值值
        passed_days = (
            datetime.date(solar_year, solar_month, solar_day)
            - datetime.date(
                (
                    lunar_year := solar_year
                    - (lambda a, c, d: ((a[0] > c) or (a[0] == c and a[1] > d)))(
                        get_lunar_new_year(solar_year), solar_month, solar_day
                    )
                ),
                *get_lunar_new_year(lunar_year),
            )
        ).days
        # 取得本农历年之月份表
        month_info, leap_month = get_lunar_month_list(lunar_year)
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
            lunar_year,
            temp_month - ((leap_month > 0) and (temp_month > leap_month)),
            (leap_month > 0) and (temp_month == leap_month + 1),
            passed_days - sum(months) + 1,
            *hour_minute_2_shíchen_kè(hour, (minute := (minute + (second // 60)))),
            minute % 15,
            (second % 60) + (microsecond // 1000000),
            microsecond % 1000000,
        )

    def __str__(self) -> str:
        return "农历 {}年{}{}月{}日 {}时{}刻{}分{}秒{}".format(
            self.lunar_year,
            "闰" if self.is_leap_month else "",
            self.lunar_month,
            self.lunar_day,
            self.shichen,
            self.quarters,
            self.minutes,
            self.seconds,
            self.microseconds,
        )

    def __add__(self, time_delta: datetime.timedelta):
        return (self.to_solar() + time_delta).to_lunar()

    def __sub__(self, datetime_delta):
        if isinstance(datetime_delta, datetime.timedelta):
            return (self.to_solar() - datetime_delta).to_lunar()
        elif isinstance(datetime_delta, DateTime):
            return self.to_solar() - datetime_delta
        elif isinstance(datetime_delta, zhDateTime):
            return self.to_solar() - datetime_delta.to_solar()
        else:
            raise TypeError("加减单位不合理：你在用什么相减？")

    def date_hànzì(self) -> str:
        return "{汉字数字} {天干地支年}{生肖}年{月份}月{日期}日".format(
            汉字数字="".join(
                [HANNUM[(self.lunar_year // (10**i)) % 10] for i in range(3, -1, -1)]
            ),
            天干地支年=TIĀNGĀN[(yc := (self.lunar_year - 1984) % 60) % 10]
            + DÌZHĪ[yc % 12],
            生肖=SHĒNGXIÀO[(self.lunar_year - 1984) % 12],
            月份=YUÈFÈN[self.lunar_month].replace("⑾", "十一"),
            日期=(
                HANNUM[self.lunar_day // 10] + "十"
                if ((self.lunar_day % 10 == 0) and (self.lunar_day > 10))
                else HÀNUNIT10P[self.lunar_day // 10]
                + (HANNUM[self.lunar_day % 10] if self.lunar_day % 10 else "")
            ),
        )

    def date_hanzify(self) -> str:
        return self.date_hànzì()

    def time_hànzì(self) -> str:
        return "{地支时}时{刻} {分}{秒}{忽} {微}{纤}".format(
            地支时=DÌZHĪ[self.shichen]
            + (
                ""
                if (
                    (self.quarters)
                    or (self.minutes)
                    or (self.seconds)
                    or (self.microseconds)
                )
                else "整"
            ),
            刻=(
                HANNUM[self.quarters]
                + "刻"
                + (
                    ""
                    if ((self.minutes) or (self.seconds) or (self.microseconds))
                    else "整"
                )
            ),
            分=(
                ("又" if self.quarters else "零")
                + (
                    (
                        lkint_hànzìfy(self.minutes)
                        + "分"
                        + ("" if ((self.seconds) or (self.microseconds)) else "整")
                    )
                    if self.minutes
                    else ""
                )
            ),
            秒=(
                lkint_hànzìfy(self.seconds)
                + "秒"
                + ("" if (self.microseconds) else "整")
            ),
            忽=(
                HANNUM[(self.microseconds // 100000) % 10]
                + HANNUM[(self.microseconds // 10000) % 10]
            ).replace("〇", "零"),
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
                if (
                    (wēi := ((self.microseconds // 100) % 100))
                    or (self.microseconds % 100)
                )
                else ""
            ),
            纤=(
                (lkint_hànzìfy(xiān) + "纤")
                if (xiān := (self.microseconds % 100))
                else ""
            ),
        )

    def time_hanzify(self) -> str:
        return self.time_hànzì()

    def hànzì(self) -> str:
        return "{汉字日期} {汉字时刻}".format(
            汉字日期=self.date_hànzì(),
            汉字时刻=self.time_hànzì(),
        )

    def hanzify(self) -> str:
        return self.hànzì()

    def to_solar(self):
        return DateTime.from_lunar(
            self.lunar_year,
            self.lunar_month,
            self.is_leap_month,
            self.lunar_day,
            self.shichen,
            self.quarters,
            self.minutes,
            self.seconds,
            self.microseconds,
        )


class DateTime(datetime.datetime):

    @classmethod
    def from_lunar(
        cls,
        lunar_year: int,
        lunar_month: int,
        is_leap: Optional[bool],
        lunar_day: int,
        shichen: Union[int, ShíchenString] = 0,
        quarters: int = 4,
        minutes: int = 0,
        seconds: int = 0,
        microseconds: int = 0,
    ):
        is_leap = bool(is_leap)
        # 确认支持年份、月份数字正误、日期数字正误
        if (
            lunar_mon_info := verify_lunar_date(
                lunar_year, lunar_month, is_leap, lunar_day
            )
        )[0]:
            _hours, _minutes = shíchen_kè_2_hour_minute(
                shichen if isinstance(shichen, int) else shíchen2int(shichen), quarters
            )
            return cls(
                lunar_year,
                *get_lunar_new_year(lunar_year),
                hour=_hours,
                minute=_minutes + minutes,
                second=seconds,
                microsecond=microseconds,
            ) + datetime.timedelta(
                days=(
                    sum(
                        (month_data := decode_lunar_month_code(*lunar_mon_info[1:]))[0][
                            : lunar_month
                            - (
                                not (
                                    (is_leap and (lunar_month > month_data[1]))
                                    and month_data[1]
                                )
                            )
                        ]
                    )
                    - 1
                    + lunar_day
                )
            )
        else:
            raise ValueError(
                "农历日期错误：不支持形如 {}年{}{}月{}日 的日期表示".format(
                    lunar_year, "闰" if is_leap else "", lunar_month, lunar_day
                )
            )

    def to_lunar(self) -> zhDateTime:

        return zhDateTime.from_solar(
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.second,
            self.microsecond,
        )
