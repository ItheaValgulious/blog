window.onload=()=>{
    for(var img of document.querySelectorAll('img')){
        if(img.getAttribute('src').startsWith('../imgs')){
            img.src=img.getAttribute('src').replace('..','');
        }
    }
}