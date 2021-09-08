window.addEventListener("DOMContentLoaded", function () {
  // Coordinates, in case location is not available
  map_center = [40.771141, -111.900237];
  // Get the users location if permitted - they will be asked for permission before we can get their location
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (position) {
      map_center = [position.coords.longitude, position.coords.latitude];
    });
  }

  var map = new atlas.Map("myMap", {
    authOptions: {
      authType: "subscriptionKey",
      subscriptionKey: "{{ map_key }}",
    },
  });

  // when the map is ready, center the map on the users location
  map.events.add("ready", function () {
    // Declare a data source for the AQI data
    var datasource = new atlas.source.DataSource();
    map.sources.add(datasource);

    // Declare a function to update the AQI data
    function updateAQIData(e) {
      // Get the current bounds on screen
      bounds = map.getCamera().bounds;

      // Set the data source data to results of the aqi call
      // This is a feature collection with the AQI measurements
      fetch("./aqi?bounds=" + bounds)
        .then((res) => {
          return res.json();
        })
        .then((response) => {
          datasource.clear();
          datasource.setShapes(response);
        });
    }

    // Add a bubble layer
    map.layers.add(
      new atlas.layer.BubbleLayer(datasource, null, {
        radius: 10,
        opacity: 0.5,
        strokeOpacity: 0,
        // Get the color from the color property
        color: ["get", "color"],
      })
    );

    // Handle any events that change the bounds of the map
    map.events.add("zoomend", updateAQIData);
    map.events.add("dragend", updateAQIData);
    map.events.add("pitchend", updateAQIData);

    map.setCamera({
      center: map_center,
      zoom: 5,
    });
  });
});
