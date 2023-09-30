<script src="https://code.jquery.com/jquery-"></script>
$(document).ready(function() {
    var slideCount = $('.carousel-item').length;
    var slideWidth = $('.carousel-item').outerWidth();
    var slideHeight = $('.carousel-item').outerHeight();
    var slideTotalWidth = slideCount * slideWidth;
  
    $('.carousel-slide').css({ width: slideTotalWidth });
  
    function moveSlide() {
      $('.carousel-slide').animate({ 'margin-left': -slideWidth }, 1000, function() {
        $('.carousel-item:first').appendTo('.carousel-slide');
        $('.carousel-slide').css('margin-left', 0);
      });
    }
  
    var slideInterval = setInterval(moveSlide, 3000);
  
    $('.carousel-container').hover(
      function() {
        clearInterval(slideInterval);
      },
      function() {
        slideInterval = setInterval(moveSlide, 3000);
      }
    );
  });