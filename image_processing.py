import cv2
import numpy as np
import os
import sys

def picture_in_picture(background, picture, index):
  padding_top = 50
  padding_left = 237
  picture_size = 150
  interval_h = 25
  interval_w = 50

  bh,bw = background.shape[:2]
  ph,pw = background.shape[:2]
  
  # resize
  if bh != 600 or bw != 1024:
    background = cv2.resize(background, (1024, 600))
  if ph != picture_size or pw != picture_size:
    picture = cv2.resize(picture, (picture_size, picture_size))

  # culculate where the image put
  pip_h = padding_top + index % 3 * (picture_size + interval_h)
  pip_w = padding_left + int(index / 3) * (picture_size + interval_w)

  # Synthesis
  background[pip_h:pip_h+picture_size,pip_w:pip_w+picture_size] = picture
  return background

def create_image(services):
  # Load Background Image
  background = cv2.imread(r'img/background.png', 1)  # '1' read as color image
  h,w = background.shape[:2]
  print('image height and width = %d x %d' % (h, w))
  
  index = 0
  for service_list in services:
    for service in service_list:
      logo_path = "img/icons/" + service["name"] + ".png"
      if not os.path.exists(logo_path):
        print("Icon File(" + service["name"] + ") not exists. exit")
        sys.exit()
      logo = cv2.imread(logo_path, 1)
      background = picture_in_picture(background, logo , index)
      index += 1
  return background
