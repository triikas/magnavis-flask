/*!***************************************************
 * yatranslate.js v1.0.0
 * https://Get-Web.Site/
 * author: Vitalii P.
 *****************************************************/

const yatranslate = {
    lang: "ru",
    // langFirstVisit: 'en',
};

document.addEventListener('DOMContentLoaded', function () {
    yaTranslateInit();
})

function yaTranslateInit() {

    if (yatranslate.langFirstVisit && !localStorage.getItem('yt-widget')) {
        yaTranslateSetLang(yatranslate.langFirstVisit);
    }

    let script = document.createElement('script');
    script.src = `https://translate.yandex.net/website-widget/v1/widget.js?widgetId=ytWidget&pageLang=${yatranslate.lang}&widgetTheme=light&autoMode=false`;
    document.getElementsByTagName('head')[0].appendChild(script);

    let code = yaTranslateGetCode();

    yaTranslateHtmlHandler(code);

    yaTranslateEventHandler('click', '[data-ya-lang]', function (el) {
        yaTranslateSetLang(el.getAttribute('data-ya-lang'));
        window.location.reload();
    })
}

function yaTranslateSetLang(lang) {
    localStorage.setItem('yt-widget', JSON.stringify({
        "lang": lang,
        "active": true
    }));
}

function yaTranslateGetCode() {
    return (localStorage["yt-widget"] != undefined && JSON.parse(localStorage["yt-widget"]).lang != undefined) ? JSON.parse(localStorage["yt-widget"]).lang : yatranslate.lang;
}

function yaTranslateHtmlHandler(code) {
    var lang_size = [28, 56, 22, 58, 22, 50];
    if (!document.querySelector("footer").classList.contains("user-agent")) {
        for (let i = 0; i < 6; i++) {
            lang_size[i] /= 2;
        }
    }
    if (code === 'zh') {
        document.querySelector('[data-lang-active]').innerHTML = `<img style="height: ${lang_size[0]}px; width: ${lang_size[1]}px;" src="../static/img/${code}2w.png">`;
        try {
            var doc = document.querySelectorAll(".cost-sp-2");
            for (let i of Array(4).keys()) {
                doc[i].classList.add("cost-sp-zh");
            }
        } catch (err) {}
    } else if (code === 'en') {
        document.querySelector('[data-lang-active]').innerHTML = `<img style="height: ${lang_size[2]}px; width: ${lang_size[3]}px;" src="../static/img/${code}2w.png">`;
        try {
            var doc = document.querySelectorAll(".cost-sp");
            for (let i of Array(4).keys()) {
                doc[i].classList.add("cost-sp-en");
            }
        } catch (err) {}
    }
    else {
        document.querySelector('[data-lang-active]').innerHTML = `<img style="height: ${lang_size[4]}px; width: ${lang_size[5]}px;" src="../static/img/${code}2w.png">`;
    }

}
function yaTranslateEventHandler(event, selector, handler) {
    document.addEventListener(event, function (e) {
        let el = e.target.closest(selector);
        if (el) handler(el);
    });
}