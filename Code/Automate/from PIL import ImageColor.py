# import image file to be manipulated
from PIL import ImageColor

ImageColor.getcolor('red','RGBA')
(255,0,0,255)

import os
import sys

cwd = os.getcwd()
files = os.listdir(cwd)

#print("Files in %r: %s" % (cwd, files))

#os.chdir ('/Users/danielskomorowski/Downloads/automate_online-materials')

#retreval = os.chdir(r'/Users/danielskomorowski/Downloads/automate_online-materials') 

import os

dirctory = os.getcwd()
print(f"Current directory: Before= {'/Users/danielskomorowski/Downloads/automate_online-materials'}")

path = '/Users/danielskomorowski/Downloads/automate_online-materials'

os.chdir(path)

dirctory = os.getcwd()

print(f"Current working directory: After= {dirctory}")

from PIL import Image

cat_image = Image.open('/Users/danielskomorowski/Downloads/automate_online-materials/zophie.png')
print(cat_image)

cat_image.size 
print(cat_image.size)

cat_image.save('/Users/danielskomorowski/Downloads/automate_online-materials/zophie.jpeg')

image = Image.new('RGBA',(100,200), 'purple')
image.save('purple_image.png')