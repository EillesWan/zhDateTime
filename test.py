from zhDateTime import DateTime, int_hànzìfy

import random
import datetime

# 时区相差

print(
    DateTime.now(
        datetime.timezone(
            datetime.timedelta(hours=8, minutes=-40),
        )
    )
    .to_lunar()
    .hanzify()
)

# import zhdate

# print(DateTime.today().to_lunar())

print(DateTime.today().to_lunar().hànzì())
print(
    "{} 是 {}\n".format(
        it := random.randint(1000000, 10000000000000000), int_hànzìfy(it)
    )
)


# print(DateTime.from_lunar(zhdate.ZhDate.today().lunar_year,zhdate.ZhDate.today().lunar_month,zhdate.ZhDate.today().leap_month,zhdate.ZhDate.today().lunar_day).to_lunar().hànzì())

while True:
    print(DateTime.today().to_lunar().hànzì(), end="    \r")
