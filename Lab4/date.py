import datetime

#ex 1
today = datetime.date.today()
five_days_ago = today - datetime.timedelta(days=5)
print(five_days_ago)

#ex 2
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(yesterday, today, tomorrow)

#ex 3 
now_time = datetime.datetime.now()
print(now_time.strftime("%Y-%m-%d %H:%M:%S"))

#ex 4
d1 = datetime.datetime(year = int(input("Enter year:")),
                       month = int(input("Enter month:")),
                       day = int(input("Enter day:")),
                       hour = int(input("Enter hour:")),
                       minute = int(input("Enter minute:")),
                       second = int(input("Enter second:"))
                       )

d2 = datetime.datetime(year = int(input("Enter year:")),
                       month = int(input("Enter month:")),
                       day = int(input("Enter day:")),
                       hour = int(input("Enter hour:")),
                       minute = int(input("Enter minute:")),
                       second = int(input("Enter second:"))
                       )

difference = abs(d2 - d1)
print(f"difference between these times is {difference.seconds} seconds")


