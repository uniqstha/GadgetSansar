$(document).ready(function(){

    $('.radio-group .radio').click(function(){
        $('.radio').addClass('gray');
        $(this).removeClass('gray');
        $('#lb').text("Company Name");
        
        
        
    });
    
   
    });
    
    

    $(document).ready(function()
    {
       if ($('#radio').is(':checked')) 
       {
         $('#lb').text("Company Name");
         alert("ddd")
         
       }
    }
  );