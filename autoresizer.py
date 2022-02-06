from fileinput import filename
import os
import time
from PIL import Image

list_of_blocked_files = []
width_size = 1024

def is_no_blocked(file_name):
    if file_name in list_of_blocked_files:
        return False
    else:
        return True

def image_resize(image, width):
    image_width, image_height = image.size   
    image_resize = image.resize((width, int(image_height * width / image_width)), Image.ANTIALIAS)
    if image_resize.mode != "RGB":
        image_resize = image_resize.convert("RGB")
    try:
        new_file_name = str(width) + "__" + image.filename + '.jpg'
        image_resize.save(new_file_name, optimize=True)
        print('Resized ' + image.filename + ' successfully')
        image.close()
        list_of_blocked_files.append(new_file_name)
        os.remove(image.filename)
    except Exception as e:
        print('Error: ' + str(e))



def main():
    while True:
        time.sleep(1)
        for file in os.listdir('.'):
            try:
                if is_no_blocked(file):
                    image = Image.open(file)
                    image_resize(image, width_size)
            except Exception as e:
                print('Error: ' + str(e))
                list_of_blocked_files.append(file)



if __name__ == '__main__':
    main()
    
