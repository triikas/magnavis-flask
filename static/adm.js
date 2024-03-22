function new_p () {
    num_p = String(Number(document.querySelector(".num-p").getAttribute("id")) + 1);
    document.querySelector(".num-p").id = num_p;
    p = document.createElement("div");
    p.classList.add(`mb-2`, `p${num_p}`);
    p.innerHTML = `<label for="${num_p}" class="text-light d-block">Абзац ${num_p}</label><textarea type="text" name="p${num_p}" class="p_${num_p} input-group-text text-start w-100"></textarea>`
    buttons = document.querySelector(`.buttons`);
    buttons.parentNode.insertBefore(p, buttons)
}


function del_p () {
    num_p = document.querySelector(".num-p").getAttribute("id");
    if (Number(num_p) > 1) {
        document.querySelector(`.p${num_p}`).remove();
        document.querySelector(".num-p").id = String(Number(num_p)-1);
    }
}

function but_recolor(id) {
    try {
        last_but = document.querySelector(".btn-dark");
        last_but.classList.remove("border");
        last_but.classList.remove("btn-dark");
    } catch (e) {}
    document.getElementById(id).classList.add("btn-dark", "border");
}

function data_update(dt) {
    dt_all = document.querySelectorAll(".data");
    for (let i = 0; i < dt_all.length; i++) {
        dt_all[i].style.display = "none";
    }
    if (dt !== "no") {document.getElementById(dt).style.display = "block";}
    document.querySelector(".main").innerHTML = `<!--no-->`;
}

function getStyle(el, styleProp) {
  var value, defaultView = (el.ownerDocument || document).defaultView;
  // W3C standard way:
  if (defaultView && defaultView.getComputedStyle) {
    // sanitize property name to css notation
    // (hypen separated words eg. font-Size)
    styleProp = styleProp.replace(/([A-Z])/g, "-$1").toLowerCase();
    return defaultView.getComputedStyle(el, null).getPropertyValue(styleProp);
  } else if (el.currentStyle) { // IE
    // sanitize property name to camelCase
    styleProp = styleProp.replace(/\-(\w)/g, function(str, letter) {
      return letter.toUpperCase();
    });
    value = el.currentStyle[styleProp];
    // convert other units to pixels on IE
    if (/^\d+(em|pt|%|ex)?$/i.test(value)) {
      return (function(value) {
        var oldLeft = el.style.left, oldRsLeft = el.runtimeStyle.left;
        el.runtimeStyle.left = el.currentStyle.left;
        el.style.left = value || 0;
        value = el.style.pixelLeft + "px";
        el.style.left = oldLeft;
        el.runtimeStyle.left = oldRsLeft;
        return value;
      })(value);
    }
    return value;
  }
}


fle = ["no"]
function focus_list_el(data) {


    if (fle[0] !== "no" && fle[0] !== data[0]) {
        document.getElementById(fle[0]).style.backgroundColor = "rgba(0, 0, 0, 0)"
    }
    fle = data
    console.log(fle)
    try {
       console.log(getStyle(document.getElementById(data[0]), "background-color"))
        if (getStyle(document.getElementById(data[0]), "background-color") === "rgba(44, 145, 81, 0.55)") {
            document.getElementById(data[0]).style.backgroundColor = "rgba(0, 0, 0, 0)"
            fle = ["no"]
        } else {
            document.getElementById(data[0]).style.backgroundColor = "rgba(44, 145, 81, 0.55)"
        }
    } catch (e) {}


}
function but (b) {
    focus_list_el(["no"])
    switch (b) {
        case "news":
            data_update("news-data");
            document.querySelector(".but-second").innerHTML = `<a onclick="but_second('add_news')" class="btn btn-success">Добавить</a>
            <a onclick="but_second('del_news')" class="btn btn-danger mx-2">Удалить</a>
            <a onclick="but_second('ch_news')" class="btn btn-warning">Редактировать</a>
            <a onclick="but_second('redirect')" class="btn btn-light mx-2">Перейти</a>
            <a class="btn btn-info">Помощь</a>`;
            but_recolor("news");
            break;
        case "titles":
            data_update("titles-data");
            document.querySelector(".but-second").innerHTML = `<a onclick="but_second('add_titles')" class="btn btn-success">Добавить</a>
            <a onclick="but_second('del_titles')" class="btn btn-danger mx-2">Удалить</a>
            <a onclick="but_second('ch_titles')" class="btn btn-warning">Редактировать</a>
            <a onclick="but_second('redirect')" class="btn btn-light mx-2">Перейти</a>
            <a class="btn btn-info">Помощь</a>`;
            but_recolor("titles");
            break;
        case "logs":
            data_update("logs-data");
            document.querySelector(".but-second").innerHTML = ``;
            but_recolor("logs");
            break;
        // case "del_news":
        //     document.querySelector(".main").classList.add("d-none");
        //     document.querySelector(".del-news").classList.remove("d-none");
        //     break;
        // case "del_news_main":
        //     document.querySelector(".del-news").classList.add("d-none");
        //     document.querySelector(".main").classList.remove("d-none");
        //     break;
    }
}


