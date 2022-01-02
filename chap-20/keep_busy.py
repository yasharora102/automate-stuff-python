import time, pyautogui
a = 1
start = time.time()
t = time.localtime()
current_time = time.strftime("%H:%M:%S, %d/%m/%Y", t)
print('Started at: ',current_time)

try:
    while True:
        pyautogui.moveRel(10, 0, 0.1)
        pyautogui.moveRel(-10, 0, 0.1)
        print('nudged_{}_times'.format(a))
        time.sleep(10)
        a+=1
        pyautogui.FAILSAFE = True
    
except KeyboardInterrupt:
    end_time = time.time()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S, %d/%m/%Y", t)
    print('\nStopped at: ',current_time)
    print("\nRan for: {} seconds".format(round(end_time-start)))

    
