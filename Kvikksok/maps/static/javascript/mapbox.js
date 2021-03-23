
mapboxgl.accessToken = 'pk.eyJ1Ijoic2t1cDI1MDYiLCJhIjoiY2trMnJidzJkMTNyaDJvdDdrMmpuODR1biJ9.UozLDX9kk8-CC4irjB1nNQ';//access token
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/skup2506/ckl8epxj02oyt17s1vb1ghpnn',  //mapbox style URL
    center: [10.404, 63.417],
    zoom: 12
});

//AJAX setup
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue =   decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
// $.ajaxSetup({
//     beforeSend: function (xhr, settings) {
//         if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
//             xhr.setRequestHeader("X-CSRFToken", "{{ form.csrf_token._value() }}")
//         }
//     }
// })
//AJAX REQUEST
function ajaxRequest() {
    $.ajax({
        type: 'POST',
        url: "addMarker/",
        success: function(result){
        console.log('PONG')
        },
        error : function (xmlHttpRequest, textStatus, errorThrown) {
            console.log(errorThrown);
        }
    });
}

function addDataLayer(){
   const geoleire = JSON.parse(kvikkleireGeojson);
    map.addSource('kvikkleire',{
        type: 'geojson',
        data: geoleire
    });
    map.addLayer({
        id: 'fareOmrade',
        type: 'fill',
        source: 'kvikkleire',
        paint: {
        'fill-opacity': ['/',1.2,['get', 'skredrisik']],
        'fill-color':'#ff0000',
        },
      });
      map.on('click', 'fareOmrade', function(e) {
         new mapboxgl.Popup()
         .setLngLat(e.lngLat)
         .setHTML("Skredrisikoen i heltaltsformat er " + e.features[0].properties.skredrisik)
         .addTo(map);
      });
      map.on('mouseenter', 'fareOmrade', function() {
         map.getCanvas().style.cursor = 'pointer';
      });
}

map.on("load", () => {
    addDataLayer();
});




var coordinatesGeocoder = function (query) {
    // match anything which looks like a decimal degrees coordinate pair
       var matches = query.match(
          /^[ ]*(?:Lat: )?(-?\d+\.?\d*)[, ]+(?:Lng: )?(-?\d+\.?\d*)[ ]*$/i
       );
       if (!matches) {
          return null;
       }
       
       function coordinateFeature(lng, lat) {
          return {
             center: [lng, lat],
             geometry: {
                type: 'Point',
                coordinates: [lng, lat]
             },
             place_name: 'Lat: ' + lat + ' Lng: ' + lng,
             place_type: ['coordinate'],
             properties: {},
             type: 'Feature'
          };
       }
       
       var coord1 = Number(matches[1]);
       var coord2 = Number(matches[2]);
       var geocodes = [];
       
       if (coord1 < -90 || coord1 > 90) {
       // must be lng, lat
          geocodes.push(coordinateFeature(coord1, coord2));
       }
       
       if (coord2 < -90 || coord2 > 90) {
       // must be lat, lng
          geocodes.push(coordinateFeature(coord2, coord1));
       }
       
       if (geocodes.length === 0) {
       // else could be either lng, lat or lat, lng
          geocodes.push(coordinateFeature(coord1, coord2));
          geocodes.push(coordinateFeature(coord2, coord1));
       }
       
       return geocodes;
};
    
map.addControl(
       new MapboxGeocoder({
          accessToken: mapboxgl.accessToken,
          localGeocoder: coordinatesGeocoder,
          zoom: 4,
          placeholder: 'Stedsnavn/Koordinater',
          mapboxgl: mapboxgl
       })
);

//NavigationControl
var nav = new mapboxgl.NavigationControl();
var addmarker_boolen = false; 
map.addControl(nav, 'top-left');


//allows user to add a marker
document.getElementById("nyttPunkt").onclick = function() {addMarker()};
function addMarker() {
    
    addmarker_boolen = true;
    console.log('addmarker is ' + addmarker_boolen)
}

//Show usermarkers from database
document.getElementById("showMarkers").onclick = function() {showMarker()};
function showMarker() {
    const geojsonParsed = JSON.parse(geojson);
    geojsonParsed.features.forEach(function(marker)  {

        // create a HTML element for each feature
        //var el = document.createElement('div');
        //el.className = 'marker';

        // make a marker for each feature and add to the map
        new mapboxgl.Marker()
            .setLngLat(marker.geometry.coordinates)
            .setPopup(
                new mapboxgl.Popup({ offset: 25 }) // add popups
                .setMaxWidth('none')
                .setHTML(
                '<h6>' +
                marker.properties.title +
                '</h6><p>' +
                marker.properties.content +
                '</p><p align="right" style="font-size:80%;">' +
                marker.properties.date_posted +
                '</p>'
                )
                )
            .addTo(map);
    });
	console.log(geojsonParsed);

	
}


//MapMouseEvent and marker
map.on('click', function(e) {
  if (addmarker_boolen == true) {
    
    
	var div = window.document.createElement('div');
    //div.innerHTML
    //var html_data = '<form method="POST">{{% csrf_token %}}<table>{{ form.as_table }}</table><button class="btn btn-outline-info" type="submit">Sign Up</button></div></form>';
	var msgtitle = window.document.createElement("input");
	msgtitle.setAttribute("id", "msgtitle");
	var textarea = window.document.createElement("textarea");
	textarea.setAttribute("rows", "5");
	textarea.setAttribute("cols", "30");
	textarea.setAttribute("name", "textmsg");
	textarea.setAttribute("id", "msg");
	var submit = window.document.createElement("input");
	submit.setAttribute("type", "submit");
	submit.setAttribute("id", "submit");
	submit.setAttribute("value", "Send melding");
	submit.addEventListener("click", () => {
        console.log(msgtitle.value);
        console.log(textarea.value);
        ajaxRequest();
    })
	div.appendChild(msgtitle);
	div.appendChild(textarea);
	div.appendChild(submit);
	
    
	var marker = new mapboxgl.Marker({
			color: '#004fa4',
			draggable: true
		})
		.setLngLat([e.lngLat.lng, e.lngLat.lat])
		.setPopup(
			new mapboxgl.Popup()
		    .setDOMContent(div))
            //.setHTML(html_data))
		.addTo(map);
        marker.togglePopup();
    
    addmarker_boolen = false;                
  }
});

    




