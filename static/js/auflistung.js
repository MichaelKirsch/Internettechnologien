

var map = L.map('mapid').setView([47.721053, 10.307946], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var marker = L.marker([47.721053, 10.307946])//.addTo(map)



function onMapClick(e){
    marker.setLatLng(e.latlng)
    marker.addTo(map)
    document.getElementById("akt_position").innerHTML = "Aktuell gewählt | Lat:"+e.latlng.lat + " Lon:" +e.latlng.lng
    console.log(e.latlng)
}



map.on('click', onMapClick)


var data = ['{{ data|tojson }}'];

console.log(data)