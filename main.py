import tensorflow as tf
import os

from parse_train import get_train_data
from model import build_model
from preprocess import preprocess_test_data

if __name__ == "__main__":
    """
      Run model without any user interface
    """
    x, y = get_train_data()
    try:
        model = tf.keras.models.load_model('model/sigDetection.h5')
    except:
        model = build_model(x, y)
        model.save("model/sigDetection.h5")
    y_pred = model.predict(x)
    cm = tf.math.confusion_matrix(y, y_pred)
    print(cm)
    dir_path = './data/test/'
    files = os.listdir(dir_path)
    test_array = preprocess_test_data()
    results = model.predict(test_array)
    with open("results.csv", "a") as file:
      file.write("Id,Expected\n")
      for data in zip(files, results):
        file.write(f'{data[0][:-4]},{round(data[1][0])}\n')