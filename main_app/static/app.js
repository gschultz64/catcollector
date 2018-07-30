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