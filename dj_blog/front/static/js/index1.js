window.onload = iniciar();


let layout_marks = [
    'iniciar',
    'selectLanguage', // (e)
    'loadLanguages', //  ()
    'loadPage', // (page, langguage)
    'selectSubmenu', // (e)
    'loadSubmenu', // (item)
    'x_loadPage', // (type)
    'x_manageLayout', // (model, params)
    //----------------------------------
    'manageLayout', // (params)
    'manageLayoutI18n', // (params)
]
//------------------------------
// Montar Languages en menus
//-------------------------

function selectLanguage(e) {
    console.log("SELECT LANGUAGE");
    console.log(localStorage.language + " --> Idioma " + e.target.id);
    let lan = e.target.id
    lan = lan.substring(3,5);
    localStorage.language = lan;
 
    const params = {
        'i18n': true,
        'filtro': `&active=1&internal=0&layout_root_alias=asinex1`,
        'idElement': 'last_alias',
    }     
    manageLayout("layouti18ns", params);
    loadPage(localStorage.page, localStorage.language)
}

function loadLanguages() {
    console.log("load Languages");
    localStorage.language = "es";
    let elem;
    let lans = ["nb1de", "nb1en", "nb1es", "nb1fr", 
                "sb1de", "sb1en", "sb1es", "sb1fr"]
    for (lan in lans) {
        console.log(lan, lans[lan]);
        document.getElementById(lans[lan]).addEventListener('click', selectLanguage);
        elem = document.getElementById(lans[lan]);
        console.log(elem);
    };
}

//------------------------------
// Montar opciones del menu work
//-------------------------
async function loadPage(page, language) {
    const filtro = `?format=json&layout_root_alias=asinex1&note=${page}&grade=${language}`;
    const url = `${localStorage.domain}/apirest/layouti18ns/${filtro}`;
    console.log(url);
    const mainPageId = page.split('-')[0]
    let respuesta = await fetch(url);
    let resultado = await respuesta.json();
    console.log(resultado);
    let data = resultado.results;
    if (data.length > 0) {
        const pageData = data[0];
        // let myPage = document.getElementById(targetId[1]);
        let myPage = document.getElementById(mainPageId);
        let htmlMain = `<div>
                          <h1>${pageData.id}: ${pageData.name}</h1>
                          ${pageData.content}
                        </div`;
        myPage.innerHTML = htmlMain; 
        
    } 
}

function selectSubMenu(e) {
    console.log("SELECT SubMenu"); 
    console.log(e.target.id); // "sb3menu_work3-n"
    const targetId = e.target.id.split('_');
    const page = targetId[1]
    localStorage.page = page
    loadPage(page, localStorage.language)
    const mainPageId = page.split('-')[0]
    window.location.href = `#${mainPageId}` // work3
}      


async function loadSubMenu(item) {

    console.log(`load Submenu: ${item.grade}`);
    // item.alias = 'asinex__sidebar__sidebar3__sb3menu', 
    const addTo = item.grade; // item.grade = sb3menu'
    parentMenu = document.getElementById(addTo); 
    //--------------------------------
    // const params = item.note.json()
    // params = {linkTo=work3}
    const linkTo = addTo.split('_')[1]  // work3
    // let filtro = `grade__startswith=${linkTo}`; 
    let filtro = `note=${linkTo}`; // filtro = work3'
    // obtener los registros para montar el menu.
    // OJO!!! no sirve si hay mas de una layout raiz en la base de datos
    filtro = `format=json&active=1&root_alias=asinex1&${filtro}`;
    const url = `${localStorage.domain}/apirest/layouts/?${filtro}`;
    console.log(url);    
    let respuesta = await fetch(url);
    let resultado = await respuesta.json();
    let data = resultado.results;
    //-----------------------------
    let idList = [];
    let content = "";
    // const clase = `class="w3-bar-item w3-buttom"` 
    data.forEach(function(item) {
        id =`${addTo.split('_')[0]}_${item.grade}` // "sb3menu_work3-n"
        content += `<li id="${id}" class="w3-bar-item w3-buttom"  >${item.name}</li>`
        // <li id="menuWork_01" class="w3-bar-item w3-buttom" >Work 1</li>
        idList.push(id)
    })
    parentMenu.innerHTML = content

    for (item in idList) {
        console.log(item, idList[item]);
        document.getElementById(idList[item]).addEventListener('click', selectSubMenu);
        elem = document.getElementById(idList[item]);
        console.log(elem);
    };

};


//------------------------------
// Cargar Pagina
//-----------------------------




async function x_loadPage(type) {
    console.log("readPage type = " + type);
    let page = ""
    if (type == 1) {
        console.log("readPage tipo 1");
        const filtro = `${localStorage.pageId}/?format=json`;
        const url = `http://127.0.0.1:8010/asinex/apirest/flayouts/${filtro}`;
        console.log(url);
    
        let respuesta = await fetch(url);
        let resultado = await respuesta.json();
        console.log(resultado);
        console.log(resultado.id, resultado.name);
        page = resultado;
        localStorage.pageKey = page.sort;
    } else {
        console.log("readPage tipo 2");
        const filtro = `format=json&active=1&grade=${localStorage.language}&sort=${localStorage.pageKey}`;
        const url = `http://127.0.0.1:8010/asinex/apirest/layouts/?${filtro}`;
        console.log(url);    
    
        let respuesta = await fetch(url);
        let resultado = await respuesta.json();
        console.log(resultado);
        let data = resultado.results;
        if (data.length > 0) {
            page = data[0];
        };
    };
    console.log(page)
    let myPage = document.getElementById("work");
    let htmlMain = getPage(page);
    myPage.innerHTML = htmlMain;    
};




