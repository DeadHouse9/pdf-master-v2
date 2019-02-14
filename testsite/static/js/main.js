var wrap = $('#wrapper'),
     btn = $('.open-modal-btn'),
     modal = $('.cover, .modal, .content');

btn.on('click', function() {
  modal.fadeIn();
});


$('.modal').click(function() {
  wrap.on('click', function(event) {
    var select = $('.content');
    if ($(event.target).closest(select).length)
      return;
    modal.fadeOut();
    wrap.unbind('click');
  });
});