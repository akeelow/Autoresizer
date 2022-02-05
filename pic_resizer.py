import os
import time
from PIL import Image

def resize_image(image_path, width_size):
    try:
        image = Image.open(image_path)
        width_percent = (width_size / float(image.size[0])) 
        height_size = int((float(image.size[1]) * float(width_percent)))
        new_image = image.resize((width_size, height_size))
        new_image.save(f'{width_size}__{image_path}', optimize=True, quality=60)
        print(f'{width_size}__{image_path} resized to {width_size}x{height_size} successfully')
        os.remove(image_path)
    except Exception as e:
        try:
            os.rename(image_path, f'ERROR__{image_path}')
        finally:
            print(f'ERROR__{image_path}')

def main():
    print("\033[4m\033[37m\033[44m{}\033[0m".format("Python 3"))
    width_size = 1024
    while True:
        time.sleep(0.1)
        for filename in os.listdir('.'):
            if filename.endswith('.jpeg') or filename.endswith('.jpg') or filename.endswith('.png'):
                if filename.startswith(str(width_size)) == False and filename.startswith('ERROR') == False:
                    resize_image(filename, width_size)


if __name__ == '__main__':
    main()
    

