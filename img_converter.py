import sys
import glob
import os
import imghdr
from PIL import Image

argv = sys.argv
img_types = [ 'rgb', 
              'gif', 
              'pbm', 
              'pgm', 
              'ppm', 
              'tif', 
              'tiff', 
              'rast', 
              'xbm',
              'jpg',
              'jpeg',
              'bmp',
              'png' ]

data_dir = os.getcwd() + '/data/'
output_dir = os.getcwd() + '/output/'
output_type = 'jpg'

for i in range(1, len(argv), 2):
  if argv[i] == '--data_dir':
    if os.path.isdir(argv[i + 1]):
      data_dir = argv[i + 1]
      continue
    else:
      raise AttributeError()
  if argv[i] == '--output_dir':
    if os.path.isdir(argv[i + 1]):
      output_dir = argv[i + 1]
      if data_dir == output_dir:
        raise AttributeError()
      continue
    else:
      raise AttributeError()
  if argv[i] == '--output_type':
    if argv[i + 1] in img_types:
      output_type = argv[i + 1]
      continue
    raise AttributeError
  raise AttributeError()

#if (len(argv) == 2) and (argv[-1] == '--help'):

images = []
for type in img_types:
  images += glob.glob(data_dir + '*.' + type)

for filepath in images:
  img = Image.open(filepath)
  img.save(output_dir + os.path.split(filepath)[-1] + '.' + output_type)

print('Work is successfully done!')
print('Data files\' directory: ' + data_dir)
print('Output files\' directory: ' + output_dir)
