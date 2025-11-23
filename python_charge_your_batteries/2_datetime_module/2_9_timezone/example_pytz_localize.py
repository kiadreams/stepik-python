from datetime import datetime

import pytz

fmt = '%Y-%m-%d %H:%M:%S %Z%z'

# Indian Standard Time
tz_india = pytz.timezone('Asia/Kolkata')
ist_local = tz_india.localize(datetime.now())
print("Indian Standard Time:", ist_local.strftime(fmt))
print('-------------')

# Europe/Amsterdam Time
amdam_tz = pytz.timezone('Europe/Amsterdam')
dt = datetime(1983, 8, 3, 2, 0, 0)
cest_local = amdam_tz.localize(dt)
print("Amsterdam time:", amdam_tz.localize(dt))
print("Indian time:", tz_india.localize(dt))
