/* Create Post */
$('#new-product-modal').on('show.bs.modal', function (e) {
    var url = $(this).data("url");
    console.log(url);
    $.ajax({
         url: url,
         method: "GET",
         success: function(response){
            
           $('#new-product-body').html(response);
         }
    })
 }); 
 
 $(document).on('submit', '#new-product-form', function (e){
     var url = $(this).attr("action");
     e.preventDefault();
      $.ajax({
         url: url,
         method: "POST",
         data:  $(this).serialize(),
         success: function(response){
             console.log(response);
             $('#new-product-body').html(response);
         }
    })
 });
 
 $('#new-product-modal').on('hide.bs.modal', function (e) {
     location.reload();
 })
 
 $("#id_is_draft").parent().attr("id", "div_id_is_draft");
