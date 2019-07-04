import datetime
def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    nDay = None
    if(day == 30 and month == 12):
        nDay = [year+1, 1, 1]
    elif(day == 30 and month != 1):
        nDay = [year, month+1, day+1]
    # elif(day == 30 and month != 1):
    #     nDay = datetime.date(year, month+1, day+1)
    else:
        nDay = [year, month, day+1]
    return nDay

print (nextDay(1999, 12, 30))
print (nextDay(2013, 1, 30))
print (nextDay(2012, 12, 30))
