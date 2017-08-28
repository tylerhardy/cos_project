import datetime

last_visit = datetime.datetime.strptime("2017-08-28", '%Y-%m-%d')
# datetime.date.strftime
print(last_visit)
print(datetime.datetime.now())
print(datetime.datetime.today())
def is_past_due(last_visit):
    d_14 = datetime.datetime.today() - datetime.timedelta(days=14)
    d_28 = datetime.datetime.today() - datetime.timedelta(days=28)

    if last_visit is None:
        print('no_visit_performed')
    elif last_visit > d_14:
        print('visit_good')
    elif (last_visit < d_14) and (last_visit > d_28):
        print('visit_old')
    elif last_visit < d_28:
        print('need_visit')
    else:
        print('error')

is_past_due(last_visit)