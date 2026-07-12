let userLat = null;
let userLon = null;

function getMyLocation() {
  if (!navigator.geolocation) return alert("Geolocation not supported.");
  navigator.geolocation.getCurrentPosition(
    (pos) => {
      userLat = pos.coords.latitude;
      userLon = pos.coords.longitude;
      document.getElementById("d-loc").value = "Current Location";
      findDocs();
    },
    () => alert("Failed to get location."),
    { enableHighAccuracy: true, timeout: 10000 }
  );
}

async function findDocs() {
  const spec = document.getElementById("d-spec").value || "hospital";
  const locInput = document.getElementById("d-loc").value;

  if (!locInput && !userLat) return alert("Enter a location or use GPS.");

  const list = document.getElementById("d-list");
  list.innerHTML = "Searching...";

  try {
    const res = await fetch("/doctors", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        specialty: spec,
        location: locInput,
        lat: userLat,
        lon: userLon,
      }),
    });

    const data = await res.json();
    list.innerHTML = "";
    if (data.result.length > 0) {
      data.result.forEach((doc) => {
        const div = document.createElement("div");
        div.innerHTML = `<strong>${doc.name}</strong> - ${doc.address}`;
        div.onclick = () => updateMap(doc.lat, doc.lon);
        list.appendChild(div);
      });
      // Center map to first result
      updateMap(data.result[0].lat, data.result[0].lon);
    } else {
      list.innerHTML = "No results found.";
    }
  } catch {
    list.innerHTML = "Error fetching data.";
  }
}

function updateMap(lat, lon) {
  document.getElementById("gmap-frame").src =
    `https://maps.google.com/maps?q=${lat},${lon}&z=15&output=embed`;
}
