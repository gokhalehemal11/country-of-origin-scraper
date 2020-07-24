// client-side js
// run by the browser each time your view template is loaded

// by default, you've got jQuery,
// add other scripts at the bottom of index.html

$(function() {
  console.log('hello world :o')

  $('#search').keyup(function(){ 
  	var query = $(this).val();  
   if(query != '')  
		{  
		$.ajax({  
		 url:"/search",  
		 method:"GET",  
		 data:{query:query},  
		 success:function(data)  
		 {  
		      $('#location_list').fadeIn();  
		      $('#location_list').html(data);  
		 }  
		});  
		}
      })

    $(document).on('click', 'li', function(){  
         $('#search').val($(this).text());  
         $('#location_list').fadeOut();  
    })

  $('form').submit(function(event) {
    event.preventDefault()
    var searched = $('input').val()
    console.log(searched)
    $.ajax({  
		 url:"/searches",  
		 method:"GET",  
		 data:{query:searched},  
		 success:function(data)  
		 {  
		      alert(data);
		 }  
		});  
  })

})
