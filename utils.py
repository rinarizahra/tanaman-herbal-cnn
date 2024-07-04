import os
from keras.utils import load_img,img_to_array
import numpy as np
from tensorflow import keras
from keras.models import load_model
import pandas as pd
import os

target_names = ['Daun Jambu Biji','Daun Kari','Daun Kemangi','Daun Kunyit','Daun Mint','Daun Pepaya','Daun Sirih','Daun Sirsak','Lidah Buaya','Teh Hijau']

df_manfaat = pd.read_excel("Pemanfaatan tanaman herbal.xlsx")
df_manfaat.index = [i for i in range(1,len(df_manfaat)+1)]

df_pengolahan = pd.read_excel("Pengolahan tanaman herbal.xlsx")
df_pengolahan.index = [i for i in range(1,len(df_pengolahan)+1)]

df_sumber = pd.read_excel("Sumber tanaman herbal.xlsx")
df_sumber.index = [i for i in range(1,len(df_sumber)+1)]

example_names = [i.split('.')[0] for i in os.listdir("contoh_tanaman_herbal") ]
model = load_model('Tanaman_Herbal.h5')
def predict(image):
    img = image.resize((224,224))

    x = img_to_array(img)
    X = x
    x /= 255
    x = np.expand_dims(x, axis=0)
    x = np.vstack([x])

    pred = np.argmax(model.predict(x),axis=1)
    return target_names[pred[0]]
    

