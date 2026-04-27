import streamlit as st

# إعدادات الصفحة لتظهر كأنها تطبيق موبايل
st.set_page_config(page_title="دارجي", layout="centered", initial_sidebar_state="collapsed")

# --- CSS مخصص لمحاكاة تصميم ريبلت الأصلي ---
st.markdown("""
    <style>
    /* إخفاء العناصر الافتراضية لزيادة السلاسة */
    header {visibility: hidden;}
    .main { background-color: #fcfcfc; }
    
    /* شريط العنوان العلوي (أبيض نظيف) */
    .top-bar {
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: white; border-bottom: 1px solid #f0f0f0;
    }
    .logo-text { color: #007b83; font-weight: bold; font-size: 22px; }

    /* البطاقة التعريفية (Hero Section) */
    .hero-box {
        background-color: #f1f8f8; border-radius: 25px;
        padding: 35px 20px; text-align: center; margin: 15px;
        border: 1px solid #e0eeee;
    }
    .hero-title { font-size: 26px; font-weight: bold; color: #1a1a1a; line-height: 1.3; }
    .hero-sub { font-size: 14px; color: #666; margin-top: 10px; }

    /* الشريط السفلي الثابت (Floating Nav) */
    .nav-wrapper {
        position: fixed; bottom: 0; left: 0; right: 0;
        background: white; display: flex; justify-content: space-around;
        padding: 12px 0; border-top: 1px solid #eee; z-index: 1000;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# إدارة الصفحات
if 'active_page' not in st.session_state:
    st.session_state.active_page = 'الرئيسية'

# 1. الهيدر العلوي
st.markdown("""
    <div class="top-bar">
        <div style="font-size: 22px;">👤</div>
        <div class="logo-text">دارجي</div>
    </div>
""", unsafe_allow_html=True)

# --- الصفحة الرئيسية ---
if st.session_state.active_page == 'الرئيسية':
    st.markdown("""
        <div class="hero-box">
            <div class="hero-title">لا تحتار.. أسطوات<br>ديرتك <span style="color:#007b83;">بين يديك</span></div>
            <div class="hero-sub">دليلك الموثوق لأفضل الورش في ميسان</div>
        </div>
    """, unsafe_allow_html=True)

    # 2. زر البحث الفعال
    search_col1, search_col2 = st.columns([1, 4])
    with search_col2:
        query = st.text_input("", placeholder="ابحث عن أسطى، ورشة، اختصاص...", label_visibility="collapsed")
    with search_col1:
        if st.button("بحث", use_container_width=True):
            if query:
                st.info(f"🔍 جاري البحث عن: {query}")
            else:
                st.warning("يرجى كتابة شيء للبحث")

    # 3. تصنيفات المركبات
    st.markdown("<p style='text-align:right; padding: 10px 20px 0 0; font-weight:bold;'>⭐ حسب نوع المركبة</p>", unsafe_allow_html=True)
    cats = ["سيدان", "بيك أب", "حوض", "شاحنة", "دراجة"]
    c_cols = st.columns(len(cats))
    for idx, c in enumerate(cats):
        c_cols[idx].button(c, key=f"cat_{idx}")

# --- صفحة الإدارة (إدخال الأسطى) ---
elif st.session_state.active_page == 'الإدارة':
    st.markdown("<h3 style='text-align:center; color:#007b83;'>تسجيل أسطى جديد</h3>", unsafe_allow_html=True)
    
    with st.container(border=True):
        name = st.text_input("اسم الأسطى أو الورشة")
        
        # إدخال الرقم وتاكيده كما طلبت
        phone = st.text_input("رقم الهاتف")
        confirm_phone = st.text_input("تأكيد رقم الهاتف")
        
        specialty = st.selectbox("الاختصاص", ["ميكانيك", "كهرباء", "تيربو", "حدادة"])
        
        if st.button("تأكيد التسجيل ✅", use_container_width=True):
            if not phone or not confirm_phone:
                st.error("الرجاء إدخال الرقم وتأكيده")
            elif phone != confirm_phone:
                st.error("رقم الهاتف غير متطابق!")
            else:
                st.success(f"تم تسجيل {name} بنجاح وجاري التفعيل")

# 4. الشريط السفلي (Navigation) لتبديل الصفحات بسلاسة
st.markdown("<br><br><br>", unsafe_allow_html=True)
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)

with nav_col1:
    if st.button("🏠\nالرئيسية"): st.session_state.active_page = 'الرئيسية'
with nav_col2:
    if st.button("🔧\nالدليل"): st.session_state.active_page = 'الرئيسية'
with nav_col3:
    if st.button("⚠️\nبلاغ"): st.info("سيتم تفعيل قسم البلاغات قريباً")
with nav_col4:
    if st.button("🔒\nالإدارة"): st.session_state.active_page = 'الإدارة'
