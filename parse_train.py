import os
from bs4 import BeautifulSoup
from PIL import Image

if __name__ == '__main__':
  signature_counter = 0
  file_counter = 0

  dir_path = './data/train_xml/'
  files = os.listdir(dir_path)
  for file_name in files[:5]:
    # print(file_name)
    with open(dir_path + file_name, 'r') as file:
      content = file.read()
      bs_content = BeautifulSoup(content, 'lxml')
      query = bs_content.find_all("dl_zone", {"gedi_type": "DLSignature"})
      for result in query:
        x_min = int(result['col'])
        x_max = x_min + int(result['width'])
        y_min = int(result['row'])
        y_max = y_min+ int(result['height'])
        print(f"{x_min}, {y_min}, {x_max}, {y_max}")
        im = Image.open('data/train/'+file_name[:-4] + '.tif')
        im_crop = im.crop((x_min, y_min, x_max, y_max))
        im_crop.show()

  
