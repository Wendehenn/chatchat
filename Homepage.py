import streamlit as st
from openai import OpenAI
import openai
import time

client = OpenAI(
    api_key="sk-vKwOMVWvmNtgsWDxteFtQxEMQJCHHcO8mWXsUGM8uOfiq0NI",
    base_url="https://api.moonshot.cn/v1",
)

st.set_page_config(page_title="Welcome", page_icon="🤖", layout="wide")
st.title("Welcome")

# 使用 st.session_state 来初始化和保存聊天历史记录
if 'history' not in st.session_state:
    st.session_state.history = [
        {"role": "system", "content": "你是 yan的专属AI，由 尹杰 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，尹杰深爱着yan，希望你在回答问题时能在适当的位置表达出尹杰深爱yan，他们在一起快两年了。你正在交流的用户就是yan。"}
    ]

def chat(query):
    try:
        # 添加当前用户消息到历史记录
        st.session_state.history.append({"role": "user", "content": query})

        # 创建聊天完成请求
        completion = client.chat.completions.create(
            model="moonshot-v1-8k",  # 确保使用正确的模型名
            messages=st.session_state.history[-10:],  # 只保留最近 10 轮对话
            temperature=0.3
        )

        # 获取模型生成的回复
        assistant_message = completion.choices[0].message.content.strip()

        # 添加模型生成的回复到历史记录
        st.session_state.history.append({"role": "assistant", "content": assistant_message})

        return assistant_message
    except openai.Error as e:
        # 捕获来自OpenAI的所有API错误
        if 'rate limit' in str(e):
            wait_time = 1  # 根据API错误消息设定合适的等待时间
            st.error(f"请求过于频繁，请等待 {wait_time} 秒后再试。")
            time.sleep(wait_time)  # 等待一定时间
            return "请重新提交您的请求。"
        else:
            st.error("发生了一个错误: " + str(e))
            return "出现了一个错误，请稍后再试。"

# 使用 CSS 将输入框固定在底部
st.markdown(
    """
    <style>
        .stTextInput {
            position: fixed;
            bottom: 50px;
            left: 50px;
            width: calc(100% - 100px);
            z-index: 999;
        }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.header("🥰欢迎研姐")

    # 显示所有历史记录
    for result in st.session_state.history:
        if result["role"] == "user":
            with st.chat_message("user"):
                st.markdown(result["content"])
        elif result["role"] == "assistant":
            with st.chat_message("assistant"):
                st.markdown(result["content"])

# 获取用户输入
prompt = st.chat_input("我啥都知道，但是不会画图。。。")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 显示加载提示
    with st.spinner('正在处理，请稍候...'):
        result = chat(prompt)
    
    # 加载完毕后，显示助手的回复
    with st.chat_message("assistant"):
        st.markdown(result)

