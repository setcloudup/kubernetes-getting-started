import datetime, time

time.sleep(5)
now = datetime.datetime.now()
next_year = datetime.date.today().year + 1
new_year = datetime.datetime(int(next_year),1,1,00,00,00) 

tdelta = new_year - now 
print("Still {} until new year...".format(tdelta)) 
