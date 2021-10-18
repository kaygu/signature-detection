import os
from bs4 import BeautifulSoup

if __name__ == '__main__':
  signature_counter = 0
  file_counter = 0

  dir_path = './data/train_xml/'
  files = os.listdir(dir_path)
  for file_name in files:
    # print(file_name)
    with open(dir_path + file_name, 'r') as file:
      content = file.read()
      bs_content = BeautifulSoup(content, 'lxml')
      query = bs_content.find_all("dl_zone", {"gedi_type": "DLSignature"})
      if len(query) > 0:
        signature_counter += len(query)
        file_counter += 1
  
  print(f'Signatures found in {file_counter} out of {len(files)} files, with a total of {signature_counter} signatures')