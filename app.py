from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
nvidia_api_key= os.getenv("NVIDIA_API_KEY")


st.title("MiniBot Chatter")

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = nvidia_api_key
)

def chatter(user_input):
    completion = client.chat.completions.create(
    model="meta/llama-3.1-405b-instruct",
    messages=[{
        "role":"user",
        "content":user_input}],
    temperature=0.7,
    top_p=0.7,
    max_tokens=100,
    stream=False)
    return completion.choices[0].message.content

query = st.text_input("Enter your question")

if st.button("Ask Me"):
    if query:
        output = chatter(query)
        st.write("You:", query)
        st.write("miniBot:", output)



