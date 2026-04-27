import streamlit as st

# إعداد الصفحة لتكون نظيفة (إخفاء القوائم الجانبية والافتراضية)
st.set_page_config(page_title="دارجي", layout="centered", initial_sidebar_state="collapsed")

# --- CSS متقدم لمحاكاة تصميم "ريبلت" الاحترافي ---
st.markdown("""
    <style>
    header {visibility: hidden;}
    .main { background-color: #ffffff; }
    
    /* الهيدر العلوي */
    .top-header {
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 15px; background: white; border-bottom: 1px solid #f0f0f0;
    }
    .logo-text { color: #007b83; font-weight: bold; font-size: 24px; }

    /* كرت الترحيب الكبير (Hero Section) بنفس ألوان الصورة */
    .hero-container {
        background-color: #f1f8f8; border-radius: 20px;
        padding: 30px 15px; text-align: center; margin: 15px;
        position: relative; overflow: hidden;
    }
    .hero-text { font-size: 24px; font-weight: 800; color: #1a1a1a; line-height: 1.3; }
    .hero-sub { color: #666; font-size: 14px; margin-top: 10px; }

    /* شريط البحث الاحترافي */
    .search-box {
        display: flex; align-items: center; background: white;
        border: 1px solid #e0e0e0; border-radius: 15px;
        padding: 5px 15px; margin: -25px 25px 20px 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    /* أزرار التصنيفات (سيدان، بيك أب...) */
    .cat-btn {
        background: #f8f9fa; border: 1px solid #eee; border-radius: 12px;
        padding: 8px 12px; font-size: 13px; color: #444;
    }

    /* الشريط السفلي الثابت (Navigation) */
    .fixed-nav {
        position: fixed; bottom: 0; left: 0; right: 0;
        background: white; display: flex; justify-content: space-around;
        padding: 10px 0; border-top: 1px solid #eee; z-index: 1000;
    }
    .nav-item { text-align: center; color: #888; font-size: 12px; }
    .nav-item.active { color: #007b83; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# إدارة الصفحات (Navigation State)
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# 1. عرض الهيدر العلوي
st.markdown("""
    <div class="top-header">
        <div style="font-size:22px;">👤</div>
        <div class="logo-text">دارجي</div>
    </div>
""", unsafe_allow_html=True)

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    # كرت الترحيب
    st.markdown("""
        <div class="hero-container">
            <div style="color:#007b83; font-size:12px; margin-bottom:10px;">دليلك الموثوق في ميسان</div>
            <div class="hero-text">لا تحتار.. أسطوات<br>ديرتك <span style="color:#007b83;">بين يديك</span></div>
            <div class="hero-sub">دارجي يجمع لك أفضل الأسطوات والورش في مكان واحد</div>
        </div>
    """, unsafe_allow_html=True)

    # شريط البحث الفعال
    with st.container():
        col_s1, col_s2 = st.columns([4, 1])
        with col_s1:
            search_query = st.text_input("", placeholder="ابحث عن أسطى، ورشة، أو تخصص...", label_visibility="collapsed")
        with col_s2:
            if st.button("بحث"):
                if search_query: st.toast(f"جاري البحث عن {search_query}...")

    # تصنيفات المركبات
    st.markdown("<p style='text-align:right; padding-right:20px; font-weight:bold;'>⭐ حسب نوع المركبة</p>", unsafe_allow_html=True)
    cats = ["سيدان", "بيك أب", "حوض", "شاحنة", "دراجة"]
    cat_cols = st.columns(len(cats))
    for i, cat in enumerate(cats):
        cat_cols[i].button(cat, key=cat, use_container_width=True)

    # بانر المساعدة البرتقالي
    st.markdown("""
        <div style="background:#ff8c00; color:white; border-radius:15px; padding:20px; margin:20px; text-align:right;">
            <h4 style="margin:0;">عندك عطل ومحتاج مساعدة؟</h4>
            <p style="font-size:12px; margin:5px 0;">بلغ عن عطل مركبتك ونوصلك بأقرب أسطى متوفر</p>
            <button style="background:white; color:#ff8c00; border:none; border-radius:10px; padding:5px 15px; font-weight:bold;">بلغ الحين ⚠️</button>
        </div>
    """, unsafe_allow_html=True)

# --- صفحة الإدارة (تسجيل الأسطى) ---
elif st.session_state.page == 'admin':
    st.markdown("<h3 style='text-align:center; color:#007b83;'>تسجيل أسطى جديد</h3>", unsafe_allow_html=True)
    with st.form("mechanic_form"):
        st.text_input("الأسم الكامل")
        phone = st.text_input("رقم الهاتف (للتواصل)")
        confirm_phone = st.text_input("تأكيد رقم الهاتف")
        st.selectbox("الاختصاص", ["ميكانيك", "كهرباء", "تيربو", "تبريد"])
        submit = st.form_submit_button("إرسال طلب التسجيل ✅", use_container_width=True)
        if submit:
            if phone == confirm_phone and len(phone) > 5:
                st.success("تم إرسال طلبك بنجاح! سيتم التواصل معك قريباً.")
            else:
                st.error("رقم الهاتف غير متطابق!")

# 2. شريط التنقل السفلي (أزرار تفاعلية)
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
n1, n2, n3, n4 = st.columns(4)
with n1:
    if st.button("🏠\nالرئيسية"): st.session_state.page = 'home'
with n2:
    if st.button("🔧\nالدليل"): st.session_state.page = 'home'
with n3:
    if st.button("⚠️\nبلاغ"): st.info("قريباً")
with n4:
    if st.button("🔒\nالإدارة"): st.session_state.page = 'admin'
