"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

phoneNumbers = set()

for number in texts:
    phoneNumbers.add(number[0])
    phoneNumbers.add(number[1])

for number in calls:
    phoneNumbers.add(number[0])
    phoneNumbers.add(number[1])

print("There are {} different telephone numbers in the records.".format(len(phoneNumbers)))
