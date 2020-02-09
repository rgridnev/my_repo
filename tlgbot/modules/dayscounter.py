import datetime

def dayscounter(year,mon,day, dest):
    now = datetime.datetime.today()
    NY = datetime.datetime(year,mon,day)
    d = NY-now #  str(d)  '83 days, 2:43:10.517807'
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    #result='1'
    #result=str(print(dest, 'через {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))
    #result=print(dest, 'через {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))
    mmm = (dest, 'через {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))
    rrr=' '.join(mmm)
    return rrr