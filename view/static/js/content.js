window.onload=function  () {
	var content=document.getElementById('s_content').innerHTML;
	content=content.replace(/br/g,'<br>');
	document.getElementById("s_content").innerHTML=content;
}