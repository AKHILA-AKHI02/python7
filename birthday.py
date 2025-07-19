import datetime
ob=datetime.datetime.now()
print("Enter your date of birth:")
dd=int(input("date:"))
mm=int(input("month:"))
yy=int(input("year:"))
bday=datetime.datetime(yy,mm,dd)
print("Total days spent on earth:",(ob-bday).days)
