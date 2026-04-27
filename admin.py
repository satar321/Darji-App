import streamlit as st

# إعدادات الصفحة كاملة
st.set_page_config(page_title="دارجي", layout="centered", initial_sidebar_state="collapsed")

# --- CSS لاستهداف التصميم القديم بدقة ---
st.markdown("""
    <style>
    /* إخفاء شريط Streamlit العلوي المزعج */
    header {visibility: hidden;}
    .main { background-color: #ffffff; padding-top: 0px; }
    
    /* الشريط العلوي الأبيض */
    .top-nav {
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: white; border-bottom: 1px solid #f0f0f0;
        position: sticky; top: 0; z-index: 999;
    }
    .logo-text { color: #007b83; font-weight: bold; font-size: 20px; }
    
    /* البطاقة الرئيسية (التركوازية) */
    .hero-card {
        background-color: #f1f8f8; border-radius: 30px;
        padding: 40px 20px; text-align: center; margin: 15px;
    }
    .hero-title { font-size: 26px; font-weight: bold; color: #000; line-height: 1.4; }
    .hero-highlight { color: #007b83; }
    
    /* محرك البحث */
    .search-bar {
        background: white; border: 1px solid #eee; border-radius: 15px;
        display: flex; align-items: center; padding: 10px 15px;
        margin: -30px 30px 20px 30px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .search-input { border: none; width: 100%; text-align: right; outline: none; }
    .search-btn { background: #007b83; color: white; border: none; padding: 8px 20px; border-radius: 10px; }

    /* التصنيفات */
    .cat-scroll { display: flex; overflow-x: auto; gap: 10px; padding: 10px 20px; }
    .cat-box { 
        background: #f8f9fa; border: 1px solid #eee; border-radius: 12px;
        padding: 8px 15px; min-width: 80px; text-align: center; font-size: 13px;
    }

    /* شريط التنقل السفلي */
    .bottom-nav {
        position: fixed; bottom: 0; left: 0; right: 0;
        background: white; display: flex; justify-content: space-around;
        padding: 12px; border-top: 1px solid #eee; z-index: 1000;
    }
    .nav-item { text-align: center; color: #999; font-size: 11px; }
    .nav-item.active { color: #007b83; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 1. شريط التنقل العلوي
st.markdown("""
    <div class="top-nav">
        <div style="font-size: 20px;">👤</div>
        <div class="logo-text">دارجي 🏠</div>
    </div>
""", unsafe_allow_html=True)

# 2. القسم الرئيسي
st.markdown("""
    <div class="hero-card">
        <div class="hero-title">لا تحتار.. أسطوات<br>ديرتك <span class="hero-highlight">بين يديك</span></div>
        <div style="color: #777; font-size: 14px; margin-top: 10px;">
            دارجي يجمع لك أفضل الأسطوات الورش في مكان واحد.<br>تصفح، اختر، وتواصل مباشرة.
        </div>
    </div>
""", unsafe_allow_html=True)

# 3. شريط البحث
st.markdown("""
    <div class="search-bar">
        <button class="search-btn">بحث</button>
        <input type="text" class="search-input" placeholder="ابحث عن أسطى، ورشة، أ...">
    </div>
""", unsafe_allow_html=True)

# 4. حسب نوع المركبة
st.markdown("<div style='text-align:right; padding: 0 20px; font-weight:bold;'>⭐ حسب نوع المركبة</div>", unsafe_allow_html=True)
st.markdown("""
    <div class="cat-scroll">
        <div class="cat-box">سيدان</div>
        <div class="cat-box">بيك أب</div>
        <div class="cat-box">حوض</div>
        <div class="cat-box">شاحنة</div>
        <div class="cat-box">دراجة</div>
    </div>
""", unsafe_allow_html=True)

# 5. التنبيه البرتقالي
st.markdown("""
    <div style="background: #ff8c00; color: white; margin: 20px; padding: 20px; border-radius: 15px; text-align: right;">
        <h4 style="margin:0;">عندك عطل ومحتاج مساعدة؟</h4>
        <div style="font-size: 12px; opacity: 0.9;">بلغ عن عطل مركبتك وخلينا نوصلك بأقرب أسطى</div>
    </div>
""", unsafe_allow_html=True)

# 6. شريط التنقل السفلي (الثابت)
st.markdown("""
    <div class="bottom-nav">
        <div class="nav-item">🔒<br>الإدارة</div>
        <div class="nav-item">⚠️<br>بلاغ</div>
        <div class="nav-item">🔧<br>الدليل</div>
        <div class="nav-item active">🏠<br>الرئيسية</div>
    </div>
""", unsafe_allow_html=True)

# إضافة مساحة في الأسفل لكي لا يغطي الشريط السفلي المحتوى
st.markdown("<br><br><br>", unsafe_allow_html=True)
