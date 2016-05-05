	$(document).ready(function(){
		$('#list_pagination').hide();
		$('.swiper-container').hide();



		$('#area_hide').click(function(){
			$('#list_pagination').toggle();
			if ($('#menus_header').show())
			 {
			 	$('#menus_header').hide()
			 };

			 $('#list').toggle();
			if ($('#menus_header').show())
			 {
			 	$('#menus_header').hide()
			 };

			$('.swiper-container').toggle();
			if ($('#menus_header').show())
			 {
			 	$('#menus_header').hide()
			 };
		});
		

		$('#search_hide').click(function(){
			$('#menus_header').toggle();
			if ($('#list').show())
			 {
			 	$('#list').hide()
			 };
			 if ($('.swiper-container').show())
			 {
			 	$('.swiper-container').hide()
			 };
			 if ($('#list_pagination').show())
			 {
			 	$('#list_pagination').hide()
			 };
		})
	});


