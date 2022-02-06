from fileinput import filename
import os
import time
from PIL import Image

def image_resize(image, width):
    image_width, image_height = image.size   
    image_resize = image.resize((width, int(image_height * width / image_width)), Image.ANTIALIAS)
    if image_resize.mode != "RGB":
        image_resize = image_resize.convert("RGB")
    try:
        image_resize.save(str(width) + "__" + image.filename + '.jpg', optimize=True)
        print('Resized ' + image.filename + ' successfully')
        image.close()
        os.remove(image.filename)
    except Exception as e:
        print('Error: ' + str(e))

def main():
    width_size = 1024
    supported_file_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']  
    while True:
        time.sleep(1)
        for file in os.listdir('.'):
            file_name, file_extensions = os.path.splitext(file)
            if file_extensions.lower() in supported_file_extensions and file_name.find('__') == -1:
                try:
                    image = Image.open(file_name + file_extensions)
                except Exception as e:
                    print('Error: ' + str(e))
                    os.rename(file_name + file_extensions, '__' + file_name + file_extensions)
                    continue

                image_resize(image, width_size)


if __name__ == '__main__':
    main()
    
