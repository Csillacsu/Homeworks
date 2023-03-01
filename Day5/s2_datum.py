##### Dátumkezelés

# import datetime
# current_datetime = datetime.datetime.now()
# print(current_datetime)
# print(type(current_datetime))

from datetime import datetime, date, time, timezone

### DATETIME
# current_datetime = datetime.now()
#
# select_datetime = datetime(2020, 1, 23, 12, 12, 54)
# print(select_datetime)
# print(type(select_datetime))
#
# print(select_datetime.date())
# print(select_datetime.time())
# print(select_datetime.year)
# print(select_datetime.month)
# print(select_datetime.day)
# print(select_datetime.hour)
# print(select_datetime.minute)
# print(select_datetime.second)
# print(select_datetime.microsecond)
#
# test_datetime = datetime(2012, 12, 14)
# print(test_datetime)
# test2 = datetime(15, 32, 43)
# test3 = datetime(, , , 15, 32, 43)

### DATE
# todays_date = date.today()
# print(todays_date)
#
# select_date = date(2022, 1, 1)
# print(select_date)
# print(type(select_date))
#
# test_date = todays_date - select_date
# print(test_date)
#
# print(select_date.year)
# print(select_date.month)
# print(select_date.day)

#### TIME
# current_time = datetime.now().time()
# print(current_time)
# current_add = current_time + 61
# print(current_add)

#
# print(current_time.hour)
# print(current_time.minute)
# print(current_time.second)
# print(current_time.microsecond)

#### TIMEZONE
# print(datetime.now())
# print(datetime.now(timezone.utc))

#### formázás
