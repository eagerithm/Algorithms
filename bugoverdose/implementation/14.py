# The Time in Words (https://www.hackerrank.com/challenges/the-time-in-words/problem)

hour = int(input())
minute = int(input())

numbers = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", 
           "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", 
           "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
           "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", 
           "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]

if minute == 0:
    print(numbers[hour], "o' clock")
elif minute <= 30:
    past = "past"
    if minute == 1:
        past = "minute " + past
    elif minute != 15 and minute != 30:
        past = "minutes " + past    
    print(numbers[minute], past, numbers[hour])
else:
    if hour == 12:
        hour = 0
    to = "to"
    if minute == 59:
        to = "minute " + to
    elif minute != 45:
        to = "minutes " + to    
    print(numbers[60 - minute], to, numbers[hour+1])

#  =================================================================