def convert_to_persian(date: str): # format = 'yyyy/mm/dd'
    gy, gm, gd = map(int, date.split('/'))
    leap = False

    jy: int = 0
    jm: int = 0
    jd: int = 0

    if ( gy % 4 == 0 and gy % 100 != 0 ) or (gy % 400 == 0):
        leap = True
    passed_days = [0 , 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    days = 355666 + 365 * gy + (gy + 3) // 4 - (gy + 99) // 100 + (gy + 399) // 400 + gd + passed_days[gm - 1]
    if gm > 2 and leap:
        days += 1
    
    jy = -1595 + 33 * (days // 12053)
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461

    if days > 365:
        jy += (days - 1) // 365
        days = (days - 1) % 365

    if days < 186:
        jm = 1 + days // 31
        jd = 1 + (days % 31)
    else:
        jm = 7 + (days - 186) // 30
        jd = 1 + ((days - 186) % 30)

    return f"{str(jy).zfill(4)}/{str(jm).zfill(2)}/{str(jd).zfill(2)}"
