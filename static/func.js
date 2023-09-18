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

(() => {
  'use strict';
  // Page is loaded
  const objects = document.getElementsByClassName('asyncImage');
  Array.from(objects).map((item) => {
    // Start loading image
    const img = new Image();
    img.src = item.dataset.src;
    // Once image is loaded replace the src of the HTML element
    img.onload = () => {
      item.classList.remove('asyncImage');
      return item.nodeName === 'IMG' ?
        item.src = item.dataset.src :
        item.style.backgroundImage = `url(${item.dataset.src})`;
    };
  });
})();

$(function() {
  // copy content to clipboard
  function copyToClipboard(element) {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($(element).text()).select();
    document.execCommand("copy");
    $temp.remove();
  }

  // copy coupone code to clipboard
  $(".coupon-btn").on("click", function() {
    copyToClipboard("#coupon-field");
    $(".coupon-alert").fadeIn("slow");
  });
});

$(function() {
  // copy content to clipboard
  function copyToClipboard(element) {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($(element).text()).select();
    document.execCommand("copy");
    $temp.remove();
  }

  // copy coupone code to clipboard
  $(".coupon-btn-2").on("click", function() {
    copyToClipboard("#coupon-field-2");
    $(".coupon-alert-2").fadeIn("slow");
  });
});

function flashh() {
  var fl = document.querySelectorAll(".flash");
  for (var i = 0; i < fl.length; i++) {
    fl[i].classList.add("d-none");
  }

}

function status() {
  var fl = document.querySelectorAll(".status-vrem");
  for (var i = 0; i < fl.length; i++) {
    fl[i].classList.remove("d-none");
  }

}

function status_delete() {
  var fl = document.querySelectorAll(".status-vrem");
  for (var i = 0; i < fl.length; i++) {
    fl[i].classList.add("d-none");
  }

}

function down() {
  var down = document.querySelectorAll(".down");
  var y1 = document.querySelectorAll(".badge");
  for (var i = 0; i < down.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = down[i].getBoundingClientRect().top;

    if (elementTop < windowHeight*0.7) {
      down[i].classList.add("svg-none");
      y1[i].classList.add("bad");
      // y1.style.cssText = 'background: rgba(87,90,87,0.66);'
    }
    if (elementTop > windowHeight*0.8) {
      down[i].classList.remove("svg-none");
    }
  }
}

window.addEventListener("scroll", down);


y1.style.cssText = 'background: rgba(87,90,87,0.66);'

