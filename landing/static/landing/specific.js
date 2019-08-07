
$("#add_to_cart").click(function(){
	$.ajax({
		url: window.location.href,
		success: function(data){
			if(data.success)
				window.location.href = "/cart";
			else
				alert("Server error");
		}
	});
});