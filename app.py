import streamlit as st
import json
import random

def read_articles(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def replace(article, keys):
    for i, key in enumerate(keys):
        article = article.replace(f"{{{{{i+1}}}}}", key)
    return article

st.title('填空游戏')

# 文件上传组件，用于上传题库文件
uploaded_file = st.file_uploader("上传题库文件", type="json")
if uploaded_file is not None:
    data = json.loads(uploaded_file.getvalue())

    # 文章选择组件，用于选择文章
    article_index = st.selectbox("选择文章", range(len(data["articles"])))
    article = data["articles"][article_index]
    st.write(f"选择的文章是：{article['title']}")

    # 文本输入组件，用于获取用户的输入
    user_input = st.text_input('请输入填入的词，用逗号分隔')
    keys = user_input.split(',')

    # 按钮组件，用于触发填词操作
    if st.button('开始填词'):
        filled_article = replace(article['article'], keys)
        st.write(f"填词后的文章是：\n{filled_article}")
