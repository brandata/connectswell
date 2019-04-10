
$(document).scroll(function() {
  var y = $(this).scrollTop();
  if (y > 50) {
    $('.startButtons').fadeIn();
  } else {
    $('.startButtons').fadeOut();
  }
});