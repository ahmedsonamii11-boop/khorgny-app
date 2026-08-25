import streamlit as st

# إعدادات الصفحة وتصميمها
st.set_page_config(
    page_title="تطبيق خرجني - الدليل الشامل", 
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
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        margin-bottom: 15px;
        border-right: 4px solid #ff4757;
    }
    </style>
""", unsafe_allow_html=True)

# عنوان التطبيق
st.markdown('<p class="main-title">🚀 تطبيق خرجني - الدليل الشامل للخروجات في مصر</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">اختر منطقتك، واستمتع بقايمة ضخمة فيها عشرات المطاعم، الكافيهات، والنوادي!</p>', unsafe_allow_html=True)

# قاعدة بيانات ضخمة وشاملة (أماكن كتير جداً لكل قسم)
database = {
    "وسط البلد (Downtown)": {
        "🍔 مطاعم ومشاوي وبرجر": [
            {"name": "برجر كنج", "type": "برجر وسريع", "rate": "⭐ 4.5", "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Burger+King+Downtown+Cairo"},
            {"name": "باستا الانسجام", "type": "مكرونة وكبدة", "rate": "⭐ 4.6", "img": "https://images.unsplash.com/photo-1621996346565-e3d5d6281298?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Makarona+El+Ensgam+Cairo"},
            {"name": "بافلو برجر", "type": "برجر مصري", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Buffalo+Burger+Downtown"},
            {"name": "كشري أبو طارق", "type": "كشري مصري أصيل", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Koshary+Abou+Tarek"},
            {"name": "مطعم جاد", "type": "فول وفلافل ومشويات", "rate": "⭐ 4.3", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Gad+Downtown+Cairo"},
            {"name": "البرنس (فرع وسط البلد)", "type": "أكل شرقي وطواجن", "rate": "⭐ 4.9", "img": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=El+Prince+Cairo"},
            {"name": "فلفلة", "type": "مأكولات مصرية تراثية", "rate": "⭐ 4.4", "img": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Felfela+Cairo"},
            {"name": "كنتاكي - طلعت حرب", "type": "دجاج مقلي وسريع", "rate": "⭐ 4.2", "img": "https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=KFC+Talaat+Harb"},
            {"name": "هاتريك", "type": "بيتزا ومخبوزات", "rate": "⭐ 4.5", "img": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Pizza+Downtown+Cairo"},
            {"name": "صب واي", "type": "ساندويتشات صحية وسريعة", "rate": "⭐ 4.4", "img": "https://images.unsplash.com/photo-1509722747041-616f39b57569?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Subway+Downtown+Cairo"}
        ],
        "☕ كافيهات وقهوة تاريخية": [
            {"name": "قهوة زهرة البستان", "type": "قهوة تاريخية وثقافية", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Zahret+Al+Bostan+Cairo"},
            {"name": "راديوم كافيه", "type": "قعدة شبابية وهادئة", "rate": "⭐ 4.4", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Downtown+Cafes+Cairo"},
            {"name": "گروبي (Groppi)", "type": "حلويات وكافيه عريق", "rate": "⭐ 4.6", "img": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Groppi+Downtown+Cairo"},
            {"name": "قهوة ريش", "type": "مقهى الأدباء والمثقفين", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Café+Riche+Cairo"},
            {"name": "سيلانترو - وسط البلد", "type": "قهوة ومذاكرة وعمل", "rate": "⭐ 4.5", "img": "https://images.unsplash.com/photo-1442512595331-e89e73853f31?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Cilantro+Downtown+Cairo"},
            {"name": "البورصة كافيه", "type": "قعدات شعبية ممتعة", "rate": "⭐ 4.3", "img": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=El+Borsa+Cafe+Cairo"},
            {"name": "إيلى كافيه", "type": "مشروبات ساخنة وعصائر", "rate": "⭐ 4.4", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Cairo+Downtown+Cafes"}
        ],
        "🍨 حلويات ومثلجات": [
            {"name": "بى لبن", "type": "أرز بلبن وإضافات", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=BLaban+Downtown+Cairo"},
            {"name": "كريسبي كريم", "type": "دونتس", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1514517521153-1be72277b32f?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Krispy+Kreme+Cairo"},
            {"name": "حلواني العبد", "type": "حلويات شرقية وغربية", "rate": "⭐ 4.9", "img": "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=El+Abd+Pasty+Downtown"}
        ],
        "🌳 نوادي وأماكن ترفيهية": [
            {"name": "حديقة الأسماك (الزمالك قريبة)", "type": "تنزه وطبيعة", "rate": "⭐ 4.4", "img": "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Aquarium+Grotto+Garden+Zamalek"},
            {"name": "ساقية الصاوي (قريبة)", "type": "حفلات وثقافة ونيل", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=El+Sawy+Culturewheel"}
        ]
    },
    "المعادي (Maadi)": {
        "🍔 مطاعم ومشاوي وبرجر": [
            {"name": "لولو كافيه ورستو", "type": "أكل عالمي", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Maadi+Restaurants"},
            {"name": "فلمنت كافيه", "type": "برجر ومشاوي", "rate": "⭐ 4.6", "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=The+Fulfillment+Maadi"},
            {"name": "بوكا", "type": "أكل إيطالي وعالمي", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Bocca+Maadi"}
        ],
        "☕ كافيهات وقهوة تاريخية": [
            {"name": "سيلانترو المعادي", "type": "قهوة ومذاكرة", "rate": "⭐ 4.6", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Cilantro+Maadi"},
            {"name": "بيبي شوب كافيه", "type": "قعدة هادئة", "rate": "⭐ 4.5", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Maadi+Cafes"}
        ],
        "🌳 نوادي وأماكن ترفيهية": [
            {"name": "نادي اليخت المصري", "type": "نادي على النيل", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Egyptian+Yacht+Club+Maadi"},
            {"name": "نادي المعادي الرياضي", "type": "نادي عريق", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Maadi+Sporting+Club"}
        ]
    }
}

# القائمة الجانبية للاختيار
st.sidebar.header("📍 حدد منطقتك المفضلة")
selected_region = st.sidebar.selectbox("اختر المنطقة:", list(database.keys()))

st.markdown(f"### 📌 قائمة الأماكن الشاملة في: **{selected_region}**")

# عرض الأماكن مقسمة بأقسام (Tabs)
region_categories = database[selected_region]
tabs = st.tabs(list(region_categories.keys()))

for index, (category_name, places_list) in enumerate(region_categories.items()):
    with tabs[index]:
        st.markdown(f"#### {category_name} (إجمالي المتوفر: {len(places_list)} مكان)")
        
        # عرض الكروت في شبكة من 3 أعمدة
        cols = st.columns(3)
        for i, place in enumerate(places_list):
            with cols[i % 3]:
                st.markdown(f"""
                    <div class="card">
                        <img src="{place['img']}" style="width:100%; height:130px; object-fit:cover; border-radius:8px; margin-bottom:8px;">
                        <h4 style="margin:5px 0; color:#2f3640; font-size:16px;">{place['name']}</h4>
                        <p style="color:#718093; font-size:12px; margin:2px 0;"><b>النوع:</b> {place['type']}</p>
                        <p style="color:#e1b12c; font-weight:bold; font-size:13px; margin:4px 0;">{place['rate']}</p>
                        <a href="{place['map']}" target="_blank" style="display:block; text-align:center; background:#00a8ff; color:white; padding:5px; border-radius:5px; text-decoration:none; font-weight:bold; font-size:13px; margin-top:8px;">📍 افتح في جوجل ماب</a>
                    </div>
                """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #b2bec3;'>تطبيق خرجني - جميع الحقوق محفوظة 2026</p>", unsafe_allow_html=True)
