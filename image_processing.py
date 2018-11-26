import cv2
import numpy as np
import os
import sys
import boto3

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
  #cv2.imwrite("tmp/image.png", background)
  return background

def draw_line(image, line_num, color):
  if line_num == 0:
    sp = (230, 125)
    ep = (794, 125)
  elif line_num == 1:
    sp = (230, 300)
    ep = (794, 300)
  elif line_num == 2:
    sp = (230, 475)
    ep = (794, 475)
  elif line_num == 3:
    sp = (237, 550)
    ep = (751, 50)
  elif line_num == 4:
    sp = (273, 50)
    ep = (751, 550)

  image_path = "tmp/image.png"
  cv2.line(image, sp, ep, color, thickness=3)
  cv2.imwrite(image_path, image)
  return image_path
  
def upload_s3(image_path):
  bucket_name = "reinventalexajap"
  s3 = boto3.resource('s3')
  s3.Bucket(bucket_name).upload_file('tmp/image.png', 'result.png')
