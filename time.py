import time
import datetime


def seconds_countdown(x):
    now = int(time.strftime("%s"))
    countdown = int(input("How many seconds would you like to count?\n"))
    while True:
        near = int(time.strftime("%s"))
        if countdown > 0:
            print(countdown)
            time.sleep(1)
            countdown -= 1
        else:
            break
'''
print(time.ctime(), ' This is the time.ctime() function')
print(time.localtime(), 'This is the .localtime() function')
print(time.gmtime(), 'This is .gmtime() ')
print(time.asctime(), 'This is .asctime() ')
print(time.time(), 'This is .time() ')
'''
def delta_time(x):
    now = time.time()
    time.sleep(x)
    later = time.time()
    print('This program ended in ', later - now, ' seconds')


def convert_input_to_time_value(x):
    input_time = input("When would you like this program to finish?\n")
    int_time = time.strptime(input_time, '%Y %m %d %H %M %S')
    now = time.time()
    time_until = int(round(time.mktime(int_time) - now))
    print('You\'ve got %f seconds remaining ' % time_until)

convert_input_to_time_value(1)
