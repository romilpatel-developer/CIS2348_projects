# Name-Romilkumar Patel
# PSID- 1765483
# Section- 8.10


user_input = input()
normal = ""
reverse = ""
for ch in user_input.lower():
    if ch != ' ':
        normal += ch
        reverse = ch + reverse
if normal == reverse:
    print(user_input + " is a palindrome")
else:
    print(user_input + " is not a palindrome")