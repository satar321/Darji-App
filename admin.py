import streamlit as st

# إعداد واجهة صفحة الإدارة
def admin_page():
    st.title("🛠️ لوحة إدارة تطبيق دارجي")
    st.write("مرحباً بك يا أسطى ستار في لوحة التحكم")

    # نظام دخول بسيط
    password = st.text_input("أدخل كلمة المرور للدخول للإدارة", type="password")
    
    if password == "1990@@@1990": # يمكنك تغيير كلمة السر لاحقاً
        st.success("تم تسجيل الدخول بنجاح")
        
        # خيارات الإدارة
        option = st.selectbox("ماذا تريد أن تفعل؟", 
                             ["إضافة ورشة جديدة", "تعديل بيانات ورشة", "حذف بلاغ"])
        
        if option == "إضافة ورشة جديدة":
            name = st.text_input("اسم الورشة")
            location = st.text_input("موقع الورشة (في ميسان)")
            phone = st.text_input("رقم الهاتف")
            if st.button("حفظ البيانات"):
                st.write(f"تم حفظ ورشة {name} بنجاح!")
    else:
        st.warning("يرجى إدخال كلمة المرور الصحيحة للوصول للصلاحيات")

# تشغيل الصفحة
if __name__ == "__main__":
    admin_page()
