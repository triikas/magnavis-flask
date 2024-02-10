const bottom_panel = document.querySelector(".bottom-panel")
const bottom_text = document.querySelector(".bottom-text")
const win = document.querySelector(".window")
const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0)

function frm1() {
  bottom_panel.style.display = 'block'
  bottom_panel.style.top = "20vh";
  bottom_text.innerHTML = `<form class="text-light" method="post" id="request-f" style="min-width: 500px;">
                        <h3>Отправить запрос</h3>
                        <div class="mb-5 form__group field">
                            <input minlength="2" type="text" class="form__field" name="name" id="name" placeholder="name" required>
                            <label class="form__label" for="name">Ваше имя</label>
                        </div>
                        <div class="mb-5 form__group field">
                            <input type="email" class="form__field" name="email" id="email" placeholder="email" required aria-describedby="emailHelp">
                            <label class="form__label" for="email">Ваш email</label>
                        </div>
                        <div class="mb-5 form__group field">
                            <input minlength="10" type="tel" class="form__field" name="number" id="number" placeholder="number" required aria-describedby="numberHelp">
                            <label class="form__label" for="number">Ваш телефон</label>
                        </div>
                        <div class="mb-5 form__group field d-none">
                            <input minlength="10" type="tel" class="form__field" name="number" id="lovushka" placeholder="number" aria-describedby="numberHelp">
                            <label class="form__label" for="lovushka">Ваш телефон</label>
                        </div>
                        <div class="mb-5 form__group field">
                            <textarea cols="40" rows="3" class="form__field" name="comment" id="comment" placeholder="comment"></textarea>
                            <label class="form__label" for="comment">Комментарий</label>
                        </div>
                        <div class="mb-5">
                            <input type="checkbox" name="check" id="check" class="custom-checkbox" required>
                            <label for="check" id="mail-check" style="color: #b9b9b9; font-size: 0.8em;">Согласие на обработку персональных данных</label>
                        </div>
                        <button type="submit" id="mail-btn" class="btn btn-danger btnf1">Отправить</button>
                        <div class="mes"></div>
                    </form>`;
}
function frm2() {
  bottom_panel.style.display = 'block'
  bottom_panel.style.top = "20vh";
  bottom_text.innerHTML = `<form method="post" id="status-f" style="min-width: 500px;">
                    <h3>Статус груза</h3>
                    <div class="mb-5 form__group field">
                        <input minlength="5" type="text" class="form__field" name="kod" id="kod" placeholder="kod" required>
                        <label class="form__label" for="kod">Код груза</label>
                    </div>
                    <button type="submit" class="btn btn-danger btnf1" style="font-size: 1.6em">Отправить</button>
                    <div class="mes"></div>
                </form>`;
}
function mp() {
  bottom_panel.style.display = 'block'
  bottom_panel.style.top = "20vh";
  bottom_text.innerHTML = `<h3 style="font-weight: bolder;">Мультимодальные<br>перевозки</h3><p class="mt-4">Обеспечиваем транспортировку грузов с использованием различных видов транспорта, чтобы доставить ваш заказ точно в срок. При этом доставка осуществляется по одному договору. На всём пути следования MAGNAVIS несёт ответственность за сохранность грузов и обеспечивает их качественное и безопасное прохождение всех границ. Виды транспорта выбираются на основе специфики грузов и с учётом пожеланий клиентов. Наши менеджеры детально продумывают маршрут и согласовывают порядок следования, чтобы доставка прошла идеально, без задержек и потерь.</p>`;
}
function st() {
  bottom_panel.style.display = 'block'
  bottom_panel.style.top = "20vh";
  bottom_text.innerHTML = `<h3 style="font-weight: bolder;">Страхование<br>грузов</h3><p class="mt-4">Наша основная задача — доставить ваш ценный груз в целостности и сохранности, однако убытки могут возникнуть по независящим от нас причинам. Поэтому мы предлагаем услуги по страхованию грузов. Благодаря этому товары защищены от всех рисков, которые могут возникнуть в процессе погрузки и выгрузки, транспортировки и хранения товаров. Стоимость страхования рассчитывается в зависимости от характеристик груза, а также от сложности маршрута перевозки.</p>`;
}
function tog() {
  bottom_panel.style.display = 'block'
  bottom_panel.style.top = "20vh";
  bottom_text.innerHTML = `<h3 style="font-weight: bolder;">Таможенное<br>оформление<br>грузов</h3><p class="mt-4">Правильно и быстро оформляем все типы грузов при пересечении таможенной границы, минимизируем риски задержек. Весь комплекс таможенных процедур для физических и юридических лиц: подготовка необходимых документов, заполнение таможенных деклараций, платежи и взаимодействие с таможенным органами. МАГНАВИС сопровождает ваш груз на каждом этапе его прохождения границы.</p>`;
}
function ps() {
  bottom_panel.style.display = 'block'
  bottom_panel.style.top = "20vh";
  bottom_text.innerHTML = `<h3 style="font-weight: bolder;">Перевозка<br>спецгрузов</h3><p class="mt-4">Осуществляем профессиональную перевозку специальных грузов: от музейных экспонатов до жирафов. Благодаря нашим специалистам мы доставляем грузы, которым требуется особые условия: температурный режим, специальное оборудование, дополнительные меры безопасности. Особое внимание уделяется подготовке необходимых документов и получению разрешений. Охрана специального груза также гарантирована: от погрузки до передачи в руки клиента товары находятся под контролем наших специалистов.</p>`;
}
function su() {
  bottom_panel.style.display = 'block'
  bottom_panel.style.top = "20vh";
  bottom_text.innerHTML = `<h3 style="font-weight: bolder;">Складские<br>услуги</h3><p class="mt-4 mb-0">MAGNAVIS предоставляет профессиональные комплексные складские услуги. Это не только хранение любых видов грузов в специально оборудованных складах, но и операции по погрузке, выгрузке, приёмке и размещении товаров. Обеспечение безопасности 24/7, создание особых условий для хранения товаров разных категорий, размещение на короткий и длительный сроки. Учитывая особенности ваших грузов, наши менеджеры смогут подобрать наиболее оптимальный вариант размещения товаров и эффективно организовать процесс хранения.</p>`;
}
var OldY = null;
var NewY = null;
var OldYBlock = null;
var NewYBlock = null;
var d;

