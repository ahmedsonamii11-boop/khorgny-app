import streamlit as st

st.set_page_config(page_title="تطبيق خرجني", page_icon="🚀", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #ff4757;'>🚀 خرجني - اقتراحات الخروجات الذكية</h1>
    <p style='text-align: center; color: #555;'>اختار خروجتك وتعرف على أحسن الأماكن حواليك وارتبط بجوجل ماب مباشرة!</p>
""", unsafe_allow_html=True)

st.markdown("---")

# اختيار المنطقة أو الموقع
location = st.selectbox("اختر المنطقة أو القرب الجغرافي:", ["وسط البلد (Downtown)", "القاهرة الكبرى", "أماكن عامة"])

st.subheader(f"📍 الأماكن المقترحة في: {location}")

# داتا الأماكن
places = [
    {
        "name": "زهرة البستان", 
        "type": "كافيه وقهوة تاريخية", 
        "img": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=600&q=80", 
        "map": "https://maps.google.com/?q=Zahret+Al+Bostan+Cairo"
    },
    {
        "name": "برجر كنج - وسط البلد", 
        "type": "مطعم برجر وسريع", 
        "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80", 
        "map": "https://maps.google.com/?q=Burger+King+Downtown+Cairo"
    },
    {
        "name": "كشري هند الأصلي", 
        "type": "كشري مصري أصيل", 
        "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=600&q=80", 
        "map": "https://maps.google.com/?q=Koshary+Hend+Cairo"
    }
]

# عرض الأماكن في كروت منظمة
for place in places:
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(place["img"], width=150)
        with col2:
            st.markdown(f"### {place['name']}")
            st.write(f"**النوع:** {place['type']}")
            st.markdown(f"[📍 افتح في جوجل ماب]({place['map']})", unsafe_allow_html=True)
        st.markdown("---")
