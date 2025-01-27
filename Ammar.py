# Créé par Ordinateur, le 03/04/2020
from __future__ import division
from lycee import *
def isbissextile(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def daysinmonth(month, year):
    if month == 2:
        if isbissextile(year):
            return 29
        else:
            return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif 0 > month or month > 12:
        return 0
    else:
        return 31


def daysinyear(year):
    if isbissextile(year):
        return 366
    else:
        return 365


def valid(day, month, year):
    if 0 < day <= daysinmonth(month, year):
        return True
    else:
        return False


def validdate(birthday, birthmonth, birthyear, todayday, todaymonth, todayyear):
    if birthyear > todayyear:
        return False
    elif birthyear == todayyear:
        if birthmonth == todaymonth:
            if birthday <= todayday:
                return True
            else:
                return False
        elif birthmonth < todaymonth:
            return True
        else:
            return False
    else:
        return True


def birthday(birthday, birthmonth, birthyear, todayday, todaymonth, todayyear):
    nbdays = 0
    if not valid(birthday, birthmonth, birthyear) or not valid(todayday, todaymonth, todayyear):
        return "Please enter a valid date"
    if not validdate(birthday, birthmonth, birthyear, todayday, todaymonth, todayyear):
        return "The birthday should come before the date!!"
    if birthday != 1 and birthyear != todayyear:
        while birthday < daysinmonth(birthmonth, birthyear):
            nbdays += 1
            birthday += 1
    while birthyear < todayyear - 1:
        nbdays += daysinyear(birthyear)
        birthyear += 1
    while birthyear != todayyear or birthmonth != todaymonth or birthday != todayday:
        if birthday < daysinmonth(birthmonth, birthyear):
            nbdays += 1
            birthday += 1
        elif birthmonth < 12:
            nbdays += 1
            birthmonth += 1
            birthday = 1
        else:
            nbdays += 1
            birthyear += 1
            birthmonth = 1
            birthday = 1
    return nbdays


def main():
    print(validdate(13, 4, 1999, 1, 4, 2020))
    print(valid(1, 4, 2000))
    print(birthday(13, 4, 1999, 1, 4, 2020))


if __name__ == '__main__':
    main()