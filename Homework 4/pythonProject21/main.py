# RomilKumar Patel
# 1765483
# Homework 4 (Zybooks lab 12.7)

def get_age():
    age=int(input())
    #checking if age is invalid
    if age<18 or age>75:
        #raising ValueError with message: 'Invalid age.'
        raise ValueError('Invalid age.')
    return age

def fat_burning_heart_rate(age):
    #subtracting age from 220 and finding 70% of it
    heart_rate=(220-age)*.70
    #returning the result
    return heart_rate

if __name__ == '__main__':
    #modified the code to handle exceptions
    try:
        #reading age
        age=get_age()
        #displaying the result if no exception is occurred
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age,fat_burning_heart_rate(age)))
    except ValueError as ve:
        #printing exception messages
        print(ve)
        print('Could not calculate heart rate info.\n')