import os
import cv2
import numpy as np

def preprocess_test_data():
  IMAGE_SIZE = 128

  dir_path = './data/test/'
  files = os.listdir(dir_path)
  test_list = []
  for file_name in files:
    img = cv2.imread(dir_path + file_name, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
    test_list.append(img)
    # for result in query:
    #   # Get Signature boundaries
    #   x_min = int(result['col'])
    #   x_max = x_min + int(result['width'])
    #   y_min = int(result['row'])
    #   y_max = y_min+ int(result['height'])
    #   # Crop img
    #   sig = img[y_min:y_max, x_min:x_max]

  test_array = np.asarray(test_list, dtype=object).astype('float32')
  test_array = test_array.reshape(-1, IMAGE_SIZE, IMAGE_SIZE, 1)
  # np.save('img.npy', img_array, allow_pickle=True)
  # np.save('label.npy', label_array, allow_pickle=True)
  return test_array
  
