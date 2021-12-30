import time,pyperclip

print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()                    
print('Started.')
startTime = time.time()    
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (str(lapNum).rjust(3), str(totalTime).rjust(5), str(lapTime).rjust(6)), end='')
        pyperclip.copy('Lap #%s: %s (%s)' % (str(lapNum).rjust(3), str(totalTime).rjust(5), str(lapTime).rjust(6)))
        lapNum += 1
        lastTime = time.time()

except KeyboardInterrupt:
    print('\nDone.')