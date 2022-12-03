function map_init(map, options) {
    // get point lat and lon
    var lon = "{{ place.location.x }}";
    var lat = "{{ place.location.y }}";
    // zoom to point & add it to map
    map.setView([lat, lon], 17);
    L.marker([lat, lon]).addTo(map);
}