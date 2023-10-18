// const items = document.querySelectorAll(".accordion a");
// function toggleAccordion(){
//   this.classList.toggle('active');
//   this.nextElementSibling.classList.toggle('active');
// }
// items.forEach(item => item.addEventListener('click', toggleAccordion));

function forms() {
  document.querySelector(".form1").innerHTML = `<form class="text-light" method="post">
                        <h3 class="mt-3">Отправить запрос</h3>
                        <div class="mb-3 form__group field">
                            <input minlength="2" type="text" class="form__field" name="name" id="name" placeholder="name" required>
                            <label class="form__label" for="name">Ваше имя</label>
                        </div>
                        <div class="mb-3 form__group field">
                            <input type="email" class="form__field" name="email" id="email" placeholder="email" required aria-describedby="emailHelp">
                            <label class="form__label" for="email">Ваш email</label>
                        </div>
                        <div class="mb-3 form__group field">
                            <input minlength="10" type="tel" class="form__field" name="number" id="number" placeholder="number" required aria-describedby="numberHelp">
                            <label class="form__label" for="number">Ваш телефон</label>
                        </div>
                        <div class="mb-3 form__group field d-none">
                            <input minlength="10" type="tel" class="form__field" name="number" id="lovushka" placeholder="number" aria-describedby="numberHelp">
                            <label class="form__label" for="lovushka">Ваш телефон</label>
                        </div>
                        <div class="mb-3 form__group field">
                            <textarea cols="40" rows="3" class="form__field" name="comment" id="comment" placeholder="comment"></textarea>
                            <label class="form__label" for="comment">Комментарий</label>
                        </div>
                        <div class="mb-3">
                            <input type="checkbox" name="check" id="check" class="custom-checkbox" required>
                            <label for="check" id="mail-check" style="color: gray; font-size: 0.8em;">Согласие на обработку персональных данных</label>
                        </div>
                        <button type="submit" id="mail-btn" class="btn btn-danger">Отправить</button>
                    </form>`;
  document.querySelector(".form2").innerHTML = `<form class="text-light" method="post" style="padding-top: 15px">
                        <h3 class="mt-3">Отправить запрос</h3>
                        <div class="mb-3 form__group field">
                            <input minlength="2" type="text" class="form__field" name="name" id="name1" placeholder="name" required>
                            <label class="form__label" for="name1">Ваше имя</label>
                        </div>
                        <div class="mb-3 form__group field">
                            <input type="email" class="form__field" name="email" id="email1" placeholder="email" required aria-describedby="emailHelp">
                            <label class="form__label" for="email1">Ваш email</label>
                        </div>
                        <div class="mb-3 form__group field">
                            <input minlength="10" type="tel" class="form__field" name="number" id="number1" placeholder="number" required aria-describedby="numberHelp">
                            <label class="form__label" for="number1">Ваш телефон</label>
                        </div>
                        <div class="mb-3 form__group field d-none">
                            <input minlength="10" type="tel" class="form__field" name="number" id="lovushka1" placeholder="number" aria-describedby="numberHelp">
                            <label class="form__label" for="lovushka1">Ваш телефон</label>
                        </div>
                        <div class="mb-3 form__group field">
                            <textarea cols="40" rows="3" class="form__field" name="comment" id="comment1" placeholder="comment"></textarea>
                            <label class="form__label" for="comment1">Комментарий</label>
                        </div>
                        <div class="mb-3">
                            <input type="checkbox" name="check1" id="check1" class="custom-checkbox" required>
                            <label for="check1" style="color: gray; font-size: 0.8em;">Согласие на обработку персональных данных</label>
                        </div>
                        <button type="submit" class="btn btn-danger">Отправить</button>
                    </form>`;
  // var dodo = document.querySelectorAll(".comment__text");
  // document.querySelector(".dodo").innerHTML = `${dodo[0]}`;
  // console.log(dodo[0].textContent)
}

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

const copyContent1 = async () => {
    try {
      await navigator.clipboard.writeText("pvl@magnavis.ru");
      console.log('Content copied to clipboard');
    } catch (err) {
      console.error('Failed to copy: ', err);
    }
}
const copyContent2 = async () => {
    try {
      await navigator.clipboard.writeText("andr@magnavis.ru");
      console.log('Content copied to clipboard');
    } catch (err) {
      console.error('Failed to copy: ', err);
    }
}
// $(function() {
//   // copy content to clipboard
//   function copyToClipboard(element) {
//     var $temp = $("<input>");
//     $("body").append($temp);
//     $temp.val($(element).text()).select();
//     document.execCommand("copy");
//     $temp.remove();
//   }
//
//   // copy coupone code to clipboard
//   // $(".coupon-btn").on("click", function() {
//   //   copyToClipboard("#coupon-field");
//   //   $(".coupon-alert").fadeIn("slow");
//   });
// });
//
//
//
// $(function() {
//   // copy content to clipboard
//   function copyToClipboard(element) {
//     var $temp = $("<input>");
//     $("body").append($temp);
//     $temp.val($(element).text()).select();
//     document.execCommand("copy");
//     $temp.remove();
//   }
//
//   // copy coupone code to clipboard
//   // $(".coupon-btn-2").on("click", function() {
//   //   copyToClipboard("#coupon-field-2");
//   //   $(".coupon-alert-2").fadeIn("slow");
//   // });
// });

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

function nav() {
  var fl = document.querySelectorAll(".navv");
  var nv = document.querySelectorAll(".nav-ac");
  // nv.slideToggle(200);
  for (var i = 0; i < fl.length; i++) {
    fl[i].classList.toggle("d-none");
    nv[i].classList.toggle("nav-activ");
  }
}
//   var speed = 200;
//   var clas = 'opened';
//   var clas_open = '.faq-answer';
//   $ul = $(this).closest('ul');
//   $answer = $(this).closest('li').find($class_open);
//
//   if (!$(this).closest('li').hasClass($class)) {
//
//     $ul.find('li').each(function() {
//       if ($(this).hasClass($class))
//         $(this).removeClass($class).find($class_open).slideUp($speed);
//     });
//   }
//
//   answer
//     .slideToggle($speed)
//     .closest('li')
//     .toggleClass($class);
//
// }


// $(function() {
//   var $speed = 200;
//   var $class = 'opened';
//   var $class_open = '.faq-answer';
//
//   $(document).ready(function() {
//     $('.navv').on('click', function() {
//       $ul = $(this).closest('ul');
//       $answer = $(this).closest('li').find($class_open);
//
//       if (!$(this).closest('li').hasClass($class)) {
//
//         $ul.find('li').each(function() {
//           if ($(this).hasClass($class))
//             $(this).removeClass($class).find($class_open).slideUp($speed);
//         });
//       }
//
//       $answer
//         .
//         .closest('li')
//         .toggleClass($class);
//     });
//   });
// });
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


// y1.style.cssText = 'background: rgba(87,90,87,0.66);'

