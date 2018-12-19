import datetime
today=datetime.datetime.today().weekday()   #print the day of today
string=''                                   #and print len(today) times
if today == 0:
    string = 'Monday'
if today == 1:
    string ='Tuesday'
if today == 2:
    string = 'Wednesday'
if today == 3:
    string = 'Thursday'
if today == 4:
    string = 'Friday'
if today == 5:
    string = 'Saturday'
if today == 6:
    string = 'Sunday'
for x in range(0,len(string)):
    print(string)
