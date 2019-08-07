$(function(){
	$(".btn-danger").click(function(){
		$.ajax({
			url: window.location.href,
			data: {'pk': $(this).data("pk"), 'type':'remove'},
			success: function(response){
				document.location.reload();
			}
		});
	});

	$(".btn-outline-success").click(function(){
		$.ajax({
			url: window.location.href,
			data: {'pk': $(this).data('pk'), 'type':'buy'},
			success: function(response){
				document.location.reload();
			}
		});
	});
});