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

__version__ = "2.0.2.1"
__all__ = [
    # 所用之函数
    "shichen_ke_2_hour_minute",
    "hour_minute_2_shichen_ke",
    "get_chinese_calendar_month_list",
    "get_chinese_new_year",
    "verify_chinese_calendar_date",
    "int_group",
    "int_group_seperated",
    "int_2_grouped_han_str",
    "lkint_hanzify",
    "int_hanzify",
    # 所用之类
    "zhDateTime",
    "DateTime",
    # 所用之数据类型标记
    "CelestialStem",
    "TerrestrialBranch",
    "ShíchenString",
    "XXIVShíChenString",
    "HànziNumericUnitsString",
    # 所用之常量
    "NUM_IN_HANZI",
    "CELESTIAL_STEMS",
    "TERRESTRIAL_BRANCHES",
    "CHINESE_ZODIACS",
]


from .main import (
    # 所用之函数
    shíchen_kè_2_hour_minute,
    hour_minute_2_shíchen_kè,
    get_chinese_calendar_month_list,
    get_chinese_new_year,
    verify_chinese_calendar_date,
    int_group,
    int_group_seperated,
    int_2_grouped_hàn_str,
    lkint_hànzìfy,
    int_hànzìfy,
    # 所用之类
    zhDateTime,
    DateTime,
)

from .types import (
    ShíchenString,
    XXIVShíChenString,
    HànziNumericUnitsString,
    CelestialStem,
    TerrestrialBranch,
)

from .constants import (
    NUM_IN_HANZI,
    CELESTIAL_STEMS,
    TERRESTRIAL_BRANCHES,
    CHINESE_ZODIACS,
)

shichen_ke_2_hour_minute = shíchen_kè_2_hour_minute
hour_minute_2_shichen_ke = hour_minute_2_shíchen_kè
int_2_grouped_han_str = int_2_grouped_hàn_str
lkint_hanzify = lkint_hànzìfy
int_hanzify = int_hànzìfy
