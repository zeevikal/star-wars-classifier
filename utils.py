import os
import glob
from PIL import Image


def remove_broken_images():
    valid_formats = ['JPEG', 'PNG']
    for filename in glob.glob('images/*/*'):
        try:
            img = Image.open('{0}'.format(filename))
            img.verify()
            if img.format not in valid_formats:
                print('wrong image format:{0}'.format(filename))
                os.remove(filename)
        except(IOError, SyntaxError)as e:
            print('broken image:{0}'.format(filename))
            os.remove(filename)


if __name__ == '__main__':
    remove_broken_images()
