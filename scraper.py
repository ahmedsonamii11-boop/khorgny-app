import json

# دي الداتا الضخمة اللي الكود هيسحبها ويحطها في التطبيق
huge_master_database = {
  "القاهرة": {
    "وسط البلد": {
      "🍔 مطاعم وكشري ومشويات": [
        {"name": "البرنس", "rating": "⭐ 4.6", "desc": "أشهر مطعم كبدة ومسقعة.", "dist": "1.2 كم", "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80", "map": "El+Prince+Agouza"},
        {"name": "ابو طارق", "rating": "⭐ 4.7", "desc": "ملك الكشري المصري الأصيل.", "dist": "0.8 كم", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=600&q=80", "map": "Abu+Tarek+Cairo"},
        {"name": "كشري التحرير", "rating": "⭐ 4.5", "desc": "طعم كشري أصلي وساخن.", "dist": "1.0 كم", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=600&q=80", "map": "Koshary+El+Tahrir"}
      ],
      "☕ كافيهات وقهاوي تراثية": [
        {"name": "قهوة الفشاوي", "rating": "⭐ 4.7", "desc": "قعدة عريقة وأصيلة في خان الخليلي.", "dist": "1.5 كم", "img": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", "map": "El+Fishawy+Khan+El+Khalili"}
      ]
    },
    "التجمع الخامس": {
      "🍔 مطاعم وكشري ومشويات": [
        {"name": "بازوكة", "rating": "⭐ 4.3", "desc": "وجبات فراخ مقرمشة وسريعة.", "dist": "2.0 كم", "img": "https://images.unsplash.com/photo-1561758033-d89a9ad46330?auto=format&fit=crop&w=600&q=80", "map": "Bazooka+New+Cairo"}
      ]
    }
  }
}

# هنا الكود بيكتب الداتا جوه ملف places.json
with open("places.json", "w", encoding="utf-8") as f:
    json.dump(huge_master_database, f, ensure_ascii=False, indent=2)

print("تم تحديث ملف places.json بنجاح يا فنان!")