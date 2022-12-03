const attribution =
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
const map = L.map("map");
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: attribution,
}).addTo(map);
map.setView([ 107.7890657186508, 51.781435272554496], 17);
L.marker([ 107.7890657186508, 51.781435272554496]).addTo(map);
map.fitWorld();