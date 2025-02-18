import os
import streamlit as st
import google.generativeai as genai

# โหลดค่า API Key จาก Streamlit Secrets
GEMINI_API_KEY = st.secrets["GENAI_API_KEY"]

# ตรวจสอบว่า API Key ถูกตั้งค่าไว้หรือไม่
if not GEMINI_API_KEY:
    raise ValueError("GENAI_API_KEY is not set in Streamlit secrets.")

# ตั้งค่า Gemini AI API
genai.configure(api_key=GEMINI_API_KEY)

# กำหนดค่าการสร้างข้อความ
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# โหลดโมเดล Gemini
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
)

# เริ่มแชทกับโมเดล
chat_session = model.start_chat(history=[])

# สร้างอินเทอร์เฟซบน Streamlit
st.title("Gemini AI Chatbot")
user_input = st.text_input("พิมพ์ข้อความที่นี่...", "")

if st.button("ส่งข้อความ"):
    if user_input:
        response = chat_session.send_message(user_input)
        st.write("**Gemini:**", response.text)
    else:
        st.warning("กรุณาพิมพ์ข้อความก่อนส่ง")

