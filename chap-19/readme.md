## Practice Questions
### 1. What is an RGBA value?
```
An RGBA value is a tuple of 4 integers, each ranging from 0 to 255. The four integers correspond to the amount of red, green, blue, and alpha (transparency) in the color.
```
### 2. How can you get the RGBA value of 'CornflowerBlue' from the Pillow module?
```python
ImageColor.getcolor('CornflowerBlue', 'RGBA')
```
### 3. What is a box tuple?
```
It is a tuple of four integers the left-edge x-coordinate, the top-edge y-coordinate, the width, and the height.
```
### 4. What function returns an Image object for, say, an image file named zophie.png?
```python
Image.open('zophie.png')
```
### 5. How can you find out the width and height of an Image object’s image?
```python
imageObj.size
```
### 6. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?
```python
imageObj.crop((0, 50, 50, 50))
```
### 7. After making changes to an Image object, how could you save it as an image file?
```python
imageObj.save('new_filename.png')
```
### 8. What module contains Pillow’s shape-drawing code?
```
ImageDraw module
```
### 9. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?
```
ImageDraw objects have shape-drawing methods such as point(), line(), or rectangle(). They are returned by passing the Image object to the ImageDraw.Draw() function.

```