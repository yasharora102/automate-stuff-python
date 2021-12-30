# Import modules and write comments to describe this program.
import os
from PIL import Image
from pathlib import Path

for foldername, subfolders, filenames in os.walk('/Users/yash'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not (filename.endswith('.jpg') or filename.endswith('.png')) :
            numNonPhotoFiles += 1
            continue
        
        # Open image file using Pillow.
        image_ = Image.open(Path(foldername,filename))
        # Check if width & height are larger than 500.
        w,h = image_.size
        if w>500 and h>500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print(Path(foldername))