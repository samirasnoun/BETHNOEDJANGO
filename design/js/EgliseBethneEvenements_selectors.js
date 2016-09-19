
var checkbox=$(".sujet1:text").css({
	color: 'red',
	size: '30px'
});

console.log(checkbox);

function valueChanged()
{
	
	if($(this).is(":checked"))   
		$(".col_sujet1").show();
	else
		$(".col_sujet1").hide();


}




toto=$(".sujet4");


$(".sujet1, .sujet2, .sujet3, .sujet4").on("change", function() {


	tata=".col_" + $(this).attr('class');
	



	if($(this).is(":checked"))   
		$(tata).show();
	else
		$(tata).hide();

});








