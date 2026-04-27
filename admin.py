import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="دارجي - دليل الأسطوات", layout="wide", initial_sidebar_state="collapsed")

# --- تنسيق CSS لمحاكاة التصميم القديم ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .header-text { color: #007b83; text-align: center; font-size: 24px; font-weight: bold; margin-bottom: 5px; }
    .sub-text { text-align: center; color: #666; font-size: 14px; margin-bottom: 20px; }
    .category-btn { background-color: white; border: 1px solid #ddd; border-radius: 20px; padding: 5px 15px; font-size: 12px; display: inline-block; margin: 2px; }
    .workshop-card { background-color: white; border-radius: 15px; padding: 15px; border: 1px solid #eee; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .status-dot { color: #28a745; font-size: 12px; float: left; }
    .btn-container { display: flex; gap: 10px; margin-top: 10px; }
    .btn-call { background-color: #007b83; color: white; flex: 1; text-align: center; padding: 8px; border-radius: 8px; text-decoration: none; font-size: 14px; }
    .btn-wa { background-color: white; color: #28a745; border: 1px solid #28a745; flex: 1; text-align: center; padding: 8px; border-radius: 8px; text-decoration: none; font-size: 14px; }
    .search-box { border-radius: 25px !important; }
    </style>
""", unsafe_allow_html=True)

# --- الواجهة الرئيسية ---
st.markdown('<div class="header-text">لا تحتار.. أسطوات ديرتك بين يديك</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">دارجي يجمع لك أفضل الأسطوات في مكان واحد: تصفح، اختر، وتواصل مباشرة</div>', unsafe_allow_html=True)

# خانة البحث
search_query = st.text_input("", placeholder="🔍 ابحث عن أسطى، ورشة، أو تخصص...", label_visibility="collapsed")

# تصنيفات نوع المركبة
st.write("⭐ **حسب نوع المركبة**")
categories = ["سيدان", "بيك أب", "حوض", "شاحنة", "دراجة نارية", "تكتك", "باص", "جيب/SUV", "تراكتور", "مان"]
cols_cat = st.columns(len(categories))
for idx, cat in enumerate(categories):
    with cols_cat[idx]:
        st.markdown(f'<div class="category-btn">{cat}</div>', unsafe_allow_html=True)

st.write("---")

# قسم الأسطوات (مثال لمحاكاة التصميم)
st.write("🟢 **أسطوات متصلين الآن**")

# جلب البيانات الحقيقية من جدولك
SHEET_URL = "https://docs.google.com/spreadsheets/d/1FTI3Vh2RNS3XL9VIJHEdmAcARI0vW34kZqHrRxsHm-g/gviz/tq?tqx=out:csv"
try:
    df = pd.read_csv(SHEET_URL)
    
    # عرض البيانات على شكل بطاقات
    col1, col2 = st.columns(2)
    for index, row in df.iterrows():
        target_col = col1 if index % 2 == 0 else col2
        with target_col:
            with st.container():
                st.markdown(f"""
                <div class="workshop-card">
                    <span class="status-dot">● متصل</span>
                    <div style="font-weight:bold; font-size:16px;">{row.get('الاسم', 'ورشة غير مسماة')}</div>
                    <div style="color:#888; font-size:12px;">📍 {row.get('المحافظة', 'العمارة')} - {row.get('الاختصاص', 'عام')}</div>
                    <div class="btn-container">
                        <a href="https://wa.me/{row.get('الهاتف', '')}" class="btn-wa">واتساب</a>
                        <a href="tel:{row.get('الهاتف', '')}" class="btn-call">اتصال</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
except:
    st.warning("جاري تحميل بيانات الأسطوات من الجدول...")

# لوحة الإدارة (مخفية في القائمة الجانبية)
with st.sidebar:
    st.title("🔒 إدارة ستار")
    if st.text_input("الرمز") == "star2026":
        st.write("أهلاً يا مدير!")