function but_second (b) {

    data_update("no");
    switch (b) {
        case "redirect":
            window.location.replace(fle[1]);
            break;
        case "add_news":
            focus_list_el(["no"])
            document.querySelector(".main").innerHTML = `<div class="d-flex justify-content-center"><div style="width: 600px">
                <form method="post" id="add-news" enctype="multipart/form-data">
                    <input type="hidden"  name="type" value="add-news"  />
                    <h2 class="text-light px-0">Новая новость</h2>
                    <div class="mb-2">
                        <label for="title" class="text-light d-block">Заголовок</label>
                        <input type="text" name="title" class="input-group-text text-start w-100" required>
                    </div>
                    <div class="mb-2">
                        <label for="path" class="text-light d-block">Ссылка</label>
                        <input type="text" name="path" class="input-group-text text-start w-100" required value="https://magnavis.ru/info/">
                    </div>
                    <div class="mb-2 text-light">
                        <p class="mb-1">* Ссылка на новость <t class="text-danger">https://magnavis.ru/info/name</t></p>
                        <p>* Никогда не ставить / в конце</p>
                    </div>
                    <div class="mb-2">
                        <label for="date" class="text-light d-block">Дата</label>
                        <input type="date" name="date" class="input-group-text text-start w-100">
                    </div>
                    <div class="mb-2">
                        <label for="img" class="text-light d-block">Изображение</label>
                        <input type="file" name="img" class="input-group-text text-start w-100">
                    </div>
                    <div class="mb-2">
                        <label for="img2" class="text-light d-block">Изображение 2</label>
                        <input type="file" name="img2" class="input-group-text text-start w-100">
                    </div>
                    <div class="mb-2 text-light">
                        <p class="mb-1">* Второе изображение (горизонтальная версия) нужно если основное сильно вытянуто по высоте для лучшего отображения статьи</p>
                        <p>* Все изображения должны быть в формате .webp и не более 1000 пикселей в ширину; преобразовать можно <a href="https://image.online-convert.com/ru/convert-to-wbmp">здесь</a>, изменить размер <a href="https://www.iloveimg.com/ru/resize-image">здесь</a></p>
                    </div>
                    <div class="mb-2">
                        <label for="pb" class="text-light d-block">Жирный абзац</label>
                        <textarea type="text" name="pb" class="form-control text-start w-100"></textarea>
                    </div>
                    <div class="mb-2 text-light">
                        <p>* Находится между заголовком и изображением; необязательный элемент</p>
                    </div>
                    <div class="mb-2 p1">
                        <label for="p1" class="text-light d-block">Абзац 1</label>
                        <textarea type="text" name="p1" class="input-group-text text-start w-100" required></textarea>
                    </div>
                    <div class="my-3 buttons">
                        <div class="d-none num-p" id="1"></div>
                        <div onclick="but_second('news_out')" class="btn btn-danger">Назад</div>
                        <button type="submit" class="btn btn-success float-end">Отправить</button>
                        <div onclick="new_p()" class="btn btn-light float-end mx-2">Добавить абзац</div>
                        <div onclick="del_p()" class="btn btn-light float-end">Удалить абзац</div>
                    </div>
                </form>
            </div></div>`;
            break;
        case "del_news":
            if (fle[0] !== "no") {
                document.querySelector(".main").innerHTML = `<div class="d-flex justify-content-center"><div style="width: 600px">
                <form method="post" id="del-news">
                    <input type="hidden"  name="type" value="del-news"  />
                    <h2 class="text-light px-0">Удалить новость</h2>
                    <div class="mb-2">
                        <label for="path" class="text-light d-block">Ссылка</label>
                        <input type="text" name="path" class="input-group-text text-start w-100" value="${fle[1]}" required>
                    </div>
                    <div class="mb-2 text-light">
                        <p class="mb-1">* Ссылка на новость <t class="text-danger">https://magnavis.ru/info/ozon</t></p>
                        <p class="mb-1">* Никогда не ставить / в конце</p>
                    </div>
                    <div class="my-3 buttons">
                        <div onclick="but_second('news_out')" class="btn btn-danger">Назад</div>
                        <button type="submit" class="btn btn-danger float-end">Удалить</button>
                    </div>
                </form>
            </div></div>`;
            } else {
                document.querySelector(".main").innerHTML = `<div class="d-flex justify-content-center"><div style="width: 600px">
                <form method="post" id="del-news">
                    <input type="hidden"  name="type" value="del-news"  />
                    <h2 class="text-light px-0">Удалить новость</h2>
                    <div class="mb-2">
                        <label for="path" class="text-light d-block">Ссылка</label>
                        <input type="text" name="path" class="input-group-text text-start w-100" required>
                    </div>
                    <div class="mb-2 text-light">
                        <p class="mb-1">* Имя страницы в ссылке <t class="text-danger">https://magnavis.ru/info/ozon</t></p>
                        <p class="mb-1">* Никогда не ставить / в конце</p>
                    </div>
                    <div class="my-3 buttons">
                        <div onclick="but_second('news_out')" class="btn btn-danger">Назад</div>
                        <button type="submit" class="btn btn-danger float-end">Удалить</button>
                    </div>
                </form>
            </div></div>`;
            }
            focus_list_el(["no"])
            break;
        case "ch_news":
            console.log(fle)
            ps = fle[6].split("@");
            if (ps.length < 1) {ps = [""]}
            console.log(ps)
            if (fle[0] !== "no") {
                document.querySelector(".main").innerHTML = `<div class="d-flex justify-content-center"><div style="width: 600px">
                <form method="post" id="add-news" enctype="multipart/form-data">
                    <input type="hidden"  name="type" value="add-news"  />
                    <h2 class="text-light px-0">Новая новость</h2>
                    <div class="mb-2">
                        <label for="title" class="text-light d-block">Заголовок</label>
                        <input type="text" name="title" class="input-group-text text-start w-100" required value="${fle[2]}">
                    </div>
                    <div class="mb-2">
                        <label for="path" class="text-light d-block">Ссылка</label>
                        <input type="text" name="path" class="input-group-text text-start w-100" required value="${fle[1]}">
                    </div>
                    <div class="mb-2 text-light">
                        <p class="mb-1">* Ссылка на новость <t class="text-danger">https://magnavis.ru/info/name</t></p>
                        <p>* Никогда не ставить / в конце</p>
                    </div>
                    <div class="mb-2">
                        <label for="date" class="text-light d-block">Дата</label>
                        <input type="date" name="date" class="input-group-text text-start w-100">
                    </div>
                    <div class="mb-2">
                        <label for="img" class="text-light d-block">Изображение</label>
                        <input type="file" name="img" class="input-group-text text-start w-100" value="${fle[3]}">
                    </div>
                    <div class="mb-2">
                        <label for="img2" class="text-light d-block">Изображение 2</label>
                        <input type="file" name="img2" class="input-group-text text-start w-100" value="${fle[4]}">
                    </div>
                    <div class="mb-2 text-light">
                        <p class="mb-1">* Второе изображение (горизонтальная версия) нужно если основное сильно вытянуто по высоте для лучшего отображения статьи</p>
                        <p>* Все изображения должны быть в формате .webp и не более 1000 пикселей в ширину; преобразовать можно <a href="https://image.online-convert.com/ru/convert-to-wbmp">здесь</a>, изменить размер <a href="https://www.iloveimg.com/ru/resize-image">здесь</a></p>
                    </div>
                    <div class="mb-2">
                        <label for="pb" class="text-light d-block">Жирный абзац</label>
                        <textarea type="text" name="pb" class="form-control text-start w-100">${fle[5]}</textarea>
                    </div>
                    <div class="mb-2 text-light">
                        <p>* Находится между заголовком и изображением; необязательный элемент</p>
                    </div>
                    <div class="mb-2 p1">
                        <label for="p1" class="text-light d-block">Абзац 1</label>
                        <textarea type="text" name="p1" class="input-group-text text-start w-100" required>${ps[0]}</textarea>
                    </div>
                    <div class="my-3 buttons">
                        <div class="d-none num-p" id="1"></div>
                        <div onclick="but_second('news_out')" class="btn btn-danger">Назад</div>
                        <button type="submit" class="btn btn-success float-end">Отправить</button>
                        <div onclick="new_p()" class="btn btn-light float-end mx-2">Добавить абзац</div>
                        <div onclick="del_p()" class="btn btn-light float-end">Удалить абзац</div>
                    </div>
                </form>
            </div></div>`;
            if (ps.length > 1) {
                for (let i = 1; i < ps.length; i++) {
                    new_p();
                    console.log((document.getElementsByName("p" + String(i + 1))), "p"+String(i+1), ps[i]);
                    // document.getElementsByName("p"+String(i+1)).value += `${ps[i]}`;
                    // document.getElementsByName("p"+String(i+1)).value += 'kjhkjhkjhkjhkjhk';
                    document.querySelector(`p_${i+1}`).value += `${ps[i]}`;
                }
            }
            } else {
                document.querySelector(".main").innerHTML = `<div class="d-flex justify-content-center"><div style="width: 600px">
                <form method="post" id="add-news" enctype="multipart/form-data">
                    <input type="hidden"  name="type" value="add-news"  />
                    <h2 class="text-light px-0">Новая новость</h2>
                    <div class="mb-2">
                        <label for="title" class="text-light d-block">Заголовок</label>
                        <input type="text" name="title" class="input-group-text text-start w-100" required>
                    </div>
                    <div class="mb-2">
                        <label for="path" class="text-light d-block">Ссылка</label>
                        <input type="text" name="path" class="input-group-text text-start w-100" required value="https://magnavis.ru/info/">
                    </div>
                    <div class="mb-2 text-light">
                        <p class="mb-1">* Ссылка на новость <t class="text-danger">https://magnavis.ru/info/name</t></p>
                        <p>* Никогда не ставить / в конце</p>
                    </div>
                    <div class="mb-2">
                        <label for="date" class="text-light d-block">Дата</label>
                        <input type="date" name="date" class="input-group-text text-start w-100">
                    </div>
                    <div class="mb-2">
                        <label for="img" class="text-light d-block">Изображение</label>
                        <input type="file" name="img" class="input-group-text text-start w-100">
                    </div>
                    <div class="mb-2">
                        <label for="img2" class="text-light d-block">Изображение 2</label>
                        <input type="file" name="img2" class="input-group-text text-start w-100">
                    </div>
                    <div class="mb-2 text-light">
                        <p class="mb-1">* Второе изображение (горизонтальная версия) нужно если основное сильно вытянуто по высоте для лучшего отображения статьи</p>
                        <p>* Все изображения должны быть в формате .webp и не более 1000 пикселей в ширину; преобразовать можно <a href="https://image.online-convert.com/ru/convert-to-wbmp">здесь</a>, изменить размер <a href="https://www.iloveimg.com/ru/resize-image">здесь</a></p>
                    </div>
                    <div class="mb-2">
                        <label for="pb" class="text-light d-block">Жирный абзац</label>
                        <textarea type="text" name="pb" class="form-control text-start w-100"></textarea>
                    </div>
                    <div class="mb-2 text-light">
                        <p>* Находится между заголовком и изображением; необязательный элемент</p>
                    </div>
                    <div class="mb-2 p1">
                        <label for="p1" class="text-light d-block">Абзац 1</label>
                        <textarea type="text" name="p1" class="input-group-text text-start w-100" required></textarea>
                    </div>
                    <div class="my-3 buttons">
                        <div class="d-none num-p" id="1"></div>
                        <div onclick="but_second('news_out')" class="btn btn-danger">Назад</div>
                        <button type="submit" class="btn btn-success float-end">Отправить</button>
                        <div onclick="new_p()" class="btn btn-light float-end mx-2">Добавить абзац</div>
                        <div onclick="del_p()" class="btn btn-light float-end">Удалить абзац</div>
                    </div>
                </form>
            </div></div>`;
            }
            focus_list_el(["no"])
            break;
        case "news_out":
            focus_list_el(["no"])
            // document.querySelector(".main").innerHTML = `<h1 class="text-light">список новостей</h1>`;
            data_update("news-data");
            break;
        case "add_titles":
            focus_list_el(["no"])
            document.querySelector(".main").innerHTML = `<div class="d-flex justify-content-center"><div style="width: 600px">
                <form method="post" id="add-titles">
                    <input type="hidden"  name="type" value="add-titles"  />
                    <h2 class="text-light px-0">Новый title</h2>
                    <div class="mb-2">
                        <label for="title" class="text-light d-block">Заголовок</label>
                        <input type="text" name="title" class="input-group-text text-start w-100" required>
                    </div>
                    <div class="mb-2">
                        <label for="path" class="text-light d-block">Ссылка</label>
                        <input type="text" name="path" class="input-group-text text-start w-100" required  value="https://magnavis.ru/">
                    </div>
                    <div class="mb-2 text-light">
                        <p class="mb-1">* Имя страницы в ссылке <t class="text-danger">https://magnavis.ru/info/ozon</t></p>
                        <p>* Никогда не ставить / в конце</p>
                        
                    </div>
                    <div class="my-3 buttons">
                        <div onclick="but_second('titles_out')" class="btn btn-danger">Назад</div>
                        <button type="submit" class="btn btn-success float-end">Добавить</button>
                    </div>
                </form>
            </div></div>`;
            break;
        case "del_titles":
            if (fle[0] !== "no") {
                document.querySelector(".main").innerHTML = `<div class="d-flex justify-content-center"><div style="width: 600px">
                <form method="post" id="del-titles">
                    <input type="hidden"  name="type" value="del-titles"  />
                    <h2 class="text-light px-0">Удалить title</h2>
                    <div class="mb-2">
                        <label for="path" class="text-light d-block">Ссылка</label>
                        <input type="text" class="input-group-text text-start w-100" value="${fle[1]}" required disabled>
                        <input type="hidden" name="path" class="input-group-text text-start w-100" value="${fle[1]}" required>
                    </div>
                    <div class="mb-2 text-light">
                        <p class="mb-1">* Имя страницы в ссылке <t class="text-danger">https://magnavis.ru/info/ozon</t></p>
                        <p class="mb-1">* Для главной страницы это "home"</p>
                        <p class="mb-1">* Никогда не ставить / в конце</p>
                        <p class="text-danger">* После удаления заголовка страницы следует тут же добавить новый, иначе заголовок страницы будет пустым</p>
                    </div>
                    <div class="my-3 buttons">
                        <div onclick="but_second('titles_out')" class="btn btn-danger">Назад</div>
                        <button type="submit" class="btn btn-danger float-end">Удалить</button>
                    </div>
                </form>
            </div></div>`;
            } else {
                document.querySelector(".main").innerHTML = `<div class="d-flex justify-content-center"><div style="width: 600px">
                <form method="post" id="del-titles">
                    <input type="hidden"  name="type" value="del-titles"  />
                    <h2 class="text-light px-0">Удалить title</h2>
                    <div class="mb-2">
                        <label for="path" class="text-light d-block">Ссылка</label>
                        <input type="text" name="path" class="input-group-text text-start w-100" required>
                    </div>
                    <div class="mb-2 text-light">
                        <p class="mb-1">* Имя страницы в ссылке <t class="text-danger">https://magnavis.ru/info/ozon</t></p>
                        <p class="mb-1">* Для главной страницы это "home"</p>
                        <p class="mb-1">* Никогда не ставить / в конце</p>
                        <p class="text-danger">* После удаления заголовка страницы следует тут же добавить новый, иначе заголовок страницы будет пустым</p>
                    </div>
                    <div class="my-3 buttons">
                        <div onclick="but_second('titles_out')" class="btn btn-danger">Назад</div>
                        <button type="submit" class="btn btn-danger float-end">Удалить</button>
                    </div>
                </form>
            </div></div>`;
            }
            focus_list_el(["no"])
            break;
        case "ch_titles":
            console.log(fle)
            if (fle[0] !== "no") {
                document.querySelector(".main").innerHTML = `<div class="d-flex justify-content-center"><div style="width: 600px">
                <form method="post" id="ch-titles">
                    <input type="hidden"  name="type" value="ch-titles"  />
                    <h2 class="text-light px-0">Редактировать title</h2>
                    <div class="mb-2">
                        <label for="title" class="text-light d-block">Заголовок</label>
                        <input type="text" name="title" class="input-group-text text-start w-100" value="${fle[2]}" required>
                    </div>
                    <div class="mb-2">
                        <label for="path" class="text-light d-block">Ссылка</label>
                        <input type="text" name="path" class="input-group-text text-start w-100" value="${fle[1]}" required>
                        <input type="hidden" name="path_old" class="input-group-text text-start w-100" value="${fle[1]}" required>
                    </div>
                    <div class="mb-2 text-light">
                        <p class="mb-1">* Имя страницы в ссылке <t class="text-danger">https://magnavis.ru/info/ozon</t></p>
                        <p class="mb-1">* Для главной страницы это "home"</p>
                        <p>* Никогда не ставить / в конце</p>
                        
                    </div>
                    <div class="my-3 buttons">
                        <div onclick="but_second('titles_out')" class="btn btn-danger">Назад</div>
                        <button type="submit" class="btn btn-success float-end">Сохранить</button>
                    </div>
                </form>
            </div></div>`;
            } else {
                document.querySelector(".main").innerHTML = `<div class="d-flex justify-content-center"><div style="width: 600px">
                <form method="post" id="ch-titles">
                    <input type="hidden"  name="type" value="ch-titles"  />
                    <h2 class="text-light px-0">Редактировать title</h2>
                    <div class="mb-2">
                        <label for="title" class="text-light d-block">Заголовок</label>
                        <input type="text" name="title" class="input-group-text text-start w-100" required>
                    </div>
                    <div class="mb-2">
                        <label for="path" class="text-light d-block">Ссылка</label>
                        <input type="text" name="path" class="input-group-text text-start w-100" required>
                    </div>
                    <div class="mb-2 text-light">
                        <p class="mb-1">* Имя страницы в ссылке <t class="text-danger">https://magnavis.ru/info/ozon</t></p>
                        <p class="mb-1">* Для главной страницы это "home"</p>
                        <p>* Никогда не ставить / в конце</p>
                        
                    </div>
                    <div class="my-3 buttons">
                        <div onclick="but_second('titles_out')" class="btn btn-danger">Назад</div>
                        <button type="submit" class="btn btn-success float-end">Сохранить</button>
                    </div>
                </form>
            </div></div>`;
            }
            focus_list_el(["no"])
            break;
        case "titles_out":
            focus_list_el(["no"])
            // document.querySelector(".main").innerHTML = `<h1 class="text-light">список заголовков</h1>`;
            data_update("titles-data");
            break;
    }
}


$(document).on('submit','#add-news',function(e) {console.log('hello');e.preventDefault();$.ajax({type:'POST', url:'/',})});
$(document).on('submit','#add-titles',function(e) {console.log('hello');e.preventDefault();$.ajax({type:'POST', url:'/',})});
$(document).on('submit','#del-titles',function(e) {console.log('hello');e.preventDefault();$.ajax({type:'POST', url:'/',})});