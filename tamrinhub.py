def date(year,month,day):
    d = "%d/%d/%d" %(year,month,day)
    print(d)
    print(type(d))
date(day= int(input('Enter day : ')), month= int(input('Enter month : ')), year= int(input('Enter year : ')))