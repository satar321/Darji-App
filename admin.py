import streamlit as st
import pandas as pd

# --- الإعدادات ---
ADMIN_DATA = {"star": "star2026", "moshref": "iraq2026"}
SHEET_URL = "https://docs.google.com/spreadsheets/d/1FTI3Vh2RNS3XL9VIJHEdmAcARI0vW34kZqHrRxsHm-g/gviz/tq?tqx=out:csv"
WHATSAPP = "9647709094462"

def main():
    st.set_page_config(page_title="دارجي العراق", page_icon="🇮🇶")
    
    menu = ["🏠 الرئيسية", "🛠️ تسجيل أسطى", "🔒 لوحة التحكم"]
    choice = st.sidebar.selectbox("القائمة", menu)

    if choice == "🏠 الرئيسية":
        st.title("🚗 أهلاً بك في تطبيق دارجي")
        st.write("هنا ستظهر ورش التصليح الموثقة قريباً.")
        st.image("https://via.placeholder.com/800x400.png?text=Darji+Iraq+App") # يمكنك وضع شعار تطبيقك هنا

    elif choice == "🛠️ تسجيل أسطى":
        st.header("تسجيل ورشة جديدة")
        with st.form("reg"):
            name = st.text_input("الأسم الكامل")
            phone = st.text_input("رقم الهاتف")
            prov = st.selectbox("المحافظة", ["بغداد", "ميسان", "البصرة", "ذي قار", "النجف", "كربلاء"])
            if st.form_submit_button("إرسال للتوثيق ✅"):
                msg = f"طلب جديد: {name} - {prov} - {phone}"
                st.markdown(f'[اضغط هنا للإرسال وتفعيل حسابك](https://wa.me/{WHATSAPP}?text={msg})')

    elif choice == "🔒 لوحة التحكم":
        st.header("دخول الإدارة")
        user = st.text_input("اسم المستخدم")
        pwd = st.text_input("كلمة المرور", type="password")
        if st.button("دخول"):
            if user in ADMIN_DATA and pwd == ADMIN_DATA[user]:
                st.success(f"أهلاً ستار! إليك بيانات الأسطوات:")
                try:
                    df = pd.read_csv(SHEET_URL)
                    st.table(df) # هذا سيعرض الجدول فوراً
                except:
                    st.warning("لا توجد بيانات مسجلة في الجدول حالياً.")

if __name__ == "__main__":
    main()
