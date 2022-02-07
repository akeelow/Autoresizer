from fileinput import filename
import os
import time
from PIL import Image

list_of_blocked_files = ['autoresizer.py', 'autoresizer.exe']
width_size = 1024

def image_resize(image, width):
    image_width, image_height = image.size   
    image_resize = image.resize((width, int(image_height * width / image_width)), Image.ANTIALIAS)
    if image_resize.mode != "RGB":
        image_resize = image_resize.convert("RGB")
    try:
        new_file_name = f"{str(width)}__{image.filename.split('.')[0]}.jpg"
        image_resize.save(new_file_name, optimize=True)
        print(f"{image.filename} → resized successfully")
        image.close()
        list_of_blocked_files.append(new_file_name)
        os.remove(image.filename)
    except Exception as e:
        print(f"Error: {str(e)}")



def main():
    while True:
        time.sleep(1)
        for file in os.listdir('.'):
            try:
                if file not in list_of_blocked_files:
                    image = Image.open(file)
                    image_resize(image, width_size)
            except Exception as e:
                print(f"Error: {str(e)}")
                list_of_blocked_files.append(file)



if __name__ == '__main__':
    main()
    
