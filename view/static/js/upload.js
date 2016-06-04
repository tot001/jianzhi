window.onload=function() 
{
	var id_title=document.getElementById('id_title');
	var id_zhao_ping=document.getElementById('id_zhao_ping');
	var id_jing_er=document.getElementById('id_jing_er');
	var id_di_zhi=document.getElementById('id_di_zhi');
	var id_jie_suan=document.getElementById('id_jie_suan');
	var id_shi_jian=document.getElementById('id_shi_jian');
	var id_shi_jian2=document.getElementById('id_shi_jian2');
	var id_lxfs=document.getElementById('id_lxfs');
	var txt_introduction=document.getElementById('txt_introduction');
	
	var	txt_tijiao=document.getElementById('txt_tijiao');

	var oText=document.getElementsByTagName('span');

	id_shi_jian.readOnly="true";
	id_shi_jian2.readOnly="true";

	id_zhao_ping.onkeypress=function()
	{
		if(window.event.keyCode < 48 || window.event.keyCode >57)
		{
		window.event.keyCode = 0;
		window.event.returnValue = false;
		}
	};
	id_jing_er.onkeypress=function()
	{
		if(window.event.keyCode < 48 || window.event.keyCode >57)
		{
		window.event.keyCode = 0;
		window.event.returnValue = false;
		}
	};


	id_title.placeholder="公司+职位 例：顺丰快递员";
	id_zhao_ping.placeholder="例：5人";
	id_jing_er.placeholder="";
	id_di_zhi.placeholder="请输入详细地址";
	id_jie_suan.placeholder="";
	id_shi_jian.placeholder="";
	id_shi_jian2.placeholder="";
	id_lxfs.placeholder="例：手机/QQ：1304630xxxx";
	txt_introduction.placeholder="注意美化您的排版哦~";



	id_title.onblur=function()
	{
		if (id_title.value==="") 
			{
				 oText[0].style.opacity="1";
			}

 		 else 
             {
                 oText[0].style.opacity="0";
              } 		
	}


	id_zhao_ping.onblur=function()
	{
		if (id_zhao_ping.value==''||id_zhao_ping.value==null)
		{
					oText[1].style.opacity="1";
		}		
			else
                {
                    oText[1].style.opacity="0";
                }  

		
	}

	id_jing_er.onblur=function()
	{
		if (id_jing_er.value==''||id_jing_er.value==null)
		{
					oText[2].style.opacity="1";		
			
		}		
			else
                {
                    oText[2].style.opacity="0";
                }  

		
	}

	id_di_zhi.onblur=function()
	{
		if (id_di_zhi.value==''||id_di_zhi.value==null)
		{
			
				
					oText[3].style.opacity="1";
				
				
		}		
			else
                {
                    oText[3].style.opacity="0";
                }  

		
	}

	id_shi_jian.onblur=function()
	{
			if (id_shi_jian.value==''||id_shi_jian.value==null)
			{
			
				
					oText[4].style.opacity="1";
				
				
			}		
			else
                {
                    oText[4].style.opacity="0";
                }  
	}
		
	

	id_shi_jian2.onblur=function()
	{
			if (id_shi_jian2.value==''||id_shi_jian2.value==null)
			{
					oText[4].style.opacity="1";
			}		
			else
                {
                    oText[4].style.opacity="0";
                }  
	}


	id_lxfs.onblur=function()
	{
			if (id_lxfs.value==''||id_lxfs.value==null)
			{
					oText[5].style.opacity="1";
			}		
			else
                {
                    oText[5].style.opacity="0";
                }  
	}


	txt_introduction.onblur=function()
	{
			if (txt_introduction.value==''||txt_introduction.value==null)
			{
					oText[6].style.opacity="1";									
			}		
			else
                {
                    oText[6].style.opacity="0";
                }  
	}



txt_tijiao.onclick=function ()

{
 
	if (id_title.value==""||id_title==null)
	 {
	 	id_title.focus();
	 	oText[0].style.opacity="1";
	 	return false;
	 }
	 else if (id_zhao_ping.value==""||id_zhao_ping==null)
	  {
	 	id_zhao_ping.focus();
	 	oText[1].style.opacity="1";
	 	return false;
	  }
	  
	 else if (id_jing_er.value==""||id_jing_er==null)
	  {
	 	id_jing_er.focus();
	 	oText[2].style.opacity="1";
	 	return false;
	  }

	 else if (id_di_zhi.value==""||id_di_zhi==null)
	  {
	 	id_di_zhi.focus();
	 	oText[3].style.opacity="1";
	 	return false;
	  }

	 else if (id_shi_jian.value==""||id_shi_jian==null)
	  {
	 	id_shi_jian.focus();
	 	oText[4].style.opacity="1";
	 	return false;
	  }

	 else if (id_shi_jian2.value==""||id_shi_jian2==null)
	  {
	 	id_shi_jian2.focus();
	 	oText[4].style.opacity="1";
	 	return false;
	  }

	 else if (id_lxfs.value==""||id_lxfs==null)
	  {
	 	id_lxfs.focus();
	 	oText[5].style.opacity="1";
	 	return false;
	  }

	 else if (txt_introduction.value==""||txt_introduction==null)
	  {
	 	txt_introduction.focus();
	 	oText[6].style.opacity="1";
	 	return false;
	  }

	  else
	  {
	  	return true;
	  }  
	  	
	var content=document.getElementById('txt_introduction').value;
	content=content.replace(/\n/g,'br');
	document.getElementById("txt_introduction").value=content; 
}



}