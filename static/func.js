// const items = document.querySelectorAll(".accordion a");
// function toggleAccordion(){
//   this.classList.toggle('active');
//   this.nextElementSibling.classList.toggle('active');
// }
// items.forEach(item => item.addEventListener('click', toggleAccordion));


$(function() {
  var $speed = 200;
  var $class = 'opened';
  var $class_open = '.faq-answer';

  $(document).ready(function() {
    $('.faq-question').on('click', function() {
      $ul = $(this).closest('ul');
      $answer = $(this).closest('li').find($class_open);

      if (!$(this).closest('li').hasClass($class)) {

        $ul.find('li').each(function() {
          if ($(this).hasClass($class))
            $(this).removeClass($class).find($class_open).slideUp($speed);
        });
      }

      $answer
        .slideToggle($speed)
        .closest('li')
        .toggleClass($class);
    });
  });
});


function reveal() {
  var reveals = document.querySelectorAll(".reveal");

  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals[i].getBoundingClientRect().top;
    var elementVisible = 150;

    if (elementTop < windowHeight - elementVisible) {
      reveals[i].classList.add("active");
    } else {
      reveals[i].classList.remove("active");
    }
  }
}

window.addEventListener("scroll", reveal);