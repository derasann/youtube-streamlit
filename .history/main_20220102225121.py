import streamlit as st
import numpy as np
import pandas as pd 

st.title('Streamilt 超入門')

st.write('DataFrame')

df = pd.DataFrame({
     '１列目':[1,2,3,4],
     '２列目':[10,20,30,40]
})


st.dataframe(df, width=100, height=100)


'Start!!'

latest_iteration = st.empty()
bar = st.progress(10)

for i in range(20):
          latest_iteration.text(f'Iteration {i+1}')
          bar.progress(i+1)
          time.sleep(0.1)

'Done!!!'

#if st.checkbox('Show Image'):
img = Image.open('picture.jpeg')
st.image(img, caption='Ninja', use_column_width=True)


#left_column, right_column = st.beta_columns(2)
#button = left_column.button('右カラムに文字を表示')
#if button:
#    right_column.write('ここは右カラム')

# expander1 = st.beta_expander('問い合わせ')
# expander1.write('問い合わせ1の回答')
# expander2 = st.beta_expander('問い合わせ')
# expander2.write('問い合わせ2の回答')



text = st.text_input('あなたの趣味を教えてください。')
condition = st.slider('あなたの今の調子は？', 0,100,50)

# 'あなたの趣味：', text
# 'コンディション：', condition




