#Name-Romilkumar Patel
# PSID-1765483
# Section 6.17

password = input()

modified_password = ''

i = 0
while i < len(password):
    ch = password[i]
    if ch == 'i':
        modified_password += '!'
    elif ch == 'a':
        modified_password += '@'
    elif ch == 'm':
        modified_password += 'M'
    elif ch == 'B':
        modified_password += '8'
    elif ch == 'o':
        modified_password += '.'
    else:
        modified_password += ch
    i += 1

modified_password += "q*s"

print(modified_password)