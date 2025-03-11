let menu = document.querySelector('#menu-button');
let header = document.querySelector('.header');

menu.addEventListener("click",  () =>{
    menu.classList.toggle('fa-times'); 
    header.classList.toggle('active'); 
    document.body.classList.toggle('active'); 
}
);

window.addEventListener("scroll",  () =>{
    if(window.innerWidth < 991){
        menu.classList.remove('fa-times'); 
        header.classList.remove('active');
        document.body.classList.remove('active');
    } 
}
);

