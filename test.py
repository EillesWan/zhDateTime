from pyLunar import LunarDate

import zhdate

print(LunarDate.from_lunar(zhdate.ZhDate.today().lunar_year,zhdate.ZhDate.today().lunar_month,zhdate.ZhDate.today().leap_month,zhdate.ZhDate.today().lunar_day))

