import streamlit as st
import pandas as pd

# --- إعدادات الأمان والبيانات ---
ADMIN_DATA = {"star": "star2026", "moshref": "iraq2026"}
SHEET_URL = "https://docs.google.com/spreadsheets/d/1FTI3Vh2RNS3XL9VIJHEdmAcARI0vW34kZqHrRxsHm-g/gviz/tq?tqx=out:csv"
WHATSAPP_NUMBER = "9647709094462"

def main():
    st.set_page_config(
        page_title="دارجي العراق",
        page_icon="🚗",
        layout="centered"
    )

    # تنسيق الألوان والتصميم مع إضافة تنبيه التحميل
    st.markdown("""
        <style>
        .install-box {
            background-color: #fff3cd;
            color: #856404;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #ffeeba;
            text-align: center;
            margin-bottom: 20px;
            font-weight: bold;
        }
        .stButton>button { width: 100%; border-radius: 10px; background-color: #1e3a8a; color: white; }
        h1 { color: #1e3a8a; text-align: center; }
        </style>
    """, unsafe_allow_html=True)

    # --- رسالة التحميل (تظهر أول ما يدخل المستخدم) ---
    st.markdown("""
        <div class="install-box">
            📲 لتثبيت "دارجي" على شاشة موبايلك:<br>
            اضغط على النقاط الثلاث (⋮) في الأعلى ثم اختر "إضافة إلى الشاشة الرئيسية"
        </div>
    """, unsafe_allow_html=True)

    # القائمة الجانبية
    menu = ["🏠 الرئيسية", "🛠️ تسجيل أسطى", "🔒 إدارة ستار"]
    choice = st.sidebar.selectbox("القائمة", menu)

    if choice == "🏠 الرئيسية":
        st.markdown("<h1>🚗 تطبيق دارجي</h1>", unsafe_allow_html=True)
        st.success("مرحباً بك يا ستار! دليلك لإدارة ورش التصليح في العراق.")
        
        search = st.text_input("🔍 ابحث عن ورشة أو اختصاص (ميكانيك، كهرباء...)", placeholder="اكتب هنا للبحث...")
        st.write("---")
        st.caption("التطبيق قيد التحديث المستمر.")

    elif choice == "🛠️ تسجيل أسطى":
        st.markdown("<h1>🛠️ تسجيل ورشة جديدة</h1>", unsafe_allow_html=True)
        with st.form("registration_form"):
            name = st.text_input("الأسم الكامل")
            phone = st.text_input("رقم الهاتف")
            prov = st.selectbox("المحافظة", ["بغداد", "البصرة", "ميسان", "ذي قار", "النجف", "كربلاء", "بابل", "الأنبار", "نينوى", "ديالى", "واسط", "صلاح الدين", "كركوك", "المثنى", "القادسية", "أربيل", "السليمانية", "دهوك"])
            job = st.selectbox("الاختصاص", ["ميكانيك عام", "كهربائي", "تبريد", "حداد", "صباغ", "ونش سحب"])
            submit = st.form_submit_button("إرسال طلب التفعيل ✅")
            if submit:
                if name and phone:
                    msg = f"*📌 طلب توثيق جديد*%0A*👤 الاسم:* {name}%0A*📍 المحافظة:* {prov}%0A*🔧 الاختصاص:* {job}%0A*📞 الهاتف:* {phone}"
                    st.markdown(f'<a href="https://wa.me/{WHATSAPP_NUMBER}?text={msg}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:15px; text-align:center; border-radius:10px; font-weight:bold;">تأكيد الإرسال عبر واتساب 💬</div></a>', unsafe_allow_html=True)

    elif choice == "🔒 إدارة ستار":
        st.markdown("<h1>🔒 لوحة التحكم</h1>", unsafe_allow_html=True)
        user = st.text_input("اسم المستخدم")
        pwd = st.text_input("كلمة المرور", type="password")
        if st.button("دخول"):
            if user in ADMIN_DATA and pwd == ADMIN_DATA[user]:
                st.success("أهلاً يا ستار! إليك البيانات:")
                try:
                    df = pd.read_csv(SHEET_URL)
                    st.dataframe(df, use_container_width=True)
                except:
                    st.error("لا يمكن الوصول للجدول حالياً.")

if __name__ == "__main__":
    main()
