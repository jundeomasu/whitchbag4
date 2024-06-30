import streamlit as st


st.title("商品提案アプリ")
st.caption("お客様の目的に最適なバッグを提案します")
st.caption("左の1～5の目的を選択してください")
img ="top.jpg"

#input

options=["0.はじめる","1.学校やおけいこに","2.オフィスに","3.デートに","4.着物をきるとき","5.海外旅行に"] 
sample_select = st.sidebar.selectbox(
    '目的を選んでね！', options)


if sample_select == "0.はじめる":
    sentence = "はじめる"
    img = "start.jpg"
elif sample_select == "1.学校やおけいこに":
    sentence = "アクティブトート"
    img = "school.jpg"
elif sample_select == "2.オフィスに":
    sentence = "アクティブトートネイビー"
    img = "office.jpg"
elif sample_select == "3.デートに":
    sentence = "マシュマロトート"
    img = "date.jpg"
elif sample_select == "4.着物をきるとき":
    sentence = "ハンドバッグ"
    img = "kimono.jpg"
elif sample_select == "5.海外旅行に":
    sentence = "パスポートショルダー"
    img = "travel.jpg"
else:
    sentence = "画像が見つかりません"
    img = "no.jpg"


# output
st.text(sentence)
st.image(img, caption='sample', use_column_width=True)






