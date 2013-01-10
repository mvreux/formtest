$('document').ready(function(){
	$('li.lang').click(function(){
		$('#language').val($(this).attr('langCode'));
		$(this).closest('form').submit();
	});
	
	$('#id_animal').autocomplete({ source: function(request, response){
												$.ajax({
													url: '/myform/find/animal/'+ $('#id_animal').val() + '/',
													dataType: 'json',
													processData: false,
													error: function(jqXHR, textStatus, errorThrown){
														console.log('error occured: ' + textStatus, errorThrown);
													},
													success: function (data){
														response( data );
													}
												});
								 			} 
								});
								
	$('#id_species').autocomplete({ source: function(request, response){
													$.ajax({
														url: '/myform/species/lookup/'+$('#id_species').val()+'/',
														processData: false,
														error: function(jqXHR, textStatus, errorThrown){
															console.log('error occured: '+ textStatus, errorThrown);
														},
														success: function(data){
															console.log(data);
															response( data );
														}
													});
											} 
								 });							
	
	$('#test').click(function(){
		$.ajax({
			url: '/myform/ajaxtest',
			dataType: 'text',
			processData: false,
			error: function (jqXHR, textStatus, errorThrown){
				console.log('error occured: ' + textStatus, errorThrown);
			},
			success: function (data){
				console.log('success');
				console.log(data);
			}
		})
	});
	
	initMap();
	
})
//openlayers doc: http://dev.openlayers.org/releases/OpenLayers-2.12/doc/apidocs/files/OpenLayers-js.html
function initMap(){
	var multiplePoints = false;
	
	var map = new OpenLayers.Map('map');
	var osm = new OpenLayers.Layer.OSM('OpenLayers OSM');
	var vectorLayer = new OpenLayers.Layer.Vector('Overlay');	
	
	var click = new OpenLayers.Control.Click({
			autoActivate: true,
			onClick :  function(e){
				if(!multiplePoints){
					vectorLayer.removeAllFeatures();
				}
				ll = map.getLonLatFromViewPortPx(e.xy);
				pt = new OpenLayers.Geometry.Point(ll.lon, ll.lat);
				ft = new OpenLayers.Feature.Vector(
					pt,
					{},
					{
						externalGraphic: staticUrl + 'images/marker-azure.png', 
						graphicHeight:24, 
						graphicWidth:24, 
						graphicYOffset:-24
					}
				);
				vectorLayer.addFeatures(ft);
			},
	});
	
	var drag = new OpenLayers.Control.DragFeature(
		vectorLayer,
		{
			autoActivate: true,
			onComplete: function(draggedFeature){ 
				//do stuff after drag and drop
				//console.log(draggedFeature.geometry.getBounds().getCenterLonLat());
			}
		}
	);
	
	map.addControl(click);
	map.addControl(drag);
	map.addLayers([osm, vectorLayer]);
	map.zoomToMaxExtent();
	
}

OpenLayers.Control.Click = OpenLayers.Class(OpenLayers.Control, {                
    defaultHandlerOptions: {
        'single': true,
        'double': false,
        'pixelTolerance': 0,
        'stopSingle': false,
        'stopDouble': false
    },

    initialize: function(options) {
        this.handlerOptions = OpenLayers.Util.extend(
            {}, this.defaultHandlerOptions
        );
        OpenLayers.Control.prototype.initialize.apply(
            this, arguments
        ); 
        this.handler = new OpenLayers.Handler.Click(
            this, {
                'click': this.onClick,
                'dblclick': this.onDblclick 
            }, this.handlerOptions
        );
    }, 

    onClick: function(evt) {
        //console.log('click!');
    },

    onDblclick: function(evt) {  
       // console.log('dblclick!');
    }   

});

