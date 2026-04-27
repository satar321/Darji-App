import streamlit as st
import pandas as pd

# --- إعدادات الأمان والبيانات ---
ADMIN_DATA = {"star": "star2026", "moshref": "iraq2026"}
SHEET_URL = "https://docs.google.com/spreadsheets/d/1FTI3Vh2RNS3XL9VIJHEdmAcARI0vW34kZqHrRxsHm-g/gviz/tq?tqx=out:csv"
WHATSAPP_NUMBER = "9647709094462"

def main():
    # إعدادات الصفحة لجعلها تبدو كتطبيق موبايل أصلي
    st.set_page_config(
        page_title="دارجي العراق",
        page_icon="🚗",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # تنسيق الألوان والتصميم (CSS) لجعل الواجهة أجمل
    st.markdown("""
        <style>
        .main { background-color: #f5f7f9; }
        .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #1e3a8a; color: white; }
        .stTextInput>div>div>input { border-radius: 10px; }
        h1 { color: #1e3a8a; text-align: center; font-family: 'Arial'; }
        .stAlert { border-radius: 10px; }
        </style>
    """, unsafe_allow_html=True)

    # القائمة الجانبية
    menu = ["🏠 الرئيسية", "🛠️ تسجيل أسطى", "🔒 إدارة ستار"]
    choice = st.sidebar.selectbox("انتقل إلى:", menu)

    if choice == "🏠 الرئيسية":
        st.markdown("<h1>🚗 تطبيق دارجي</h1>", unsafe_allow_html=True)
        st.info("مرحباً بك يا ستار! هذا هو دليلك لإدارة ورش تصليح السيارات في العراق.")
        
        # محرك بحث بسيط (سيتم تفعيله عند امتلاء البيانات)
        search = st.text_input("🔍 ابحث عن ورشة أو اختصاص (ميكانيك، كهرباء...)", placeholder="اكتب هنا للبحث...")
        
        st.write("---")
        st.caption("التطبيق قيد التحديث المستمر لإضافة كافة المحافظات.")

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
                    # تنسيق الرسالة المنظمة لمجموعتك
                    msg = f"*📌 طلب توثيق جديد*%0A------------------%0A*👤 الاسم:* {name}%0A*📍 المحافظة:* {prov}%0A*🔧 الاختصاص:* {job}%0A*📞 الهاتف:* {phone}"
                    wa_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={msg}"
                    st.success("تم تجهيز طلبك!")
                    st.markdown(f'<a href="{wa_url}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:15px; text-align:center; border-radius:10px; font-weight:bold;">إرسال عبر واتساب الآن 💬</div></a>', unsafe_allow_html=True)
                else:
                    st.error("يرجى ملء جميع الحقول")

    elif choice == "🔒 إدارة ستار":
        st.markdown("<h1>🔒 لوحة التحكم</h1>", unsafe_allow_html=True)
        user = st.text_input("اسم المستخدم")
        pwd = st.text_input("كلمة المرور", type="password")
        
        if st.button("دخول"):
            if user in ADMIN_DATA and pwd == ADMIN_DATA[user]:
                st.success("أهلاً بك يا مدير! هذه بيانات الأسطوات المسجلين:")
                try:
                    df = pd.read_csv(SHEET_URL)
                    st.dataframe(df, use_container_width=True)
                except:
                    st.error("عذراً، لا يمكن الوصول لجدول البيانات حالياً.")
            else:
                st.error("البيانات غير صحيحة")

if __name__ == "__main__":
    main()
