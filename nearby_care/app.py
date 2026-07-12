from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/doctors", methods=["POST"])
def doctors():
    data = request.json
    specialty = data.get("specialty", "hospital")
    lat = data.get("lat")
    lon = data.get("lon")
    location_text = data.get("location", "")

    results = []

    # ✅ Use Google Places API if GPS coordinates are available
    if lat and lon:
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {
            "key": GOOGLE_API_KEY,
            "location": f"{lat},{lon}",
            "radius": 10000,
            "keyword": specialty
        }


        r = requests.get(url, params=params)
        print(r.json())  # Debugging

        if r.status_code == 200:
            places = r.json().get("results", [])[:15]
            for p in places:
                results.append({
                    "name": p.get("name"),
                    "address": p.get("vicinity", "Address not available"),
                    "lat": p["geometry"]["location"]["lat"],
                    "lon": p["geometry"]["location"]["lng"],
                    "rating": p.get("rating", "N/A")
                })
    # ❌ Fallback: If no GPS, just return empty for now
    return jsonify({"result": results})

if __name__ == "__main__":
    app.run(debug=True)
