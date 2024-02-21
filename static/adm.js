function new_p () {
    num_p = String(Number(document.querySelector(".num-p").getAttribute("id")) + 1);
    document.querySelector(".num-p").id = num_p;
    p = document.createElement("div");
    p.classList.add(`mb-2`, `p${num_p}`);
    p.innerHTML = `<label for="${num_p}" class="text-light d-block">Абзац ${num_p}</label><input type="text" name="${num_p}" class="input-group-text text-start w-100">`
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


function but (b) {
    switch (b) {
        case "add_news":
            document.querySelector(".main").classList.add("d-none");
            document.querySelector(".add-news").classList.remove("d-none");
            break;
        case "add_news_main":
            document.querySelector(".add-news").classList.add("d-none");
            document.querySelector(".main").classList.remove("d-none");
            break;
        case "del_news":
            document.querySelector(".main").classList.add("d-none");
            document.querySelector(".del-news").classList.remove("d-none");
            break;
        case "del_news_main":
            document.querySelector(".del-news").classList.add("d-none");
            document.querySelector(".main").classList.remove("d-none");
            break;
    }
}