import streamlit as st
import random

st.set_page_config(page_title="KonstitutsiyaLab AI", page_icon="⚖️")

st.title("🇺🇿 KonstitutsiyaLab AI Platforma")
st.write("O‘zbekiston Respublikasining 2023-yilgi Konstitutsiyasi asosida AI yordamida o‘rganish platformasi")

menu = st.sidebar.radio("Bo‘limni tanlang:", ["Testlar", "Kazuslar", "Muhim ma'lumotlar"])

# === TESTLAR ===
if menu == "Testlar":
    st.header("🧩 Test sinovi")
    questions = [
        {
            "savol": "O‘zbekiston Respublikasining Konstitutsiyasi qachon kuchga kirgan?",
            "javoblar": ["1992-yil 8-dekabr", "2023-yil 1-may", "2022-yil 1-dekabr"],
            "togrisi": "2023-yil 1-may"
        },
        {
            "savol": "Konstitutsiyada nechta bo‘lim mavjud?",
            "javoblar": ["7 ta", "10 ta", "12 ta"],
            "togrisi": "7 ta"
        }
    ]
    ball = 0
    for q in questions:
        st.write("**" + q["savol"] + "**")
        ans = st.radio("Variantni tanlang:", q["javoblar"], key=q["savol"])
        if st.button("Javobni tekshirish", key=q["savol"]):
            if ans == q["togrisi"]:
                st.success("✅ To‘g‘ri javob!")
                ball += 1
            else:
                st.error(f"❌ Noto‘g‘ri. To‘g‘ri javob: {q['togrisi']}")
    st.info(f"Sizning umumiy ballingiz: {ball}/{len(questions)}")

# === KAZUSLAR ===
elif menu == "Kazuslar":
    st.header("⚖️ AI Kazus generatori")
    kazuslar = [
        "Fuqarolik masalalarida Konstitutsiya qoidalari qanday ustunlikka ega?",
        "Agar Prezident muddati tugashidan avval iste’foga chiqsa, kim vaqtincha vazifani bajaradi?",
        "Mahalliy kengash qarorlari Konstitutsiyaga zid bo‘lsa, nima bo‘ladi?"
    ]
    st.write(random.choice(kazuslar))

# === MUHIM MA'LUMOTLAR ===
elif menu == "Muhim ma'lumotlar":
    st.header("📘 Muhim Konstitutsiyaviy ma'lumotlar")
    st.markdown("""
    - **Kuchga kirgan sana:** 2023-yil 1-may  
    - **Bo‘limlar soni:** 7 ta  
    - **Moddalar soni:** 155 ta  
    - **Davlat tili:** O‘zbek tili  
    - **Xalq hokimiyatining manbai:** Xalq o‘zi  
    - **Prezident vakolat muddati:** 7 yil  
    """)
  
