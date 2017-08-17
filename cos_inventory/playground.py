import datetime
# audited_date = None
audited_date = datetime.datetime.strptime('03 15 2016', '%m %d %Y')
def is_past_due(audited_date):
    d_180 = datetime.datetime.today() - datetime.timedelta(days=180)
    d_365 = datetime.datetime.today() - datetime.timedelta(days=365)
    if audited_date is None:
        return print("no_audit_performed")
    if audited_date > d_180:
        return print("audit_good")
    elif (audited_date < d_180) and (audited_date > d_365):
        return print("audit_old")
    elif audited_date < d_365:
        return print("need_audit")
    else:
        return print("missing_info")

is_past_due(audited_date)