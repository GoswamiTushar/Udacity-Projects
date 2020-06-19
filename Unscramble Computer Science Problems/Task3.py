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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)
Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.
Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?
Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def classifyNumber(phoneNum):
    phoneNumType = None
    areaCode = None
    prefix = None

    startNums = ("7", "8", "9")
    TelemarketerAreaCode = "140"

    if(phoneNum.startswith("(0")):
        phoneNumType = "Fixed"
        areaCode = phoneNum[1:phoneNum.find(")")]
    elif(phoneNum.find(" ") == 5 and phoneNum.startswith(startNums)):
        phoneNumType = "Mobile"
        prefix = phoneNum[0:4]
    elif (phoneNum.startswith(TelemarketerAreaCode)):
        phoneNumType = "Telemarketer"
        areaCode = TelemarketerAreaCode

    return {"phoneNumType": phoneNumType, "areaCode": areaCode, "prefix": prefix}


# ------------------------------------------------------
callsMadeFromBangalore = []
bangaloreAreaCode = "(080)"


"""
Part A: 
"""
phoneNumberCodes = []

for record in calls:
    # Fixed line numbers phone number of people in Bangalore which starts with (080)
    outgoingNumber = record[0]
    recievingNumber = record[1]

    if(outgoingNumber.startswith(bangaloreAreaCode)):
        callsMadeFromBangalore.append(record)
        numData = classifyNumber(recievingNumber)
        code = numData['areaCode'] if numData['areaCode'] != None else numData['prefix']
        if code not in phoneNumberCodes:
            phoneNumberCodes.append(code)

    """ 
    Find all of the area codes and mobile prefixes called by people in Bangalore.
    The prefix of a mobile number is its first four digits, and they always start with 7, 8 or 9.
    """

    timestamp = record[2]
    callDuration = record[3]


print("The numbers called by people in Bangalore have codes:")
print(*sorted(phoneNumberCodes), sep='\n')

# print(callsMadeFromBangalore)


"""
Part B: 
percentage formula: y/x = P%
What percent of callsMadeFromBangalore is countRecords?
y is countRecords
x is len(callsMadeFromBangalore), 
"""

countRecords = 0
for record in callsMadeFromBangalore:
    recievingNumber = record[1]
    if(recievingNumber.startswith(bangaloreAreaCode)):
        countRecords += 1

y = countRecords
x = len(callsMadeFromBangalore)
p = y/x

# Converting decimal to a percent: p * 100 = ?%
percentage = p * 100
# print(percentage)

print(f"{format(percentage,'.2f')} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
