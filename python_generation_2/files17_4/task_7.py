def name_is_fitting(line: str) -> str:
    name, start_time, end_time = line.split(',')
    hours_s, minits_s = map(int, start_time.strip().split(':'))
    hours_e, minits_e = map(int, end_time.strip().split(':'))
    duaration = (hours_e - hours_s)*60 + (minits_e - minits_s)
    return name if duaration >= 60 else ''


with (open('17_4_files/logfile.txt', encoding='utf-8') as log_f,
      open('17_4_files/output.txt', 'w', encoding='utf-8') as out_f):
    for line in log_f:
        if name := name_is_fitting(line):
            print(name, file=out_f)
