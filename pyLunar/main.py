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
from typing import Tuple, List, Optional, Union, Callable

from .constants import LUNAR_NEW_YEAR_DATE, LUNAR_MONTH_PER_YEAR, LEAP_SIZE


def get_lunar_new_year(solar_year: int) -> Tuple[int, int]:
    new_year_code = LUNAR_NEW_YEAR_DATE[solar_year - 1900]
    return new_year_code // 100, new_year_code % 100


month_days_bs: Callable[[Union[bool, int]], int] = lambda big_or_small: (
    30 if big_or_small else 29
)

month_days_pusher: Callable[[int, int], int] = lambda month_code, push_i: month_days_bs(
    (month_code >> push_i) & 0x1
)


def get_lunar_month_list_from_month_code(
    month_code: int, leap_days: int = 0
) -> Tuple[List[int], int]:
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


decode_lunar_month_code: Callable[[int], int] = lambda solar_year: int.from_bytes(
    LUNAR_MONTH_PER_YEAR[(solar_year - 1900) * 2 : (solar_year - 1899) * 2],
    "big",
)


get_lunar_month_list: Callable[[int], Tuple[List[int], int]] = (
    lambda lunar_year: get_lunar_month_list_from_month_code(
        decode_lunar_month_code(lunar_year),
        month_days_bs((LEAP_SIZE >> (lunar_year - 1900)) & 0x1),
    )
)

verify_legal_lunar_date: Callable[[int, int, bool, int], Tuple[bool, int, int]] = (
    lambda lunar_year, lunar_month, is_leap, lunar_day: (
        (
            (1900 <= lunar_year <= 2100)  # 确认年份范围
            and (1 <= lunar_month <= 12)  # 确认月份范围
            and (
                (  # 当为闰月时
                    1
                    <= lunar_day
                    <= (
                        leap_days := month_days_bs(
                            (LEAP_SIZE >> (lunar_year - 1900)) & 0x1
                        )  # 获取顿月日数
                    )
                    and (
                        lunar_month
                        == (lunar_month_code := decode_lunar_month_code(lunar_year))
                    )  # 确认此月闰月与否
                )
                if is_leap
                else (  # 当非闰月时，确认日期范围
                    (leap_days := 0)
                    < lunar_day
                    <= (  # 获取当月日数
                        month_days_pusher(
                            (lunar_month_code := decode_lunar_month_code(lunar_year)),
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


@dataclass(init=False)
class LunarDateInfo:
    lunar_year: int
    lunar_month: int
    is_leap_month: bool
    lunar_day: int

    def __init__(
        self, lunar_year: int, lunar_month: int, is_leap: Optional[bool], lunar_day: int
    ) -> None:
        pass    # 未完待续


class LunarDate(datetime.datetime):

    @classmethod
    def from_lunar(
        cls,
        lunar_year: int,
        lunar_month: int,
        is_leap: Optional[bool],
        lunar_day: int,
    ):
        is_leap = bool(is_leap)
        # 确认支持年份、月份数字正误、日期数字正误
        if lunar_mon_info := verify_legal_lunar_date(
            lunar_year, lunar_month, is_leap, lunar_day
        ):
            return cls(
                lunar_year, *get_lunar_new_year(lunar_year)
            ) + datetime.timedelta(
                days=(
                    sum(
                        (
                            month_data := get_lunar_month_list_from_month_code(
                                *lunar_mon_info[1:]
                            )
                        )[0][
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

    def to_lunar_date_info(self) -> str:

        return "农历{}年{}{}月{}日".format(
            self.year
            - (
                0
                < (
                    datetime.datetime(self.year, *get_lunar_new_year(self.year)) - self
                ).total_seconds()
            ),
            # 未完待续
        )
