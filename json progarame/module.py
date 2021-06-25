import platform
import datetime


x = platform.system()
print(x)


#import platform

#x1 = dir(platform)
#print(x1)



x = datetime.datetime.now()
print(x)


#x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
