 let post_container = document.querySelector(".post_container");

 window.onload = () => {

    fetch('http://localhost:8000/posts/',)
    .then(res => res.json())
    .then(res => console.log(res))
 }
 const showpost = (elem, flag)=>{
     flag== 1 ? elem.setAttribute("style","visibility:hidden; display:none;"): elem.setAttribute("style, "visibility: display:grid);
 }
 document.querySelector("#post_back").onclick=()=>showpost(document.querySelector('.add_post_container'),1)
 document.querySelector(".floating_create_post").onclick=()=>showpost(document.querySelector('.add_post_container'),0)
 document.querySelector("#post_back").onclick=()=>addpost{}

 let post_media= document.querySelector('#post_media');
 post_media.onchange=()=>{
     if(["png","jpg","jpeg"].indexOf(post_media.files[0].name.toLowerCase().split(".")[1])<0){
         alert('Only Images can be posted for now');
         return
     }
     let path = window.URL.createObjectURL(post_media.files[0]).split("/");
     console.log('blob:null/${path[path.length - 1]}');
     document.querySelector(".post_media_label").textContent=post_media.files[0].name.substring(0,20)+ "...";
 }


   
