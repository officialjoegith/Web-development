let slidetext = document.querySelector(".slidetext");
let container = document.querySelector(".container");
let textArray = [ "@officialjoegith","You are Welcome"]
let imageArray = ["image/Hydrangeas.jpg","image/Jellyfish.jpg"]
let pointerT = 0;
let pointerI = 0;
function changeText(text){
    slidetext.textContent = text;

}
function changeimage(url){
    container.style.backgroundImage = `url("${url}")`;
} 
setInterval(
    ()=>{
        if (pointerT == textArray.length) pointerT = 0;
        if (pointerI == imageArray.length) pointerI = 0;
            changeText(textArray[pointerT]);
            changeimage(imageArray[pointerI]);
            pointerT++;
            pointerI++;

       
    }, 2000
);