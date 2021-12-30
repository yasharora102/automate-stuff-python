## Practice Questions
### 1. How can you trigger PyAutoGUI’s fail-safe to stop a program?
```
Move the mouse to the upper-left corner of the screen, that is, the (0, 0) coordinates.
```
### 2. What function returns the current resolution()?
```python
pyautogui.size()
```
### 3. What function returns the coordinates for the mouse cursor’s current position?
```python
pyautogui.position() 
```
### 4. What is the difference between pyautogui.moveTo() and pyautogui.move()?
```
moveto() moves to absolute coordinates of the screen and move() to the relative position of the mouse.
```
### 5. What functions can be used to drag the mouse?
```python
pyautogui.dragTo()
pyautogui.drag()
```
### 6. What function call will type out the characters of "Hello, world!"?
```python
pyautogui.typewrite('Hello, world!')
```
### 7. How can you do keypresses for special keys such as the keyboard’s left arrow key?
```python
pyautogui.press('left')
```
### 8. How can you save the current contents of the screen to an image file named screenshot.png?
```python
pyautogui.screenshot('screenshot.png')
```
### 9. What code would set a two-second pause after every PyAutoGUI function call?
```python
pyautogui.PAUSE = 2
```
### 10. If you want to automate clicks and keystrokes inside a web browser, should you use PyAutoGUI or Selenium?
```
Selenium
```
### 11. What makes PyAutoGUI error-prone?
```
It clicks and types blindly and we cannot easily find out if it’s clicking and typing into the correct windows.
```
### 12. How can you find the size of every window on the screen that includes the text Notepad in its title?
```python
pyautogui.getWindowsWithTitle('Notepad')
```
### 13. How can you make, say, the Firefox browser active and in front of every other window on the screen?
```python
w = pyatuogui.getWindowsWithTitle('Firefox')
w.activate()
```
