import random

import time

def getRandomDate(starDate, endDate):
    print("\nPrinting random date between", starDate, "and", endDate)
    
    randomGenerator = random.random()
    
    dateFormat = '%m/%d/%Y'
    
    starttime = time.mktime(time.strptime(starDate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))
    
    randomTime = starttime + randomGenerator * (endtime - starttime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    
    return randomDate



print("\nRandom Date = ", getRandomDate("1/1/2020", "12/12/2026"))

