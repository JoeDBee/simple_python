import datetime


def get_birthday():
    print("When were you born?\n")
    year = int(input("Year [YYYY]: \n"))
    month = int(input("Month [MM]: \n"))
    day = int(input("Day [DD]: \n"))

    birthday = datetime.date(year, month, day)

    return birthday


def days_from_birthday(birthday):
    ts = datetime.date.today()
    # map birthday days to current timestamp year and get the difference
    dt_days = datetime.date(ts.year, birthday.month, birthday.day) - ts
    dt_year = ts - birthday
    dt_year = round(dt_year.days/365.25)

    return {'dt1': dt_days.days, 'dt2': dt_year}


def print_birthday_info(info):
    age = info["dt2"]
    days = info["dt1"]
    print('You are currently {} years old \n'.format(age))
    if days > 0:
        print('Your birthday is in {} days \n'.format(days))
    elif days < 0:
        print('Your birthday was {} days ago \n'.format(days))
    elif days == 0:
        print('Your birthday is today... Happy Birthday!\n')


def main():
    print('---------------------')
    print('   Birthday App      ')
    print('---------------------')

    bday = get_birthday()
    bday_info = days_from_birthday(bday)
    print_birthday_info(bday_info)


main()
