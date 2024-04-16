import streamlit as st
from openai import OpenAI

f = open('.openai_apikey.txt')
key = f.read()

client = OpenAI(api_key=key)

st.title('🤖CodeBot - The AI Code Reviewer')

prompt = st.text_area(label='Enter code to review.', height=200)

if st.button('Generate') == True :
    response = client.chat.completions.create(
                    model="gpt-3.5-turbo-16k",
                    messages=[
                            {"role": "system", "content": "You are a Code Reviewer. You help in reviewing code and providing input."},
                            {"role": "user", "content": prompt}
                        ]
    )   
    st.write(response.choices[0].message.content)