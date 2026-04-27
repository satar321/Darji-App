import streamlit as st

# إعدادات المظهر الأساسية
st.set_page_config(page_title="دارجي", layout="centered", initial_sidebar_state="collapsed")

# --- تنسيق التصميم السلس (CSS) ---
st.markdown("""
    <style>
    header {visibility: hidden;}
    .main { background-color: #ffffff; }
    
    /* شريط العنوان العلوي */
    .header-style {
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: white; border-bottom: 1px solid #eee;
    }
    .logo-font { color: #007b83; font-weight: bold; font-size: 22px; }

    /* بانر الترحيب (نفس القديم) */
    .hero-banner {
        background-color: #f1f8f8; border-radius: 25px;
        padding: 40px 20px; text-align: center; margin: 15px;
    }
    .hero-h1 { font-size: 26px; font-weight: bold; color: #1a1a1a; }

    /* شريط التنقل السفلي الثابت */
    .nav-footer {
        position: fixed; bottom: 0; left: 0; right: 0;
        background: white; display: flex; justify-content: space-around;
        padding: 12px; border-top: 1px solid #eee; z-index: 1000;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# 1. عرض الهيدر العلوي
st.markdown('<div class="header-style"><div style="font-size:20px;">👤</div><div class="logo-font">دارجي</div></div>', unsafe_allow_html=True)

# --- الصفحة الرئيسية (Home) ---
if st.session_state.page == 'home':
    st.markdown("""
        <div class="hero-banner">
            <div class="hero-h1">لا تحتار.. أسطوات<br>ديرتك <span style="color:#007b83;">بين يديك</span></div>
            <p style="color: #666; font-size: 14px; margin-top: 10px;">دليلك الموثوق في ميسان</p>
        </div>
    """, unsafe_allow_html=True)

    # قسم البحث الفعال
    with st.container():
        c1, c2 = st.columns([1, 4])
        with c2:
            query = st.text_input("", placeholder="ابحث عن أسطى، ورشة، أو تخصص...", label_visibility="collapsed")
        with c1:
            if st.button("بحث", use_container_width=True):
                if query:
                    st.success(f"🔍 جاري البحث عن: {query}")
                else:
                    st.warning("اكتب شيئاً!")

    # تصنيفات المركبات
    st.markdown("<p style='text-align:right; padding-right:20px; font-weight:bold;'>⭐ حسب نوع المركبة</p>", unsafe_allow_html=True)
    cats = ["سيدان", "بيك أب", "حوض", "شاحنة", "دراجة"]
    cols = st.columns(5)
    for i, cat in enumerate(cats):
        cols[i].button(cat, key=cat)

# --- صفحة الإدارة (تسجيل الأسطى) ---
elif st.session_state.page == 'admin':
    st.markdown("<h3 style='text-align:center;'>تسجيل ورشة جديدة</h3>", unsafe_allow_html=True)
    with st.container(border=True):
        st.text_input("الأسم الكامل للأسطى")
        
        # نظام التأكيد بالرقم (مهم جداً)
        phone = st.text_input("رقم الهاتف")
        confirm_phone = st.text_input("تأكيد رقم الهاتف")
        
        st.selectbox("المحافظة", ["ميسان", "بغداد", "البصرة"])
        st.selectbox("الاختصاص", ["ميكانيك", "كهرباء", "تيربو"])
        
        if st.button("إرسال طلب التفعيل ✅", use_container_width=True):
            if phone == confirm_phone and len(phone) > 5:
                st.success("تم تأكيد الرقم وإرسال الطلب!")
            else:
                st.error("رقم الهاتف غير متطابق!")

# 2. شريط التنقل السفلي (أزرار حقيقية لتغيير الصفحة)
st.markdown("<br><br><br>", unsafe_allow_html=True)
n1, n2, n3, n4 = st.columns(4)
with n1:
    if st.button("🏠\nالرئيسية"): st.session_state.page = 'home'
with n2:
    if st.button("🔧\nالدليل"): st.session_state.page = 'home'
with n3:
    if st.button("⚠️\nبلاغ"): st.info("قريباً")
with n4:
    if st.button("🔒\nالإدارة"): st.session_state.page = 'admin'
