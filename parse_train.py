import os
from bs4 import BeautifulSoup
import cv2
import numpy as np

if __name__ == '__main__':
  IMAGE_SIZE = 128

  dir_path = './data/train_xml/'
  files = os.listdir(dir_path)
  img_list = []
  label_list = []
  for file_name in files:
    with open(dir_path + file_name, 'r') as file:
      content = file.read()
      bs_content = BeautifulSoup(content, 'lxml')
      query = bs_content.find_all("dl_zone", {"gedi_type": "DLSignature"})
      img = cv2.imread('data/train/'+file_name[:-4] + '.tif', cv2.IMREAD_GRAYSCALE)
      cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
      img_list.append(img)
      label_list.append(1 if query else 0)
      # for result in query:
      #   # Get Signature boundaries
      #   x_min = int(result['col'])
      #   x_max = x_min + int(result['width'])
      #   y_min = int(result['row'])
      #   y_max = y_min+ int(result['height'])
      #   # Crop img
      #   sig = img[y_min:y_max, x_min:x_max]
      #   sig = cv2.resize(sig, (IMAGE_SIZE, IMAGE_SIZE))
      #   cv2.imshow("signature", sig)
      #   cv2.waitKey(0)

  label_array = np.array(label_list)
  img_array = np.array(img_list)
  np.save('img.npy', img_array, allow_pickle=True)
  np.save('label.npy', label_array, allow_pickle=True)

  
