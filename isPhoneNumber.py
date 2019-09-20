#function that checks the validity of a Nigerian number 

def isPhoneNumber(number):
    if len(number) != 14:
        return False
    for i in range(1,3):
        if not number[i].isdecimal():
            return False
    if number[0] != '+':
        return False
    for i in range(1, 14):
        if not number[i].isdecimal():
            return False
    return True

print('Is this a valid Nigerian phone number? ')
print(isPhoneNumber('+2348023836922')) #call to check

message = 'Call me at +2348023836922 tomorrow. +2349056761516 is my office line.'
for i in range(len(message)):
    chunk = message[i:i+14]
    if isPhoneNumber(chunk):
        print(' Phone number found in message: ' +chunk)

