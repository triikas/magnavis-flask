const bottom_panel = document.querySelector(".bottom-panel")
const bottom_text = document.querySelector(".bottom-text")
const win = document.querySelector(".window")
const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0)

function mp() {
  bottom_panel.style.display = 'block'
  bottom_panel.style.top = "20vh";
  bottom_text.innerHTML = `<p class="mt-4">Обеспечиваем транспортировку грузов с использованием различных видов транспорта, чтобы доставить ваш заказ точно в срок</p>`;
}
function st() {
  bottom_panel.style.display = 'block'
  bottom_panel.style.top = "20vh";
  bottom_text.innerHTML = `<p class="mt-4">Гарантируем защиту ваших ценных грузов на всем пути доставки</p>`;
}
function tog() {
  bottom_panel.style.display = 'block'
  bottom_panel.style.top = "20vh";
  bottom_text.innerHTML = `<h3 style="font-weight: bolder;">Таможенное<br>оформление<br>грузов</h3><p class="mt-4">Правильное и быстро оформляем все типы грузов при пересечении таможенной границы, минимизируем риски задержек. Весь комплекс таможенных процедур для физических и юридических лиц: подготовка необходимых документов, заполнение таможенных деклараций, платежи и взаимодействие с таможенным органами. МАГНАВИС сопровождает ваш груз на каждом этапе его прохождения границы</p>`;
}
var OldY = null;
var NewY = null;
var d;

win.addEventListener('touchstart', (e) => {
  OldY = e.changedTouches[0].clientY;
  NewY = OldY.y;
})


win.addEventListener('touchmove', (e) => {
  e.preventDefault();
  NewY = e.changedTouches[0].clientY;
  if (NewY > 0.2*vh) {
    bottom_panel.style.top = String(NewY)+"px";
  }
  // console.log(NewY, "   ", 20*vh)
  // if (OldY - NewY < 0) {
  //   // d = -(OldY - NewY)
  //   // bottom_panel.style.transform = "translate3d( 0 px, " + d + "px, 0)";
  //   // bottom_panel.style.backgroundColor = 'red'
  //
  // }
})


win.addEventListener('touchend', (e) => {
  if (NewY > 0.5*vh) {
    EndY = NewY
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
    EndY = NewY
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
