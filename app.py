import streamlit as st
import json
import os

st.set_page_config(
    page_title="خرجني | الدليل الشامل",
    page_icon="🗺️",
    layout="wide"
)

# تنسيق الشاشة
st.markdown("""
<style>
    .stApp { background: #07090e; color: #f1f5f9; font-family: 'Cairo', sans-serif; }
    .place-card {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 16px;
        overflow: hidden;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }
    .badge-rating {
        background: #1e3a8a;
        color: #93c5fd;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# دالة قراءة الملف الخارجي
def load_data():
    if os.path.exists("places.json"):
        with open("places.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# تحميل البيانات في كل مرة للتحديث الفوري
egypt_master_db = load_data()

st.markdown("<h1 style='text-align: center; color: #3b82f6;'>🗺️ تطبيق خرجني - النسخة الاحترافية</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; margin-bottom: 30px;'>دليلك الشامل لكل الأماكن في مصر (مطاعم، كافيهات، حدائق، وحلويات)</p>", unsafe_allow_html=True)

if not egypt_master_db:
    st.error("⚠️ لم يتم العثور على ملف places.json أو الملف فارغ!")
else:
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_gov = st.selectbox("📍 اختر المحافظة:", list(egypt_master_db.keys()))

    with col2:
        available_areas = list(egypt_master_db[selected_gov].keys())
        selected_area = st.selectbox("🏙️ اختر المنطقة/الحي:", available_areas)

    with col3:
        categories = list(egypt_master_db[selected_gov][selected_area].keys())
        selected_category = st.selectbox("🎯 التصنيف:", categories)

    st.markdown("---")
    
    # محرك بحث حر
    search_query = st.text_input("🔍 ابحث عن اسم مكان معين (مثال: البرنس، بلبن، الفشاوي..):", "")

    current_list = egypt_master_db[selected_gov][selected_area].get(selected_category, [])

    if search_query:
        current_list = [p for p in current_list if search_query.lower() in p['name'].lower()]

    st.subheader(f"📋 النتائج المتاحة في ({selected_gov} ← {selected_area}):")

    if not current_list:
        st.warning("⚠️ عذراً، لا توجد نتائج مطابقة لبحثك في هذه المنطقة حالياً.")
    else:
        for place in current_list:
            maps_url = f"https://www.google.com/maps/search/?api=1&query={place['map']}"
            st.markdown(f"""
            <div class="place-card">
                <div style="display: flex; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 220px; max-width: 260px;">
                        <img src="{place['img']}" style="width: 100%; height: 180px; object-fit: cover;" />
                    </div>
                    <div style="flex: 2; padding: 20px; display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                                <h3 style="margin: 0; color: #60a5fa; font-size: 1.25rem;">{place['name']}</h3>
                                <span class="badge-rating">{place['rating']}</span>
                            </div>
                            <p style="margin: 0 0 12px 0; color: #cbd5e1; font-size: 0.95rem;">{place['desc']}</p>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 12px;">
                            <span style="color: #34d399; font-size: 0.85rem; font-weight: 600;">📍 المسافة التقريبية: {place['dist']}</span>
                            <a href="{maps_url}" target="_blank" style="background: #2563eb; color: white; padding: 7px 16px; border-radius: 8px; text-decoration: none; font-size: 0.85rem; font-weight: bold;">🗺️ افتح خريطة جوجل</a>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)