
$(".sujet").on("change", function() {


	sujet=".col_" + $(this).attr('id');
	



	if($(this).is(":checked"))   
		$(sujet).show();
	else
		$(sujet).hide();

});





$(".auteur").on("click", function() {


	sujet= $(this).attr('id') ;
	



	 
		/*$(sujet).show();*/
	
		$(sujet).hide();

});
