// $('document').ready()
$('.like-btn').on('click', function(e) {
  e.preventDefault();
  var element = $(this);
  $.ajax({
    url: '/like_cat/',
    method: 'GET',
    data: {cat_id: element.attr('data-id')},
    success: function(response) {
      element.html('Likes: ' + response)
    }
  })
})

$('.addtoy').on('click', function(e) {
  console.log('you clicked');
  e.preventDefault();
  var element = $(this);
  $.ajax({
    url: '/add_toy_to_cat/',
    method: 'GET',
    data: {cat_id: element.attr('data-cat'), toy_id: element.attr('data-toy')},
    success: function (response) {  
      window.location = '/' + element.attr('data-cat');
    }
  })
})