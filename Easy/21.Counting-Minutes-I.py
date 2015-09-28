# Using the Python language, have the function CountingMinutesI(str) take the str parameter being passed 
# which will be two times (each properly formatted with a colon and am or pm) separated by a hyphen 
# and return the total number of minutes between the two times. 
# The time will be in a 12 hour clock format. For example: if str is 9:00am-10:00am then the output should be 60. 
# If str is 1:00pm-11:00am the output should be 1320. 

def CountingMinutesI(str):
    times = str.split("-")
    time1 = times[0][:-2], times[0][-2:]
    time2 = times[1][:-2], times[1][-2:]
    hours12 = 720
    hours24 = 1440

    def getMinutes(time, amOrPm):
        arr = time.split(":")
        hours = arr[0]
        minutes = arr[1]
        res = 0
        if amOrPm == "pm":
            res = int(hours) * 60 + hours12 + int(minutes)
        if amOrPm == "am":
            res = int(hours) * 60 + int(minutes)
        return res

    min1 = getMinutes(*time1)
    min2 = getMinutes(*time2)

    if min2 > min1:
        return min2 - min1
    elif min1 > min2:
        return hours24 - min1 + min2

