from datetime import datetime, timedelta


fmt_in, fmt_out = '%m/%d/%Y', '%d.%m.%Y'
current_dt = datetime.strptime(input(), fmt_in).date()
period = timedelta(days=1)
for _ in range(15):
    current_dt += period
    print(current_dt.strftime(fmt_out))
