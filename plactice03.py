import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 入門')

st.write('DataFrame')

df = pd.DataFrame({
  '1列目':[1, 2, 3, 4],
  '2列目':[40, 20, 30, 10]
})

# st.dataframe(df.style.highlight_max(axis=0))
st.table(df)

"""
# 章
## 節
### 項

```python
import pandas as pd
import streamlit as st
```
"""

df1 = pd.DataFrame(
  np.random.randn(20, 3),
  columns=['a', 'b', 'c'],
)

st.line_chart(df1)
st.area_chart(df1)
st.bar_chart(df1)

df2 = pd.DataFrame(
  np.random.randn(100, 2)/[5, 5] + [35.69, 139.70],
  columns=['lat', 'lon'],
)

st.map(df2)

picture = 'sample_05.jpg'
img = Image.open(picture)

st.image(img, caption='samurai', use_column_width=True)


