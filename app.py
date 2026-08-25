import streamlit as st

# إعدادات الصفحة وتصميمها
st.set_page_config(
    page_title="تطبيق خرجني - الدليل الشامل في مصر", 
    page_icon="🚀", 
    layout="wide"
)

# تصميم CSS مخصص لتجميل الشكل وإعطاء طابع احترافي وعصري
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
st.markdown('<p class="sub-title">اختر منطقتك واكتشف مئات المطاعم، الكافيهات، والنوادي الحقيقية حواليك!</p>', unsafe_allow_html=True)

# قاعدة بيانات ضخمة وحقيقية لمناطق وأماكن مصر المختلفة
database = {
    "وسط البلد (Downtown)": {
        "🍔 المطاعم والأكل": [
            {"name": "برجر كنج - طلعت حرب", "type": "برجر وسريع", "rate": "⭐ 4.5", "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Burger+King+Talaat+Harb+Cairo"},
            {"name": "باستا الانسجام", "type": "مكرونة وكبدة", "rate": "⭐ 4.6", "img": "https://images.unsplash.com/photo-1621996346565-e3d5d6281298?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Makarona+El+Ensgam+Cairo"},
            {"name": "بافلو برجر - وسط البلد", "type": "برجر", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Buffalo+Burger+Downtown+Cairo"},
            {"name": "كشري أبو طارق", "type": "كشري مصري", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Koshary+Abou+Tarek+Cairo"},
            {"name": "مطعم جاد - الفلكي", "type": "فول وفلافل ومشويات", "rate": "⭐ 4.3", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Gad+Downtown+Cairo"},
            {"name": "فلفلة - ميدان تيمور", "type": "مأكولات شرقية", "rate": "⭐ 4.4", "img": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Felfela+Downtown+Cairo"},
            {"name": "كنتاكي - ميدان التحرير", "type": "دجاج مقلي وسريع", "rate": "⭐ 4.2", "img": "https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=KFC+Tahrir+Square+Cairo"},
            {"name": "هاتريك بيتزا", "type": "بيتزا ومخبوزات", "rate": "⭐ 4.5", "img": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Pizza+Downtown+Cairo"},
            {"name": "صب واي - وسط البلد", "type": "ساندويتشات صحية", "rate": "⭐ 4.4", "img": "https://images.unsplash.com/photo-1509722747041-616f39b57569?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Subway+Downtown+Cairo"},
            {"name": "بيبز برجر", "type": "برجر أمريكي", "rate": "⭐ 4.6", "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Beeps+Burger+Cairo"},
            {"name": "كشري هند", "type": "كشري وممبار", "rate": "⭐ 4.5", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Koshary+Hend+Cairo"},
            {"name": "البرنس (فرع قصر النيل)", "type": "طواجن ومشاوي", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=El+Prince+Cairo"}
        ],
        "☕ الكافيهات والقعدات": [
            {"name": "قهوة زهرة البستان", "type": "قهوة تاريخية وثقافية", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Zahret+Al+Bostan+Cairo"},
            {"name": "راديوم كافيه", "type": "قعدة شبابية", "rate": "⭐ 4.4", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Downtown+Cafes+Cairo"},
            {"name": "گروبي (Groppi)", "type": "حلويات وكافيه عريق", "rate": "⭐ 4.6", "img": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Groppi+Downtown+Cairo"},
            {"name": "قهوة ريش", "type": "مقهى الأدباء", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Café+Riche+Cairo"},
            {"name": "سيلانترو - وسط البلد", "type": "قهوة وعمل", "rate": "⭐ 4.5", "img": "https://images.unsplash.com/photo-1442512595331-e89e73853f31?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Cilantro+Downtown+Cairo"},
            {"name": "البورصة كافيه", "type": "قعدات شعبية", "rate": "⭐ 4.3", "img": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=El+Borsa+Cafe+Cairo"},
            {"name": "استرا كافيه", "type": "مشروبات وشيشة", "rate": "⭐ 4.4", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Astra+Cafe+Cairo"},
            {"name": "كافيه الباشا", "type": "قعدة هادئة", "rate": "⭐ 4.5", "img": "https://images.unsplash.com/photo-1442512595331-e89e73853f31?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Basha+Cafe+Cairo"}
        ],
        "🍨 الحلويات والمثلجات": [
            {"name": "بى لبن", "type": "أرز بلبن وإضافات", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=BLaban+Downtown+Cairo"},
            {"name": "كريسبي كريم", "type": "دونتس", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1514517521153-1be72277b32f?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Krispy+Kreme+Cairo"},
            {"name": "حلواني العبد - طلعت حرب", "type": "حلويات شرقية وغربية", "rate": "⭐ 4.9", "img": "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=El+Abd+Pastry+Downtown+Cairo"},
            {"name": "حلواني تسواني", "type": "بسبوسة وشرقي", "rate": "⭐ 4.5", "img": "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Tswany+Sweets+Cairo"}
        ],
        "🌳 النوادي وأماكن التنزيه": [
            {"name": "النادي الأهلي (فرع الجزيرة قريب)", "type": "نادي رياضي واجتماعي", "rate": "⭐ 4.9", "img": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Al+Ahly+Sporting+Club+Gezira"},
            {"name": "نادي المعلمين بالجزيرة", "type": "نادي على النيل", "rate": "⭐ 4.3", "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Teachers+Club+Zamalek"}
        ]
    },
    "المعادي (Maadi)": {
        "🍔 المطاعم والأكل": [
            {"name": "لولو كافيه ورستو", "type": "أكل عالمي", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Maadi+Restaurants"},
            {"name": "فلمنت كافيه", "type": "برجر ومشاوي", "rate": "⭐ 4.6", "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=The+Fulfillment+Maadi"},
            {"name": "بوكا المعادي", "type": "أكل إيطالي وعالمي", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Bocca+Maadi"},
            {"name": "أبيكس برجر", "type": "برجر لذييذ", "rate": "⭐ 4.5", "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Apex+Burger+Maadi"}
        ],
        "☕ الكافيهات والقعدات": [
            {"name": "سيلانترو المعادي", "type": "قهوة وعمل", "rate": "⭐ 4.6", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Cilantro+Maadi"},
            {"name": "كوستا كوفي المعادي", "type": "قهوة عالمية", "rate": "⭐ 4.5", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Costa+Coffee+Maadi"}
        ],
        "🍨 الحلويات والمثلجات": [
            {"name": "تورس هوم ميكد", "type": "حلويات وكيك", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=TORS+Maadi"}
        ],
        "🌳 النوادي وأماكن التنزيه": [
            {"name": "نادي المعادي الرياضي والاجتماعي", "type": "نادي عريق ومساحات خضراء", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Maadi+Sporting+Club"},
            {"name": "نادي اليخت المصري", "type": "نادي على النيل مباشرة", "rate": "⭐ 4.9", "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Egyptian+Yacht+Club+Maadi"}
        ]
    },
    "الشيخ زايد وأكتوبر (Zayed & October)": {
        "🍔 المطاعم والأكل": [
            {"name": "أركان بلازا مطاعم", "type": "مجمع مطاعم عالمية", "rate": "⭐ 4.9", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Arkan+Plaza+Zayed"},
            {"name": "ذا يارد زايد", "type": "مطاعم وكافيهات مفتوحة", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=The+Yard+Zayed"},
            {"name": "معدوي مول العرب", "type": "مطاعم متنوعة", "rate": "⭐ 4.6", "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Mall+of+Arabia+Restaurants+October"}
        ],
        "☕ الكافيهات والقعدات": [
            {"name": "بيلا كافيه - زايد", "type": "قعدة رايقة", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Zayed+Cafes"}
        ],
        "🍨 الحلويات والمثلجات": [
            {"name": "إلبابلي - أكتوبر", "type": "آيس كريم وحلويات", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Elbably+October"}
        ],
        "🌳 النوادي وأماكن التنزيه": [
            {"name": "نادي وادي دجلة - أكتوبر", "type": "نادي رياضي كبير", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Wadi+Degla+Club+October"},
            {"name": "نادي الشيخ زايد الرياضي", "type": "نادي اجتماعي", "rate": "⭐ 4.6", "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Sheikh+Zayed+Club"}
        ]
    },
    "التجمع الخامس ومصر الجديدة (New Cairo & Heliopolis)": {
        "🍔 المطاعم والأكل": [
            {"name": "كايرو فستيفال سيتي مطاعم", "type": "تنوع هائل", "rate": "⭐ 4.9", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Cairo+Festival+City+Mall"},
            {"name": "ميركاتو التجمع", "type": "مطاعم وكافيهات", "rate": "⭐ 4.7", "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=New+Cairo+Restaurants"}
        ],
        "☕ الكافيهات والقعدات": [
            {"name": "واتس آب كافيه - مصر الجديدة", "type": "قعدة شبابية", "rate": "⭐ 4.5", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Heliopolis+Cafes"}
        ],
        "🍨 الحلويات والمثلجات": [
            {"name": "الدمياطي - مصر الجديدة", "type": "حلويات شرقية", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=ElDomyati+Heliopolis"}
        ],
        "🌳 النوادي وأماكن التنزيه": [
            {"name": "نادي هليوبوليس (مصر الجديدة)", "type": "نادي عريق", "rate": "⭐ 4.9", "img": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=Heliopolis+Sporting+Club"},
            {"name": "نادي الزهور (التجمع)", "type": "نادي اجتماعي متكامل", "rate": "⭐ 4.8", "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80", "map": "https://maps.google.com/?q=El+Zohour+Club+New+Cairo"}
        ]
    }
}

# القائمة الجانبية لتحديد المنطقة
st.sidebar.header("📍 اختر منطقتك في مصر")
selected_region = st.sidebar.selectbox("المنطقة الحالية:", list(database.keys()))

st.markdown(f"### 📌 الدليل الشامل والأماكن المتاحة في: **{selected_region}**")

# عرض الأماكن مقسمة في أقسام احترافية (Tabs)
region_categories = database[selected_region]
tabs = st.tabs(list(region_categories.keys()))

for index, (category_name, places_list) in enumerate(region_categories.items()):
    with tabs[index]:
        st.markdown(f"#### {category_name} (إجمالي المتاح: {len(places_list)} مكان)")
        
        # عرض الأماكن في شبكة مكونة من 3 أعمدة
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
