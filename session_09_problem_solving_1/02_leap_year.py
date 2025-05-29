# Leap Year

from datetime import datetime

def is_leap_year(year):
	return(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

current_year = datetime.now().year

if is_leap_year(current_year):
	print(f"{current_year} is a Leap Year.")
else:
	print(f"{current_year} is not a Leap Year.")