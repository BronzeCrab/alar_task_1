$(document).ready(function() {
    $(".btn-danger").on("click", function(){
    	var id = $(this).parents().siblings(".user_id").text();

     	$.ajax({
	        url : "/delete/"+id, // the endpoint
	        type : "GET", // http method
			success: function(json) {
			  if(json.error) return;
			  //fire off other ajax calls
			  $(document).ajaxStop(function() { location.reload(true); });
			}
     	});	

    });
});