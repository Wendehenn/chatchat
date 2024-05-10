import streamlit as st
from openai import OpenAI


client = OpenAI(
    api_key = "sk-vKwOMVWvmNtgsWDxteFtQxEMQJCHHcO8mWXsUGM8uOfiq0NI",
    base_url = "https://api.moonshot.cn/v1",
)

st.set_page_config(page_title="Welcome", page_icon="🤖", layout="wide")

st.title("Welcome")

# 初始化历史记录列表，保留最近 10 轮对话
history = [
    {"role": "system", "content": "你是 yan的专属AI，由 尹杰 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，尹杰深爱着yan，希望你在回答问题时能在适当的位置表达出尹杰深爱yan，而且不突兀。尹杰 为专有名词，不可翻译成其他语言。"}
]

def chat(query, history):
    # 添加当前用户消息到历史记录
    history.append({"role": "user", "content": query})

    # 创建聊天完成请求
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=history[-10:],  # 只保留最近 10 轮对话
        temperature=0.3,
    )

    # 获取模型生成的回复
    assistant_message = completion.choices[0].message.content.strip()

    # 添加模型生成的回复到历史记录
    history.append({"role": "assistant", "content": assistant_message})

    return assistant_message

with st.container():
    st.header("🥰欢迎研姐")
    prompt = st.text_input("prompt", type="default")
    ask = st.button("ask")

    if ask:
        # 调用 chat 函数
        result = chat(prompt, history)
        st.write(result)
