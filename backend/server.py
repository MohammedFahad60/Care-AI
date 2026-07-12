from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/doctors", methods=["POST"])
def doctors():
    spec = request.json.get("specialty", "Hospital")
    lat = request.json.get("lat")
    lon = request.json.get("lon")
    loc = request.json.get("location")
    results = []
    center = None

    # CASE 1: User provides GPS coordinates
    if lat and lon:
        center = {"lat": lat, "lon": lon}
    # CASE 2: User provides location text → convert to coordinates
    elif loc:
        geo_res = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": loc, "format": "json", "limit": 1}
        ).json()
        if geo_res:
            center = {"lat": float(geo_res[0]["lat"]), "lon": float(geo_res[0]["lon"])}
            lat, lon = center["lat"], center["lon"]

    if center:
        # Query Overpass API for nearby hospitals/clinics/doctors
        q = f"""
        [out:json];
        (
          node["amenity"~"hospital|clinic|doctors|pharmacy"](around:10000,{lat},{lon});
        );
        out center;
        """
        r = requests.get("http://overpass-api.de/api/interpreter", params={"data": q}, timeout=15)
        if r.status_code == 200:
            for el in r.json().get("elements", [])[:15]:
                results.append({
                    "name": el.get("tags", {}).get("name", "Clinic"),
                    "address": el.get("tags", {}).get("addr:full", "Nearby"),
                    "lat": el.get("lat"),
                    "lon": el.get("lon")
                })

    return jsonify({"center": center, "result": results})
