(function ($) {
 "use strict";

	/*--------------------------
	menu jquery mobile code
	---------------------------- */
	$(function() {
		$('#menu').cookcodesmenu({
			brand: '<a href="index.html"><img src="images/logo.png"></a>'
		});
	});
	
/*----------------------------
 wow js active
------------------------------ */
	new WOW().init();
 
/*----------------------------
 owl active
------------------------------ */  
  $(".testimonial-area").owlCarousel({
      autoPlay: true, 
	  slideSpeed:1000,
	  pagination:true,
	  navigation:false,	  
      items : 1,
	  /* transitionStyle : "fade", */    /* [This code for animation ] */
	  navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
      itemsDesktop : [1199,1],
	  itemsDesktopSmall : [980,1],
	  itemsTablet: [768,1],
	  itemsMobile : [479,1],
  });  
  $(".total-teams").owlCarousel({
      autoPlay: true, 
	  slideSpeed:1000,
	  pagination:true,
	  navigation:false,	  
      items : 1,
	  /* transitionStyle : "fade", */    /* [This code for animation ] */
	  navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
      itemsDesktop : [1199,1],
	  itemsDesktopSmall : [980,1],
	  itemsTablet: [768,1],
	  itemsMobile : [479,1],
  }); 
  $(".home2-testimonial").owlCarousel({
      autoPlay: true, 
	  slideSpeed:1000,
	  pagination:true,
	  navigation:false,	  
      items : 2,
	  /* transitionStyle : "fade", */    /* [This code for animation ] */
	  navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
      itemsDesktop : [1199,2],
	  itemsDesktopSmall : [980,2],
	  itemsTablet: [768,1],
	  itemsMobile : [479,1],
  });

/*----------------------------
 price-slider active
------------------------------ */  
	  $( "#slider-range" ).slider({
	   range: true,
	   min: 40,
	   max: 600,
	   values: [ 60, 570 ],
	   slide: function( event, ui ) {
		$( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
	   }
	  });
	  $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
	   " - $" + $( "#slider-range" ).slider( "values", 1 ) );  
	   
/*--------------------------
 scrollUp
---------------------------- */	
	$.scrollUp({
        scrollText: '<i class="fa fa-angle-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });

	//Search trigger
	$(".search i").on("click", function(e) {
		e.stopPropagation();		
		$(".search-box").toggle("");
	});

	/*-------------------------------
	Counter Up
	---------------------------------*/
	$('.about-counter').counterUp({
		delay: 50,
		time: 3000
	});
	/*--------------------------
		Sticky Menu Activation Code
	---------------------------- */		   
	$(window).on('scroll', function(){
		if( $(window).scrollTop()>100 ){
			$('#sticky').addClass('stick');
			} else {
			$('#sticky').removeClass('stick');
		}
	});

	/*---------------------
	Circular Bars - Knob
	--------------------- */
	if(typeof($.fn.knob) != 'undefined') {
	$('.knob').each(function () {
		var $this = $(this),
			knobVal = $this.attr('data-rel');   		

		$this.knob({
		'draw' : function () {
			$(this.i).val(this.cv + '%')
		}
		});
		$this.appear(function() {
		$({
			value: 0
		}).animate({
			value: knobVal
		}, {
			duration : 2000,
			easing   : 'swing',
			step     : function () {
			$this.val(Math.ceil(this.value)).trigger('change');
			}
		});
		}, {accX: 0, accY: -150});
	});
	}

//popup video loaded js
//==========================

if ($('.popup-link').length > 0) {
	$('.popup-link').magnificPopup({
		type: 'image',
		gallery: {
					enabled: true,
					navigateByImgClick: true,
					preload: [0,1]
				},	
		});
}
if ($('.popup-youtube').length > 0) {

	$('.popup-youtube').magnificPopup({
		type: 'iframe',
		mainClass: 'mfp-fade',
		removalDelay: 160,
		preloader: false,
		fixedContentPos: false
	});
}
/*-------------------------------------
Single Product jQuery activation code
-------------------------------------*/
$(".tab-image").owlCarousel({
		// Most important owl features
		items : 3,
		itemsDesktop : [1199,3],
		itemsDesktopSmall : [980,3],
		itemsTablet: [768,2],
		itemsTabletSmall: false,
		itemsMobile : [479,1],
		singleItem : false,
		itemsScaleUp : false,
		// Navigation
		navigation : true,
		navigationText : ["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
		// Responsive 
		responsive: true,
		pagination:false,    

});
/*-------------------------------------
Single Product Tab  activation code
-------------------------------------*/
	$(".tab-image").on('click', 'li', function(event) {
			event.preventDefault();
			var displayTarget = $("#product-1");
			displayTarget.find('a').removeClass('active');
			var id = $(this).attr('data-id');
			// var targetUrl = $(this).find('a').attr('href');
			// console.log(displayTarget.html());
			var targetClass = ".product-gallery-img-"+id;
			console.log(targetClass);
			displayTarget.find(targetClass).addClass('active');
			// displayTarget.find('img').attr('src', targetUrl);
			/* Act on the event */
	});          
	/*-------------------------------------
		Related Product jQuery activation code
		-------------------------------------*/
		$(".related-product-area > .single-product-store").owlCarousel({
				// Most important owl features
					items : 3,
				itemsDesktop : [1199,3],
				itemsDesktopSmall : [980,2],
				itemsTablet: [768,1],
				itemsTabletSmall: false,
				itemsMobile : [479,1],
				singleItem : false,
				itemsScaleUp : false,
				// Navigation
				navigation : true,
				navigationText : ["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
				// Responsive
				responsive: true,
				pagination:false,
		});
		/*----------------------------
		mixitup active
		------------------------------ */  
		$('#Container').mixItUp();
//google map activation 
//----------------------------------- 
if ($('#gmap').length > 0) {
	new GMaps({
			div: '#gmap',
			lat: -37.8178945, // -37.8178945,144.9630094
			lng: 144.9630094,
			scrollwheel: false,				
			styles: [
					{
							"featureType": "landscape",
							"elementType": "geometry",
							"stylers": [
									{
											"color": "#000000"
									},
									{
											"lightness": 20
									}
							]
					},
					{
							"featureType": "road.highway",
							"elementType": "geometry.fill",
							"stylers": [
									{
											"color": "#000000"
									},
									{
											"lightness": 17
									}
							]
					},
					{
							"featureType": "road.highway",
							"elementType": "geometry.stroke",
							"stylers": [
									{
											"color": "#000000"
									},
									{
											"lightness": 29
									},
									{
											"weight": 0.2
									}
							]
					},
					{
							"featureType": "road.arterial",
							"elementType": "geometry",
							"stylers": [
									{
											"color": "#000000"
									},
									{
											"lightness": 18
									}
							]
					},
					{
							"featureType": "road.local",
							"elementType": "geometry",
							"stylers": [
									{
											"color": "#000000"
									},
									{
											"lightness": 16
									}
							]
					},
					{
							"featureType": "poi",
							"elementType": "geometry",
							"stylers": [
									{
											"color": "#000000"
									},
									{
											"lightness": 21
									}
							]
					},
					{
							"featureType": "poi.park",
							"elementType": "geometry",
							"stylers": [
									{
											"color": "#000000"
									},
									{
											"lightness": 21
									}
							]
					},
					{
							"elementType": "labels.text.stroke",
							"stylers": [
									{
											"visibility": "on"
									},
									{
											"color": "#000000"
									},
									{
											"lightness": 16
									}
							]
					},
					{
							"elementType": "labels.icon",
							"stylers": [
									{
											"visibility": "on"
									}
							]
					}
			]
	}).addMarker({
			lat: -37.8178945, // -37.8178945,144.9630094
			lng: 144.9630094,
			infoWindow: {
					content: '<p>Australia, Envato Level 13, 2 Elizabeth, St. Melbourne, Victoria 3000</p>'
			}
			});

}			


})(jQuery); 