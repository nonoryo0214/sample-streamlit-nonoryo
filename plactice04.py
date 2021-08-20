import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title('インタラクティブな機能')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration{i+1}')
  bar.progress(i + 1)
  time.sleep(0.01)

'Done!!'


left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムへ文字を表示')
if button:
  right_column.write('左のボタンが押されました！')

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
text = st.sidebar.text_input('あなたの趣味を教えてください。')

f'コンディション：{condition}'
f'あなたの趣味は、{text}です！'

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1に対する回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2に対する回答')

option = st.selectbox(
  'あなたが好きな数字を教えてください。',
  list(range(1,11))
)
f'あなたの好きな数字は、{option}です！'

# if st.checkbox('Show Image'):
#   img = Image.open('sample_05.jpg')
#   st.image(img, caption='samurai', use_column_width=True)