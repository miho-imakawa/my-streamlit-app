import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title('streamlit 入門')

st.write('ブログレスバーの表示')

##　プログレスバーの使い方
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'DONE!'

##FAQなどに使えるexpanderの使い方
expander = st.expander('問い合わせ')
expander.write('問い合わせの回答を記入')
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせの回答を記入1')

##カラムの使い方　columnsに入れると、その数のカラムができる
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右カラムに文字を表示')

##サイドバーの追加

#st.sidebar.write('Interactive Widgets')

## スライダーの使い方 sidebar
#condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
#テキストボックスの使い方
#text = st.sidebar.text_input('あなたの趣味は？')
#セレクトボックスの使い方
#option = st.sidebar.selectbox(
#    'あなたが好きな数字を教えてください',
#    list(range(1, 11))
#)


#'コンディション', condition 
#'あなたの趣味は、', text, 'です。'
#'あなたの好きな数字は、', option, 'です。'

#if st.checkbox('Show Image'):
#    img = Image.open('IMG_20210410_175248.jpg')
#    st.image(img, caption='Mashimaro', use_column_width=True)

#st.write('DataFrame')

#df = pd.DataFrame({
#    '1st column': [1, 2, 3, 4],
#    '2nd column': [10, 20, 30, 40]  
#})

#st.dataframe(df, width=300, height=300)
#st.write(df, width=200, height=200)
#st.dataframe(df.style.highlight_max(axis=0))

#テーブルだと、幅と高さの指定はできない例
#st.table(df)

#折れ線グラフのチャート
#df = pd.DataFrame(
#    np.random.rand(20, 3),
#    columns=['a', 'b', 'c']
#)
#st.line_chart(df)

# マップに表示するためのデータフレームを作成
#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns=['lat', 'lon']
#)
#st.map(df)



"""
# 章
## 節
### 項目 

'''python
import streamlit as st
import pandas as pd
import numpy as np
'''

"""
