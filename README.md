# Autoresizer Images

This code is a script to resize the images in the current directory. The script will execute infinitely in a loop and wait 1 second between iterations. On each iteration of the loop it goes through all the files in the current directory, opens the file if it is an image, and resizes it with image_resize().

The image_resize() function takes two arguments: image and width. It first calculates a new image height preserving the aspect ratio, and then resizes the image with the resize() function of the PIL library. If the color model of the image is not "RGB", the image is converted to that color model. The script then tries to save the new image with a new name consisting of the width of the image and the name of the original file, and closes the original image. If the new image is saved successfully, the original file is deleted.

The default image width is 1024 pixels, but it can be changed if an integer number is specified in the script file name. For example, if the script is named "resize_images_512.py", the width of the images will be 512 pixels.

The script uses the list_of_blocked_files to store the names of files that should not be processed. The name of the script and the names of files that failed to be processed are added to this list. This is to prevent the script from trying to process the same files repeatedly.

## Instructions
1. Create a folder for images
2. Download autoresizer.exe to this folder and run
3. All existing and new files will be resized 

## Formats
The following image formats are supported: jpg, png, bmp, webp

## Demo

![](https://github.com/akeelow/Autoresizer/blob/main/img/demo.gif)

## Build to EXE

`pyinstaller --noconfirm --onefile --console --icon "img/icon.ico" --name "autoresizer"  "autoresizer.py"`
