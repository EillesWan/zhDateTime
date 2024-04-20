from zhDateTime import DateTime

import zhdate

# print(DateTime.today().to_lunar())

# print(DateTime.today().to_lunar().hànzì())

# print(DateTime.from_lunar(zhdate.ZhDate.today().lunar_year,zhdate.ZhDate.today().lunar_month,zhdate.ZhDate.today().leap_month,zhdate.ZhDate.today().lunar_day).to_lunar().hànzì())

while True:
    print(DateTime.today().to_lunar().hànzì(),end="\r")