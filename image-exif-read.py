#!/usr/bin/env python

import exifread

image_name = 'test.jpg'
# Open image file for reading (binary mode)
f = open(image_name, 'rb')

# Return Exif tags
tags = exifread.process_file(f)

from PIL import Image
img = Image.open(image_name)
exif_data = img._getexif()
print 'Done'
