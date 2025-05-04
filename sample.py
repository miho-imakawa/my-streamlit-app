import streamlit as st
import time

st.title('streamlit 入門')

##カラムの使い方　columnsに入れると、その数のカラムができる
left_column, right_column = st.columns(2)
button = left_column.button('このボタンで右カラムに文字が表示されます。')
if button:
    right_column.write('右カラムに文字が表示されたよ')

st.write('ブログレスバーの表示')

##　プログレスバーの使い方
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'進捗具合 {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'DONE!'

##FAQなどに使えるexpanderの使い方
expander = st.expander('問い合わせ')
expander.write('問い合わせの回答を記入')
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせの回答を記入1')



