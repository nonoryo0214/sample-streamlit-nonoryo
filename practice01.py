import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('streamlit 超入門')

st.write('Interactive Widgets')


left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ボタンを押しましたね！')

expander = st.beta_expander('問い合わせ1')
expander.write('問い合わせ回答1')
expander = st.beta_expander('問い合わせ2')
expander.write('問い合わせ回答2')
expander = st.beta_expander('問い合わせ3')
expander.write('問い合わせ回答3')

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# text = st.text_input('あなたの趣味を教えてください')

# 'コンディション：', condition
# 'あなたの趣味：', text

option = st.selectbox(
  'あなたが好きな数字を教えてください！',
  list(range(1,11))
)
'あなたの好きな数字は、', option, 'です。'


if st.checkbox('Show Image'):
  img = Image.open('sample.jpg')
  st.image(img, caption='Oozeki', use_column_width=True)




# df = pd.DataFrame({
#   'A': [1, 2, 3, 4],
#   'B': [10, 20, 30, 40]
# })

# # st.dataframe(df.style.highlight_max(axis=0), width=1000, height=200)

# # st.table(df.style.highlight_max(axis=0))

# # """
# # # 章
# # ## 節
# # ```python
# # import streamlit as st
# # import pandas as pd
# # import numpy as np
# # ```
# # """

# df = pd.DataFrame(
#   np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#   columns = ['lat', 'lon']
# )
# df

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# st.map(df)