bottom_panel.addEventListener('touchstart', (e) => {
  OldY = e.changedTouches[0].clientY;
  NewY = OldY.y;
  OldYBlock = bottom_panel.getBoundingClientRect().top;

})


bottom_panel.addEventListener('touchmove', (e) => {
  e.preventDefault();
  NewY = e.changedTouches[0].clientY;
  NewYBlock = bottom_panel.getBoundingClientRect().top;
  if (NewY-OldY > 0) {
    bottom_panel.style.top = String(OldYBlock+(NewY-OldY))+"px";
  } else if (NewY-OldY > 0 && NewYBlock > OldYBlock) {
    bottom_panel.style.top = String(OldYBlock+(NewY-OldY))+"px";
  }
  // console.log(NewY, "   ", 20*vh)
  // if (OldY - NewY < 0) {
  //   // d = -(OldY - NewY)
  //   // bottom_panel.style.transform = "translate3d( 0 px, " + d + "px, 0)";
  //   // bottom_panel.style.backgroundColor = 'red'
  //
  // }
})


bottom_panel.addEventListener('touchend', (e) => {
  if (NewYBlock > 0.5*vh) {
    EndY = NewYBlock
    // while (EndY < vh) {
      let end = setInterval(function () {
        if (EndY < vh) {
          EndY += 25
          // console.log("qwe")
          bottom_panel.style.top = String(EndY) + "px";
        } else {
          clearInterval(end);
          bottom_panel.style.display = 'none'
          return;
        }
      }, 15)
    // }
  } else {
    EndY = NewYBlock
    // while (EndY < vh) {
      let end = setInterval(function () {
        if (EndY > 0.2*vh) {
          EndY -= 25
          // console.log("qwe")
          bottom_panel.style.top = String(EndY) + "px";
        } else {
          clearInterval(end);
          bottom_panel.style.top = "20vh";
          return;
        }
      }, 15)
    // bottom_panel.style.top = "20vh";
  }
  OldY = null;
  NewY = null;
  // console.log("asd")
})


function d_none() {
  EndY = NewY
  setTimeout(function () {
    if (EndY < vh) {
      EndY += 4
      bottom_panel.style.top = String(EndY)+"px";
    } else {return;}
  }, 20)

}
// var dragItem = document.querySelector(".bottom-panel");
// var container = document.querySelector(".window");
//
// var active = false;
// var currentX;
// var currentY;
// var initialX;
// var initialY;
// var xOffset = 0;
// var yOffset = 0;
//
// container.addEventListener("touchstart", dragStart, false);
// container.addEventListener("touchend", dragEnd, false);
// container.addEventListener("touchmove", drag, false);
//
// container.addEventListener("mousedown", dragStart, false);
// container.addEventListener("mouseup", dragEnd, false);
// container.addEventListener("mousemove", drag, false);
//
// function dragStart(e) {
//   if (e.type === "touchstart") {
//     initialX = e.touches[0].clientX - xOffset;
//     initialY = e.touches[0].clientY - yOffset;
//   } else {
//     initialX = e.clientX - xOffset;
//     initialY = e.clientY - yOffset;
//   }
//
//   if (e.target === dragItem) {
//     active = true;
//   }
// }
//
// function dragEnd(e) {
//   initialX = currentX;
//   initialY = currentY;
//
//   active = false;
// }
//
// function drag(e) {
//   if (active) {
//
//     e.preventDefault();
//
//     if (e.type === "touchmove") {
//       currentX = e.touches[0].clientX - initialX;
//       currentY = e.touches[0].clientY - initialY;
//     } else {
//       currentX = e.clientX - initialX;
//       currentY = e.clientY - initialY;
//     }
//
//     xOffset = currentX;
//     yOffset = currentY;
//
//     setTranslate(currentX, currentY, dragItem);
//   }
// }
//
// function setTranslate(xPos, yPos, el) {
//   el.style.transform = "translate3d(" + xPos + "px, " + yPos + "px, 0)";
//   console.log("uhkuhk")
// }
