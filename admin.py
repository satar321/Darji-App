import streamlit as st
import pandas as pd

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="دارجي", layout="centered", initial_sidebar_state="collapsed")

# --- تطبيق التصميم القديم بدقة عبر CSS ---
st.markdown("""
    <style>
    /* تنسيق الخلفية العامة */
    .main { background-color: #fcfcfc; }
    
    /* الحاوية العلوية (التركوازية الفاتحة) */
    .hero-section {
        background-color: #f0f7f7;
        padding: 30px 15px;
        border-radius: 25px;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .hero-title { color: #000; font-size: 28px; font-weight: bold; margin-bottom: 0px; }
    .hero-highlight { color: #007b83; }
    .hero-sub { color: #666; font-size: 14px; line-height: 1.6; margin-top: 10px; }
    
    /* شريط البحث */
    .search-container {
        background: white;
        border-radius: 50px;
        padding: 5px 10px;
        display: flex;
        align-items: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-top: 20px;
    }
    .search-btn {
        background-color: #007b83 !important;
        color: white !important;
        border-radius: 40px !important;
        padding: 10px 25px !important;
        border: none;
    }
    
    /* تصنيفات المركبات */
    .cat-item {
        background: white;
        border: 1px solid #eee;
        border-radius: 15px;
        padding: 8px 12px;
        text-align: center;
        font-size: 13px;
        margin: 5px;
    }
    
    /* التنبيه البرتقالي */
    .orange-alert {
        background-color: #ff8c00;
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: right;
        margin-top: 20px;
        position: relative;
    }
    </style>
""", unsafe_allow_html=True)

# --- محاكاة الواجهة ---

# 1. قسم العنوان
st.markdown("""
    <div class="hero-section">
        <div class="hero-title">لا تحتار.. أسطوات<br>ديرتك <span class="hero-highlight">بين يديك</span></div>
        <div class="hero-sub">دارجي يجمع لك أفضل الأسطوات الورش<br>في مكان واحد. تصفح، اختر، وتواصل مباشرة.</div>
    </div>
""", unsafe_allow_html=True)

# 2. شريط البحث
col_s1, col_s2 = st.columns([1, 3])
with col_s1:
    st.button("بحث", key="search_btn")
with col_s2:
    st.text_input("", placeholder="ابحث عن أسطى، ورشة، أ...", label_visibility="collapsed")

# 3. حسب نوع المركبة
st.markdown("<div style='text-align:right; font-weight:bold; margin-top:20px;'>⭐ حسب نوع المركبة</div>", unsafe_allow_html=True)
categories = ["سيدان", "بيك أب", "حوض", "شاحنة", "دراجة"]
cols = st.columns(5)
for i, cat in enumerate(categories):
    cols[i].markdown(f'<div class="cat-item">{cat}</div>', unsafe_allow_html=True)

# 4. التنبيه البرتقالي
st.markdown("""
    <div class="orange-alert">
        <h4 style="margin:0;">عندك عطل ومحتاج مساعدة؟</h4>
        <p style="margin:5px 0 0 0; font-size:12px;">بلغ عن عطل مركبتك وخلينا نوصلك بأقرب أسطى</p>
    </div>
""", unsafe_allow_html=True)

# --- شريط التنقل السفلي (محاكاة) ---
st.markdown("""
    <hr style="margin-top:50px;">
    <div style="display: flex; justify-content: space-around; text-align: center; font-size: 12px; color: #007b83;">
        <div>🏠<br>الرئيسية</div>
        <div>🔧<br>الدليل</div>
        <div>⚠️<br>بلاغ</div>
        <div>🛡️<br>الإدارة</div>
    </div>
""", unsafe_allow_html=True)

# إضافة لوحة التحكم في القائمة الجانبية كما هي
with st.sidebar:
    if st.text_input("رمز الدخول", type="password") == "star2026":
        st.success("أهلاً يا ستار")
        # هنا تضع كود عرض الجدول الخاص بك
