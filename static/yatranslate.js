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
    let lg = {
        'en':'ENG',
        'ru':'РУС',
        'zh':'中文'
    };
    document.querySelector('[data-lang-active]').innerHTML = lg[code];
}

function yaTranslateEventHandler(event, selector, handler) {
    document.addEventListener(event, function (e) {
        let el = e.target.closest(selector);
        if (el) handler(el);
    });
}