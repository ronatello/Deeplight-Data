from os import listdir
from os.path import isfile, join
from PIL import Image 
import PIL
import os
  
# creating a image object (main image)
subfolders = [ f.path for f in os.scandir('D:/is/data/') if f.is_dir() ]
for sub in subfolders:
	onlyfiles = [f for f in listdir(sub) if isfile(join(sub, f))]
	for f in onlyfiles:
		im1 = Image.open(sub + '/' + f)
		# rotating a image 90 deg counter clockwise 
		im1 = im1.rotate(270, PIL.Image.NEAREST, expand = 1) 
		im1.save(sub + '/' + f)