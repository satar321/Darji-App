import streamlit as st

# إعدادات الصفحة الأساسية لتشبه التطبيقات
st.set_page_config(page_title="دارجي", layout="centered", initial_sidebar_state="collapsed")

# --- CSS مخصص لمحاكاة التصميم القديم بدقة ---
st.markdown("""
    <style>
    header {visibility: hidden;} /* إخفاء شريط ستريمليت */
    .main { background-color: #ffffff; }
    
    /* الشريط العلوي */
    .top-header {
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: white; border-bottom: 1px solid #eee;
    }

    /* بطاقة الترحيب */
    .welcome-card {
        background: #f1f8f8; border-radius: 25px;
        padding: 30px 20px; text-align: center; margin: 15px;
    }
    .hero-text { font-size: 24px; font-weight: bold; color: #333; }
    .hero-highlight { color: #007b83; }

    /* شريط البحث */
    .search-container {
        background: white; border-radius: 15px; padding: 5px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin: -25px 25px 20px 25px;
        display: flex; align-items: center;
    }

    /* الشريط السفلي الثابت */
    .footer-nav {
        position: fixed; bottom: 0; left: 0; right: 0;
        background: white; display: flex; justify-content: space-around;
        padding: 10px; border-top: 1px solid #eee; z-index: 1000;
    }
    .nav-btn { text-align: center; color: #777; font-size: 12px; cursor: pointer; }
    .nav-btn.active { color: #007b83; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# إدارة حالة الصفحة (Navigation State)
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# 1. الهيدر العلوي
st.markdown('<div class="top-header"><div style="font-size:20px;">👤</div><div style="color:#007b83; font-weight:bold;">دارجي 🏠</div></div>', unsafe_allow_html=True)

# --- محتوى الصفحة الرئيسية ---
if st.session_state.page == 'home':
    st.markdown("""
        <div class="welcome-card">
            <div class="hero-text">لا تحتار.. أسطوات<br>ديرتك <span class="hero-highlight">بين يديك</span></div>
            <div style="font-size: 14px; color: #666; margin-top: 10px;">دليلك الموثوق في ميسان</div>
        </div>
    """, unsafe_allow_html=True)

    # قسم البحث (يعمل الآن)
    with st.container():
        col1, col2 = st.columns([1, 4])
        with col2:
            search_query = st.text_input("", placeholder="ابحث عن أسطى أو ورشة...", label_visibility="collapsed")
        with col1:
            search_trigger = st.button("بحث")
        
        if search_trigger and search_query:
            st.success(f"جاري البحث عن: {search_query}...")

    # تصنيفات المركبات
    st.markdown("<p style='text-align:right; padding-right:20px;'>⭐ حسب نوع المركبة</p>", unsafe_allow_html=True)
    cats = ["سيدان", "بيك أب", "حوض", "شاحنة", "دراجة"]
    cols = st.columns(len(cats))
    for i, cat in enumerate(cats):
        cols[i].button(cat, key=cat)

# --- محتوى صفحة تسجيل الأسطى ---
elif st.session_state.page == 'register':
    st.markdown("<h2 style='text-align:center;'>تسجيل ورشة جديدة</h2>", unsafe_allow_html=True)
    with st.form("workshop_form"):
        name = st.text_input("الأسم الكامل")
        phone = st.text_input("رقم الهاتف (سيصلك كود تأكيد)")
        confirm_phone = st.text_input("تأكيد رقم الهاتف")
        location = st.selectbox("المحافظة", ["ميسان", "بغداد", "البصرة"])
        specialty = st.selectbox("الاختصاص", ["ميكانيك", "كهرباء", "تيربو", "إطارات"])
        
        submitted = st.form_submit_state = st.form_submit_button("إرسال طلب التفعيل ✅")
        
        if submitted:
            if phone == confirm_phone and len(phone) >= 10:
                st.success("تم إرسال طلبك بنجاح! جاري مراجعة البيانات.")
            else:
                st.error("عذراً، تأكد من مطابقة رقم الهاتف.")

# --- محتوى صفحة البلاغات ---
elif st.session_state.page == 'report':
    st.warning("قسم البلاغات: بلغ عن عطل مركبتك وسنتصل بك.")
    st.text_area("وصف العطل")
    st.button("إرسال البلاغ")

# 6. شريط التنقل السفلي الثابت (Navigation Bar)
st.markdown("<br><br><br>", unsafe_allow_html=True) # مساحة للشريط
col_f1, col_f2, col_f3, col_f4 = st.columns(4)

with col_f1:
    if st.button("🏠\nالرئيسية"): st.session_state.page = 'home'
with col_f2:
    if st.button("🔧\nالدليل"): st.session_state.page = 'home'
with col_f3:
    if st.button("⚠️\nبلاغ"): st.session_state.page = 'report'
with col_f4:
    if st.button("🔒\nالإدارة"): st.session_state.page = 'register'