// Modal Image Gallery
function onClick(element) {
    document.getElementById("img01").src = element.src;
    document.getElementById("modal01").style.display = "block";
    var captionText = document.getElementById("caption");
    captionText.innerHTML = element.alt;
}

//----------------------------
// mySidebar
//---------------------------
// Toggle between showing and hiding the sidebar when clicking the menu icon
var mySidebar = document.getElementById("sideBar");

function w3_open() {
    if (mySidebar.style.display === 'block') {
    mySidebar.style.display = 'none';
    } else {
    mySidebar.style.display = 'block';
    }
}

// Close the sidebar with the close button
function w3_close() {
    mySidebar.style.display = "none";
}


function x_myDropFunc() {
    var x = document.getElementById("sb1menulan");
    if (x.className.indexOf("w3-show") == -1) {
      x.className += " w3-show";
      x.previousElementSibling.className += " w3-theme-d5";
    } else { 
      x.className = x.className.replace(" w3-show", "");
      x.previousElementSibling.className = 
      x.previousElementSibling.className.replace(" w3-theme-d5", "");
    }
}

function myAccFunc() {
    var x = document.getElementById("sb3menu_work3");
    if (x.className.indexOf("w3-show") == -1) {
      x.className += " w3-show";
      x.previousElementSibling.className += " w3-theme-d5";
    } else { 
      x.className = x.className.replace(" w3-show", "");
      x.previousElementSibling.className = 
      x.previousElementSibling.className.replace(" w3-theme-d5", "");
    }
}



function iniciar() {
    localStorage.domain = "http://127.0.0.1:8010/asinex";
    localStorage.language = "es";
    localStorage.age0 = "work3-1";
    let params;
    //----------------------------------
    params = {
        'filtro': `&active=1&internal=0&root_alias__=asinex1`,
        'idElement': 'grade', 

    } 
    manageLayout("layouts", params);
    // loadLanguages();
    // loadMenuWork("layouts", "sb3menuwork", "_05_03_");

    // ------------------------------------
    params = {
        'filtro': `&active=1&internal=0&layout_root_alias=asinex1`,
        'idElement': 'note',
    } 

    manageLayout("layouti18ns", params);
    loadPage(localStorage.page, localStorage.language)
}


async function manageLayout(model, params) {
    console.log(`Ejecutar  manageLayout model=${model} params=${params}`);

    let filtro = `format=json${params.filtro}`;
   
    const url = `${localStorage.domain}/apirest/${model}/?${filtro}`;
    console.log(url);    

 
    const layoutMarks = [
        'iniciar',
        'selectLanguage', // (e)
        'loadLanguages', //  ()
        'loadPage', // (page, langguage)
        'selectSubmenu', // (e)
        'loadSubmenu', // (item)
        'x_loadPage', // (type)
        'manageLayout', // (model, params)
    ]

    let respuesta = await fetch(url);
    let resultado = await respuesta.json();
    let data = resultado.results;
    // console.log(resultado);
    // console.log(data);
    let idElement;
    let mark;
    let element;

    data.forEach(function(item) {
        mark = item.mark
        idElement = item[params.idElement]
        element = document.getElementById(idElement);
        
        console.log(`--- model=${model} alias=${item.grade} mark=${mark} -- idElement=${idElement}` )
        switch (mark) {
            case 'loadLanguages':
                loadLanguages(item);
                break;
            case 'loadSubMenu':
                loadSubMenu(item) 
                break;
            // case 'loadDashboard()':
            //     loadDashboard();
            //     break;
            case null:
                break;
            default:
                // if (mark in defaultMarks){
                if (defaultMarks.includes(mark)) {
                    // console.log("mark SI ESTA EN defaultMarks")
                    if (element != null) { 
                        console.log("mark SI ESTA EN defaultMarks y elem !=  null")
                        const prefix = mark.split('__')[0];
                        const sufix = mark.split('__')[1];
                        element[prefix] = item[sufix];   
                    } else {
                        console.log("mark SI ESTA EN defaultMarks pero element = null")
                    }
                } else {
                    console.log("mark NO ESTA EN defaultMarks")
                }
                break;
            };
        }
    );
};

async function manageLayoutI18n(model, params) {
    console.log(`Ejecutar  manageLayout model=${model} paramss=${params}`);

    let filtro = `format=json${params.filtro}`;
    if (params.i18n) {
        filtro = `${filtro}&grade=${localStorage.language}`
    };
   
    const url = `${localStorage.domain}/apirest/${model}/?${filtro}`;
    console.log(url);    

    const defaultMarks = [
        'innerHTML__name', 'innerHTML__note', 'innerHTML__content', 
    ]
 
    let respuesta = await fetch(url);
    let resultado = await respuesta.json();
    let data = resultado.results;
    // console.log(resultado);
    // console.log(data);
    let idElement;
    let mark;
    let element;

    data.forEach(function(item) {
        mark = item.mark
        idElement = item[params.idElement]
        element = document.getElementById(idElement);
        
        console.log(`--- model=${model} alias=${item.grade} mark=${mark} -- idElement=${idElement}` )

        if (defaultMarks.includes(mark)) {
            // console.log("mark SI ESTA EN defaultMarks")
            if (element != null) { 
                console.log("mark SI ESTA EN defaultMarks y elem !=  null")
                const prefix = mark.split('__')[0];
                const sufix = mark.split('__')[1];
                element[prefix] = item[sufix];   
            } else {
                console.log("mark SI ESTA EN defaultMarks pero element = null")
            }
        } else {
            console.log("mark NO ESTA EN defaultMarks")
        }

        }
    );
};
