	$(document).ready(function(){
		$('#list_pagination').hide();
		$('.swiper-container').hide();


			$('#area_hide').click(function(){
			    if($(".swiper-container").is(":hidden")){
			        $(".swiper-container").show();
			        $('#list_pagination').show();
			        $('#list').show();
			        $("#wrapper").css("top","180px");
			    }else{
			        $("#list").hide();
			        $(".swiper-container").hide();
			        $('#list_pagination').hide();
			        $("#wrapper").css("top","45px");
			    }
			    if ($('#menus_header').show())
			 	{
			 	$('#menus_header').hide()
			 	};
			})


			$('#search_hide').click(function(){
			    if($("#menus_header").is(":hidden")){
			        $("#menus_header").show();
			        $("#wrapper").css("top","120px");
			    }else{
			        $('#menus_header').hide();
			        $("#wrapper").css("top","45px");
			    }
				if ($('#list').show())
				 {
				 	$('#list').hide();
			        $(".swiper-container").hide();
			        $('#list_pagination').hide();
				 };
			})

	});


