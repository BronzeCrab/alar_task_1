$(document).ready(function() {
	//delete
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
    //edit
    $('.select').change(function(){
    	var is_admin = $(this).val();
    	var id = $(this).parents().siblings(".user_id").text();   	
     	$.ajax({
	        url : "/put/"+id, // the endpoint
	        type : "GET", // http method
	        data : { is_admin : is_admin },
			success: function(json) {
			  if(json.error) return;
			  //fire off other ajax calls
			  $(document).ajaxStop(function() { location.reload(true); });
			}
     	});	
    });
});