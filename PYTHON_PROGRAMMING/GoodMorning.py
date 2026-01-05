
import time

print(time.strftime('%Y-%m-%d %H:%M:%S'))

if (time.strftime('%H:%M') >= '00:00') and (time.strftime('%H:%M') <= '11:59'):
    print("Good Morning")
elif (time.strftime('%H:%M') >= '12:01') and (time.strftime('%H:%M') <= '17:00'):
    print("Good Afternoon")
elif (time.strftime('%H:%M') >= '17:01') and (time.strftime('%H:%M') <= '21:00'):
    print("Good Evening")
else :
    print("Good Night")
