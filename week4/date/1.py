import datetime
from datetime import date

cd = date.today()
fd = cd + datetime.timedelta(days=-5)
print(fd)