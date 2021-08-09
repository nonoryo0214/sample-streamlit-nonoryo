import streamlit as st
import requests
import json
from PIL import Image
from PIL import ImageDraw, ImageFont
import io

st.title('顔認識アプリ')

SUBSCRIPTION_KEY = 'a78dd3dac287419b9da9926c974909e3'
assert SUBSCRIPTION_KEY

face_api_url = 'https://20210808-youtube.cognitiveservices.azure.com/face/v1.0/detect'

uploaded_file = st.file_uploader('Choose an image...', type='jpg')
if uploaded_file is not None:
  img = Image.open(uploaded_file)
########################################################################
  with io.BytesIO() as output:
    img.save(output, format='JPEG')
    binary_img = output.getvalue() #バイナリ取得

# with open('sample_04.jpg', 'rb') as f:
#   binary_img = f.read()

  headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

  params = {
    'returnFaceId': 'true',
    'returnFaceAttributes':'age,gender,blur,exposure,noise,facialhair,glasses,hair,makeup,accessories,occlusion,headpose,emotion,smile',
  }

  res = requests.post(face_api_url, params=params, headers=headers, data=binary_img)

  results = res.json()

  for result in results:
    rect = result['faceRectangle']
    age = result['faceAttributes']['age']
    gender = result['faceAttributes']['gender']

  # # よくわからない。。。
    # textsize = 20
    # font = ImageFont.truetype("arial.ttf", size=textsize)

    draw = ImageDraw.Draw(img)
    draw.rectangle([(rect['left'], rect['top']),(rect['left']+rect['width'],rect['top']+rect['height'])], fill=None, outline='blue', width=3)

    draw.text((rect['left'], rect['top']-10), f'{age},{gender}', fill='blue')
########################################################################
  st.image(img, caption='Uploaded Image...', use_column_width=True)

