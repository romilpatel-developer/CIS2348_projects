
#Part A

var = 1
months = ['January','February','March','April','May','June',
          'July','August','September','October','November','December']
while var == 1:
  try:
    stri = input("Enter the month day, year: ")
  except SyntaxError:
    continue
  if stri=='-1':
    break

  try:
    arr = stri.split()
    digit = len(arr)
    if digit!=3:
      continue
    m = arr[0]
    day = arr[1]
    y = arr[2]
    d, comma = day.split(',')

    for x in range(12):
      if stri.find(months[x])>=0:
        mo = str(x+1)
        ans = mo + '/' + d + '/' + y
        print(ans)
        break
  except ValueError:
    continue

#Part B

file1 = open('inputDates.txt', 'r')
dates = file1.readlines()

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

for stri in dates:
    if stri == '-1':
        break

    try:
        arr = stri.split()
        digit = len(arr)
        if digit != 3:
            continue
        m = arr[0]
        day = arr[1]
        y = arr[2]
        d, comma = day.split(',')

        for x in range(12):
            if stri.find(months[x]) >= 0:
                mo = str(x + 1)
                ans = mo + '/' + d + '/' + y
                print(ans)
                break
    except ValueError:
        continue

file1.close()

#Part C

file1 = open('inputDates.txt','r')
dates = file1.readlines()

months = ['January','February','March','April','May','June',
          'July','August','September','October','November','December']

count = 0
for stri in dates:
  count++
  if stri=='-1':
    break

  try:
    arr = stri.split()
    digit = len(arr)
    if digit!=3:
      continue
    m = arr[0]
    day = arr[1]
    y = arr[2]
    d, comma = day.split(',')

    for x in range(12):
      if stri.find(months[x])>=0:
        mo = str(x+1)
        ans = mo + '/' + d + '/' + y
        if count>0:
          file2 = open('parsedDates.txt','a')
          file2.write("ans \n")
          file2.close()
        else:
          file3 = open('parsedDates.txt','w')
          file3.write("ans \n")
          file3.close()
        break

  except ValueError:
    continue

file1.close()
