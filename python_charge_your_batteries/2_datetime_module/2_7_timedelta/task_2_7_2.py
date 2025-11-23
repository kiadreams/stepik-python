from datetime import datetime, timedelta


fmt_in, fmt_out = '%d-%m-%Y', '%d.%m.%Y'
current_dt = datetime.strptime(input(), fmt_in).date()
before_30_days = current_dt - timedelta(days=30)
after_30_days = current_dt + timedelta(days=30)
print(
    f'30 days before current date: {before_30_days.strftime(fmt_out)}',
    f'Current Date: {current_dt.strftime(fmt_out)}',
    f'30 days after current date: {after_30_days.strftime(fmt_out)}',
    sep='\n'
)
