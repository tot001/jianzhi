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





// window.onscroll=function(){

// };





window.onload=function()
{
	var suspension=document.getElementById('suspension');
	var timer=null;
	
	suspension.style.top=parseInt(document.documentElement.clientHeight/1.2)+"px";
	
	function startMove(iTarget)
	{
			
			clearInterval(timer);
			timer=setInterval(function(){
				var speed=(iTarget-suspension.offsetTop)/5;
				speed=speed>0?Math.ceil(speed):Math.floor(speed);

				if (suspension.offsetTop==iTarget)
				 {
				 	clearInterval(timer);
				 }
				 else
				 {
				 	suspension.style.top=suspension.offsetTop+speed+"px";
				 }
			},30)
	};

	suspension.onclick=function()
	{
		document.documentElement.scrollTop = document.body.scrollTop = 0;
	};


//加载
function getScrollTop(){
	var scrollTop_2=0;
	if (document.documentElement&&document.documentElement.scrollTop)
	 {
	 	scrollTop_2=document.documentElement.scrollTop;
	 }
	 else if (document.body)
	 {
	 	scrollTop_2=document.body.scrollTop;
	 }
	 return scrollTop_2;
};

function getClientHeigth(){
	var clientHeight=0;
	if (document.body.clientHeight&&document.documentElement.clientHeight)
	 {
	 	clientHeight=Math.min(document.body.clientHeight,document.documentElement.clientHeight);
	 }
	 else 
	 {
	 	 	clientHeight=Math.max(document.body.clientHeight,document.documentElement.clientHeight);	
	 }
	 return clientHeight;
	};

	function getScrollHeight(){
	return Math.max(document.body.scrollHeight,document.documentElement.scrollHeight);
	};

	window.onscroll=function()
	{
		var scrollTop=document.documentElement.scrollTop||document.body.scrollTop;

		startMove(parseInt(document.documentElement.clientHeight/1.2-suspension.offsetHeight+scrollTop));
		// suspension.style.top=document.documentElement.clientHeight/1.2-suspension.offsetHeight+scrollTop+"px";

		var id_con=document.getElementById('con');
		var timer_2=null;
		var newnode = document.createElement("div"); 
			newnode.setAttribute("class","tb_one");
			newnode.innerHTML = "new item";
		 var contents = new Array();
		 	timer_2=setInterval(function(){
		 		if (getScrollTop()+getClientHeigth()==getScrollHeight()){
				
				for (var i = 0; i < 5; i++) {
					contents=newnode;
					id_con.appendChild(contents); 
				}

		 		}
		 		else
		 		{
		 			clearInterval(timer);
		 		}
		 	},100);
	};

};



