import streamlit as st
import pandas as pd

# --- إعدادات الإدارة (ستار) ---
MY_WHATSAPP = "9647709094462" 
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/1FTI3Vh2RNS3XL9VIJHEdmAcARI0vW34kZqHrRxsHm-g/gviz/tq?tqx=out:csv"

ADMIN_DATA = {
    "star": "star2026",
    "moshref": "iraq2026"
}

def main():
    st.set_page_config(page_title="دارجي العراق - الإدارة", page_icon="🇮🇶")

    menu = ["🏠 الرئيسية", "🛠️ تسجيل أسطى", "🔒 لوحة التحكم"]
    choice = st.sidebar.selectbox("القائمة", menu)

    if choice == "🛠️ تسجيل أسطى":
        st.header("تسجيل ورشة جديدة")
        with st.form("reg_form"):
            name = st.text_input("الأسم الكامل")
            phone = st.text_input("رقم الهاتف")
            prov = st.selectbox("المحافظة", ["بغداد", "ميسان", "البصرة", "ذي قار", "النجف", "كربلاء", "بابل", "الأنبار", "نينوى", "ديالى", "واسط", "صلاح الدين", "كركوك", "المثنى", "القادسية", "أربيل", "السليمانية", "دهوك"])
            job = st.selectbox("الاختصاص", ["ميكانيك", "كهرباء", "تبريد", "حدادة", "ونش"])
            
            if st.form_submit_button("إرسال طلب التفعيل ✅"):
                if name and phone:
                    # تنسيق الرسالة لتكون منظمة جداً عند وصولها لمجموعتك
                    msg = (
                        f"*📌 طلب تسجيل أسطى جديد*%0A"
                        f"----------------------------%0A"
                        f"*👤 الاسم:* {name}%0A"
                        f"*📍 المحافظة:* {prov}%0A"
                        f"*🔧 المهنة:* {job}%0A"
                        f"*📞 الرقم:* {phone}%0A"
                        f"----------------------------%0A"
                        f"*✅ للموافقة التلقائية:* يرجى الرد بكلمة (تم التفعيل)"
                    )
                    wa_url = f"https://wa.me/{MY_WHATSAPP}?text={msg}"
                    st.success("تم تنظيم طلبك! اضغط الزر لإرساله للإدارة.")
                    st.markdown(f'<a href="{wa_url}" target="_blank" style="background-color: #25D366; color: white; padding: 12px; text-decoration: none; border-radius: 8px; display: block; text-align: center; font-weight: bold;">إرسال للتوثيق الآن ✅</a>', unsafe_allow_html=True)
                else:
                    st.error("يرجى إكمال البيانات")

    elif choice == "🔒 لوحة التحكم":
        # كود الإدارة والجدول (نفس السابق)
        pass

if __name__ == "__main__":
    main()
