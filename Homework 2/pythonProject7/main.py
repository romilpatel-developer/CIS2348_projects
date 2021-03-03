# Name- Romilkumar Patel
# PSID- 1765483
# Section 6.22


a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

solution_found = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            solution_found = True

if not solution_found:
    print("No solution")