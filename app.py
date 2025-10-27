import streamlit as st
import requests
import random

# === SOZLAMALAR ===
st.set_page_config(page_title="KonstitutsiyaLab AI", page_icon="⚖️")

# 👉 BU YERGA O'Z TOKENINGIZNI JOYLASHTIRING
import streamlit as st
HUGGINGFACE_API_KEY = st.secrets["HUGGINGFACE_API_KEY"]

# === FUNKSIYA: Hugging Face AI javobi ===
def ask_ai(prompt):
    API_URL = "https://api-inference.huggingface.co/models/google/gemma-2b-it"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    data = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        try:
            return result[0]["generated_text"]
        except:
            return "AI javob qaytara olmadi."
    else:
        return f"Xatolik: {response.status_code}"

# === SAHIFA ===
st.title("🇺🇿 KonstitutsiyaLab AI Platforma")
st.write("O‘zbekiston Respublikasining 2023-yilgi Konstitutsiyasi asosida AI yordamida o‘rganish platformasi")

menu = st.sidebar.radio("Bo‘limni tanlang:", ["AI Testlar", "AI Kazuslar", "Muhim ma'lumotlar"])

# === AI TESTLAR ===
if menu == "AI Testlar":
    st.header("🧠 AI tomonidan yaratilgan testlar")
    st.write("Pastga yozing: masalan, *'3 ta test yarat'* yoki *'1-bo‘lim bo‘yicha test yoz'*")
    user_input = st.text_input("Buyruqni kiriting:")
    if st.button("Test yaratish"):
        with st.spinner("AI test tayyorlamoqda..."):
            prompt = f"O‘zbekiston Respublikasi Konstitutsiyasi asosida {user_input}. Har bir testda 3 ta variant va to‘g‘ri javob bo‘lsin."
            answer = ask_ai(prompt)
            st.success("✅ Natija:")
            st.write(answer)

# === AI KAZUSLAR ===
elif menu == "AI Kazuslar":
    st.header("⚖️ AI Kazus generatori")
    st.write("Masalan: *'Sud hokimiyati bo‘yicha kazus yoz'* yoki *'Prezident vakolatiga oid kazus'*")
    case_input = st.text_input("Kazus mavzusini kiriting:")
    if st.button("Kazus yaratish"):
        with st.spinner("AI kazus tayyorlamoqda..."):
            prompt = f"O‘zbekiston Respublikasi Konstitutsiyasi asosida {case_input} mavzusida 1 ta o‘ylantiruvchi huquqiy kazus yoz."
            answer = ask_ai(prompt)
            st.success("✅ Kazus:")
            st.write(answer)

# === MUHIM MA'LUMOTLAR ===
elif menu == "Muhim ma'lumotlar":
    st.header("📘 Muhim Konstitutsiyaviy ma'lumotlar")
    st.markdown("""
    - **Kuchga kirgan sana:** 2023-yil 1-may  
    - **Bo‘limlar soni:** 7 ta  
    - **Moddalar soni:** 155 ta  
    - **Davlat tili:** O‘zbek tili  
    - **Prezident vakolat muddati:** 7 yil  
    - **Xalq hokimiyatining manbai:** Xalq o‘zi  
    """)
        
