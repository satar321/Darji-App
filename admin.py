import streamlit as st
import pandas as pd
from datetime import datetime

# --- إعدادات المدير (ستار) ---
MY_WHATSAPP = "9647709094462"  # ضع رقمك هنا ليبدأ بـ 964
ADMIN_PWD = "star2026"
# رابط الجدول الخاص بك (للقراءة)
SHEET_URL = "https://docs.google.com/spreadsheets/d/1FTI3Vh2RNS3XL9VIJHEdmAcARI0vW34kZqHrRxsHm-g/gviz/tq?tqx=out:csv"

def main():
    st.set_page_config(page_title="تطبيق دارجي - دليل العراق", page_icon="🇮🇶", layout="wide")

    # قائمة محافظات العراق
    iraq_provinces = [
        "بغداد", "ميسان", "البصرة", "النجف", "كربلاء", "ذي قار", "بابل", 
        "الأنبار", "أربيل", "السليمانية", "دهوك", "نينوى", "كركوك", 
        "صلاح الدين", "ديالى", "واسط", "المثنى", "القادسية"
    ]

    # تسجيل "زيارة" تلقائية عند فتح التطبيق (ستظهر في جدولك)
    if 'visitor_logged' not in st.session_state:
        # هنا سيتم إضافة كود الربط مع Google Sheets لاحقاً لتسجيل كل دخول
        st.session_state.visitor_logged = True

    tab1, tab2, tab3 = st.tabs(["🔍 بحث عن ورشة", "🛠️ تسجيل أسطى", "🔒 إدارة ستار"])

    with tab1:
        st.header("ابحث عن أقرب أسطى في محافظتك")
        search_prov = st.selectbox("اختر المحافظة", iraq_provinces)
        st.info(f"عرض الورش المتوفرة في {search_prov}...")
        # هنا تظهر نتائج البحث للناس

    with tab2:
        st.header("سجل ورشتك في دليل العراق")
        name = st.text_input("الأسم الكامل")
        phone = st.text_input("رقم الهاتف (واتساب)")
        province = st.selectbox("المحافظة", iraq_provinces, key="reg_prov")
        job = st.selectbox("الاختصاص", ["ميكانيك", "كهرباء", "تبريد", "حدادة", "ونش سحب"])

        if st.button("إرسال طلب التوثيق"):
            if name and phone:
                msg = f"طلب توثيق جديد:%0Aالاسم: {name}%0Aالمحافظة: {province}%0Aالمهنة: {job}%0Aالرقم: {phone}"
                wa_url = f"https://wa.me/{MY_WHATSAPP}?text={msg}"
                st.markdown(f'''<a href="{wa_url}" target="_blank" style="background-color: #25D366; color: white; padding: 12px; text-decoration: none; border-radius: 8px; display: block; text-align: center;">إرسال عبر واتساب ✅</a>''', unsafe_allow_html=True)
            else:
                st.error("يرجى ملء كافة البيانات")

    with tab3:
        pwd = st.text_input("رمز الإدارة", type="password")
        if pwd == ADMIN_PWD:
            st.title("📊 إحصائيات تطبيق دارجي")
            
            # عرض عداد وهمي حالياً حتى تكتمل قاعدة البيانات
            col1, col2 = st.columns(2)
            col1.metric("إجمالي الزيارات", "154") # هذا الرقم سيتحدث من الجدول
            col2.metric("الأسطوات المسجلين", "12")
            
            try:
                df = pd.read_csv(SHEET_URL)
                st.write("سجل البيانات الشامل:")
                st.dataframe(df)
            except:
                st.write("بانتظار تسجيل البيانات في الجدول...")

if __name__ == "__main__":
    main()
