# -*- coding: utf-8 -*-

"""
版权所有 © 2024 金羿ELS
Copyright (R) 2024 Eilles Wan

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

__version__ = "1.0.1"
__all__ = [
    # 所用之函数
    "shichen_ke_2_hour_minute",
    "hour_minute_2_shichen_ke",
    "get_lunar_month_list",
    "get_lunar_new_year",
    "verify_lunar_date",
    "int_group",
    "int_group_seperated",
    "int_2_grouped_han_str",
    "lkint_hanzify",
    "int_hanzify",
    # 所用之类
    "zhDateTime",
    "DateTime",
    # 所用之数据类型标记
    "ShíchenString",
    "XXIVShíChenString",
    "HànziNumericUnitsString",
    # 所用之常量
    "TIANGAN",
    "DIZHI",
    "HANNUM",
    "SHENGXIAO",
]


from .main import (
    # 所用之函数
    shíchen_kè_2_hour_minute,
    hour_minute_2_shíchen_kè,
    get_lunar_month_list,
    get_lunar_new_year,
    verify_lunar_date,
    int_group,
    int_group_seperated,
    int_2_grouped_hàn_str,
    lkint_hànzìfy,
    int_hànzìfy,
    # 所用之类
    zhDateTime,
    DateTime,
    # 所用之数据类型标记
    ShíchenString,
    XXIVShíChenString,
    HànziNumericUnitsString,
    # 所用之常量
    TIĀNGĀN,
    DÌZHĪ,
    HANNUM,
    SHĒNGXIÀO,
)

from .constants import (
    TIANGAN,
    DIZHI,
    SHENGXIAO,
)

shichen_ke_2_hour_minute = shíchen_kè_2_hour_minute
hour_minute_2_shichen_ke = hour_minute_2_shíchen_kè
int_2_grouped_han_str = int_2_grouped_hàn_str
lkint_hanzify = lkint_hànzìfy
int_hanzify = int_hànzìfy
