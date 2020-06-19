"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
The call data (call.csv) has the following columns: 
1: calling telephone number (string), 
2: receiving telephone number (string),
3: start timestamp of telephone call (string),
4: duration of telephone call in seconds (string)
"""


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

dictionary = {}

def isDateTrue(date):
    if date[3:10] == '09-2016':
        return True
    return False

for info in calls:
    caller = info[0]
    reciever = info[1]
    date = info[2].split(' ')[0]
    duration = info[3]
    if isDateTrue(date):
        dictionary[caller] = dictionary.get(caller, 0) + int(duration)
        dictionary[reciever] = dictionary.get(reciever, 0) + int(duration)

phoneMax = max(dictionary.items(), key=lambda x: int(x[1]))
print(f"{phoneMax[0]} spent the longest time, {phoneMax[1]} seconds, on the phone during September 2016.")
