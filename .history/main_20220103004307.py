import streamlit as st
import numpy as np
import pandas as pd 
from PIL import Image
import time

st.title('Streamilt 超入門まとめ')

left_column, right_column = st.columns(2)
button = left_column.button('右に文字を出すよ')
if button:
     right_column.write('ここは右カラム')


text = st.text_input('あなたの趣味を教えてください。')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'あなたの趣味：', text
'コンディション：', condition

expander = st.expander('問い合わせフォーム')
expander.write('ここに書いてもらう')

"""
# 使っているライブラリ

```python
import streamlit as st
import numpy as np
import pandas as pd 
from PIL import Image
import time
```


## プログレスバーの表示
"""

'何の写真が出るでしょう？'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
          latest_iteration.text(f'Iteration {i+1}')
          bar.progress(i+1)
          time.sleep(0.1)

'Done!!!'

"""
### 写真の埋め込み
"""

img = Image.open('picture.jpeg')
st.image(img, caption='Syuriken dojo', use_column_width=True)




