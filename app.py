import streamlit as st

# إعدادات الصفحة وتصميمها
st.set_page_config(
    page_title="تطبيق خرجني - دليل الخروجات الذكي", 
    page_icon="🚀", 
    layout="wide"
)

# تصميم CSS مخصص لتجميل الشكل وإعطاء طابع احترافي
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #ff4757;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        color: #718093;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        border-right: 5px solid #ff4757;
    }
    .stButton>button {
        background-color: #ff4757;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #e84118;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# عنوان التطبيق
st.markdown('<p class="main-title">🚀 تطبيق خرجني - دليل الخروجات الأذكى في مصر</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">حدد موقعك أو اختر منطقتك، واعرف أحسن المطاعم، الكافيهات، والنوادي حواليك!</p>', unsafe_allow_html=True)

# قاعدة بيانات شاملة لأشهر مناطق وأماكن مصر
database = {
    "وسط البلد (Downtown)": {
        "🍔 مطاعم وبرجر وفريت": [
            {"name": "برجر كنج", "type": "برجر وسريع", "rate": "⭐ 4.5", "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Burger+King+Downtown+Cairo"},
            {"name": "باستا الانسجام", "type": "مكرونة وكبدة وسريعة", "rate": "⭐ 4.6", "img": "https://images.unsplash.com/photo-1621996346565-e3d5d6281298?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Makarona+El+Ensgam+Cairo"},
            {"name": "بافلو برجر", "type": "برجر مصري أصيل", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Buffalo+Burger+Downtown"}
        ],
        "☕ كافيهات وقعدات رايقة": [
            {"name": "قهوة زهرة البستان", "type": "قهوة تاريخية وثقافية", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Zahret+Al+Bostan+Cairo"},
            {"name": "راديوم كافيه", "type": "قعدة شبابية وهادئة", "rate": "⭐ 4.4", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Downtown+Cafes+Cairo"}
        ],
        "🍨 حلويات ومرطبات": [
            {"name": "بى لبن", "type": "أرز بلبن وإضافات ابتكارية", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=BLaban+Downtown+Cairo"},
            {"name": "كريسبي كريم", "type": "دونتس وقهوة", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1514517521153-1be72277b32f?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Krispy+Kreme+Cairo"}
        ]
    },
    "المعادي (Maadi)": {
        "🍔 مطاعم وبرجر وفريت": [
            {"name": "لولو كافيه ورستو", "type": "أكل عالمي وقعدات راقية", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Maadi+Restaurants"}
        ],
        "☕ كافيهات وقعدات رايقة": [
            {"name":_ "سيلانترو المعادي", "type": "قهوة وقعدة عمل ومذاكرة", "rate": "⭐ 4.6", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Cilantro+Maadi"}
        ],
        "🌳 نوادي وتنزيلات": [
            {"name": "نادي اليخت المصري", "type": "نادي على النيل مباشرة", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Egyptian+Yacht+Club+Maadi"}
        ]
    },
    "الشيخ زايد ومدينة السادس من أكتوبر (Zayed & October)": {
        "🍔 مطاعم وبرجر وفريت": [
            {"name": "ذا يارد زايد", "type": "مجمع مطاعم وكافيهات مفتوح", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=The+Yard+Zayed"}
        ],
        "☕ كافيهات وقعدات رايقة": [
            {"name": "أركان بلازا كافيهات", "type": "أرقى قعدات ومطاعم أكتوبر", "rate": "⭐ 4.9", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Arkan+Plaza+Zayed"}
        ]
    }
}

# شريط جانبى للتحكم المتقدم (اختيار الموقع أو التحديد التلقائي)
st.sidebar.header("📍 أدوات البحث وتحديد الموقع")

search_mode = st.sidebar.radio("اختر طريقة البحث:", ["اختر منطقتك يدويًا", "حدد موقعي عبر الجي بي إس (GPS)"])

selected_region = "وسط البلد (Downtown)"

if search_mode == "اختر منطقتك يدويًا":
    selected_region = st.sidebar.selectbox("اختر المنطقة الحالية:", list(database.keys()))
else:
    st.sidebar.info("اضغط على الزر أدناه لتفعيل الموقع الجغرافي بمتصفحك:")
    # كود جافاسكريبت صغير لتحديد الموقع الحقيقي للمستخدم وعرضه
    st.sidebar.markdown("""
        <script>
        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function(position) {
                    alert("تم رصد موقعك بنجاح! خط عرض: " + position.coords.latitude.toFixed(2) + " , خط طول: " + position.coords.longitude.toFixed(2));
                });
            } else {
                alert("الخاصية غير مدعومة في متصفحك.");
            }
        }
        </script>
        <button onclick="getLocation()" style="background:#00a8ff; color:white; border:none; padding:8px 15px; border-radius:5px; cursor:pointer; font-weight:bold;">📍 تفعيل حساس الموقع</button>
    """, unsafe_allow_html=True)
    st.sidebar.success("تم افتراض وجودك في (وسط البلد) بناءً على أقرب نطاق افتراضي متاح حالياً.")

st.markdown(f"### 📌 النتائج والأماكن المتاحة في: **{selected_region}**")

# عرض الأماكن مقسمة بأقسام احترافية (Tabs)
region_categories = database[selected_region]
tabs = st.tabs(list(region_categories.keys()))

for index, (category_name, places_list) in enumerate(region_categories.items()):
    with tabs[index]:
        st.markdown(f"#### أقسام {category_name}")
        
        # عرض الأماكن في أعمدة منظمة (كل صف 3 كروت)
        cols = st.columns(3)
        for i, place in enumerate(places_list):
            with cols[i % 3]:
                st.markdown(f"""
                    <div class="card">
                        <img src="{place['img']}" style="width:100%; height:140px; object-fit:cover; border-radius:10px; margin-bottom:10px;">
                        <h4 style="margin:5px 0; color:#2f3640;">{place['name']}</h4>
                        <p style="color:#718093; font-size:13px; margin:2px 0;"><b>النوع:</b> {place['type']}</p>
                        <p style="color:#e1b12c; font-weight:bold; font-size:14px; margin:5px 0;">{place['rate']}</p>
                        <a href="{place['map']}" target="_blank" style="display:block; text-align:center; background:#00a8ff; color:white; padding:6px; border-radius:5px; text-decoration:none; font-weight:bold; margin-top:10px;">📍 افتح في جوجل ماب</a>
                    </div>
                """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #b2bec3;'>تطبيق خرجني 2026 - جميع الحقوق محفوظة لفنان البرمجة</p>", unsafe_allow_html=True)
