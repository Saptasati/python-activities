import time
second = input("Enter the number of seconds: ")
def count_down(second):
    while second>0:
        mins = int(second/60)
        secs = int(second%60)
        timer = f'{mins}:{secs}'
        print(timer, end='\r')
        time.sleep(1)
        second = second-1
    print("Time is up !!!")

count_down(int(second))    