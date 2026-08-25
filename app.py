from flask import Flask, render_template_string

app = Flask(__name__)

# قالب صفحة الويب اللي بيحدد الموقع ويقترح الأماكن ويربطها بجوجل ماب
html_template = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تطبيق خرجني - اقتراحات الخروجات الذكية</title>
    <style>
        body { font-family: 'Cairo', Arial, sans-serif; background: #f8f9fa; margin: 0; padding: 20px; color: #333; text-align: center; }
        h1 { color: #ff4757; }
        .btn-container { margin: 20px 0; }
        button { background: #ff4757; color: white; border: none; padding: 12px 24px; font-size: 16px; border-radius: 8px; cursor: pointer; font-weight: bold; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: 0.3s; }
        button:hover { background: #e84118; }
        .places-grid { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 20px; }
        .card { background: white; border-radius: 12px; width: 280px; box-shadow: 0 4px 10px rgba(0,0,0,0.08); overflow: hidden; text-align: right; }
        .card img { width: 100%; height: 150px; object-fit: cover; }
        .card-content { padding: 15px; }
        .card-title { font-size: 18px; font-weight: bold; margin-bottom: 5px; color: #2f3640; }
        .card-desc { font-size: 14px; color: #718093; margin-bottom: 10px; }
        .map-link { display: inline-block; background: #00a8ff; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-size: 14px; font-weight: bold; }
        .map-link:hover { background: #0097e6; }
    </style>
</head>
<body>

    <h1>🚀 خرجني - اختار خروجتك حسب مكانك</h1>
    <p>دوس على زرار تحديد الموقع عشان نقترح عليك أحسن الأماكن حواليك!</p>

    <div class="btn-container">
        <button onclick="getLocation()">📍 حدد موقعي الحالي</button>
    </div>

    <div id="status" style="font-weight: bold; color: #e1b12c; margin: 15px 0;"></div>

    <div class="places-grid" id="placesContainer"></div>

    <script>
        const database = {
            "Downtown": [
                {name: "زهرة البستان", type: "كافيه وقهوة تاريخية", img: "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=600&q=80", map: "https://maps.google.com/?q=Zahret+Al+Bostan+Cairo"},
                {name: "برجر كنج - وسط البلد", type: "مطعم برجر وسريع", img: "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80", map: "https://maps.google.com/?q=Burger+King+Downtown+Cairo"},
                {name: "كشري هند الأصلي", type: "كشري مصري أصيل", img: "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=600&q=80", map: "https://maps.google.com/?q=Koshary+Hend+Cairo"}
            ],
            "General": [
                {name: "سيلفر ساندس / كافيهات متنوعة", type: "قعدات رواق وكافيهات", img: "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=600&q=80", map: "https://maps.google.com/?q=Cafes+Near+Me"},
                {name: "مطاعم المشويات الكبرى", type: "مشويات وطيور وطواجن", img: "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80", map: "https://maps.google.com/?q=Grills+Near+Me"}
            ]
        };

        function getLocation() {
            const statusDiv = document.getElementById("status");
            if (navigator.geolocation) {
                statusDiv.innerHTML = "جاري تحديد موقعك عبر الأقمار الصناعية...";
                navigator.geolocation.getCurrentPosition(
                    (position) => {
                        statusDiv.innerHTML = `تم تحديد موقعك بنجاح! جبنالك أحسن الأماكن القريبة:`;
                        displayPlaces(database["Downtown"]); 
                    },
                    (error) => {
                        statusDiv.innerHTML = "تعذر تحديد الموقع تلقائياً، دي أقوى المقترحات المتاحة:";
                        displayPlaces(database["General"]);
                    }
                );
            } else {
                statusDiv.innerHTML = "متصفحك لا يدعم تحديد الموقع الجغرافي.";
                displayPlaces(database["General"]);
            }
        }

        function displayPlaces(places) {
            const container = document.getElementById("placesContainer");
            container.innerHTML = "";
            places.forEach(place => {
                const card = document.createElement("div");
                card.className = "card";
                card.innerHTML = `
                    <img src="${place.img}" alt="${place.name}">
                    <div class="card-content">
                        <div class="card-title">${place.name}</div>
                        <div class="card-desc">${place.type}</div>
                        <a href="${place.map}" target="_blank" class="map-link">📍 افتح في جوجل ماب</a>
                    </div>
                `;
                container.appendChild(card);
            });
        }

        window.onload = function() {
            displayPlaces(database["Downtown"]);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)
